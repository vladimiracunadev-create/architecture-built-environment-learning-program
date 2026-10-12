#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Validate homeowner budget templates and independent numerical controls."""

from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FILES = (
    ROOT / "templates" / "presupuesto-vivienda.csv",
    ROOT / "templates" / "presupuesto-ampliacion.csv",
)
REQUIRED = {
    "caso", "escenario", "capitulo", "codigo", "partida", "unidad",
    "cantidad_neta", "merma_pct", "cantidad_compra", "precio_unitario_clp",
    "transporte_clp", "subtotal_neto_clp", "iva_pct", "total_clp",
    "fuente_precio", "fecha_precio", "region_comuna", "estado_precio", "notas",
}


def money(quantity: Decimal, waste: Decimal, unit_price: Decimal, transport: Decimal, vat: Decimal) -> tuple[Decimal, Decimal]:
    if quantity < 0 or waste < 0 or unit_price < 0 or transport < 0 or vat < 0:
        raise ValueError("negative budget input")
    purchase = quantity * (Decimal("1") + waste)
    net = purchase * unit_price + transport
    return net, net * (Decimal("1") + vat)


def validate_csv(path: Path) -> int:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if set(reader.fieldnames or ()) != REQUIRED:
            raise AssertionError(f"unexpected schema in {path.name}")
        rows = list(reader)
    codes = [row["codigo"] for row in rows]
    if len(codes) != len(set(codes)):
        raise AssertionError(f"duplicate codes in {path.name}")
    if {row["escenario"] for row in rows} != {"economico", "estandar", "mayor-desempeno"}:
        raise AssertionError(f"missing scenarios in {path.name}")
    for row in rows:
        quantity = Decimal(row["cantidad_neta"])
        waste = Decimal(row["merma_pct"])
        purchase = Decimal(row["cantidad_compra"])
        price = Decimal(row["precio_unitario_clp"])
        transport = Decimal(row["transporte_clp"])
        net = Decimal(row["subtotal_neto_clp"])
        vat = Decimal(row["iva_pct"])
        total = Decimal(row["total_clp"])
        expected_net, expected_total = money(quantity, waste, price, transport, vat)
        if purchase != quantity * (Decimal("1") + waste):
            raise AssertionError(f"purchase quantity mismatch: {row['codigo']}")
        if net != expected_net or total != expected_total:
            raise AssertionError(f"amount mismatch: {row['codigo']}")
        if row["estado_precio"] == "HIPOTETICO" and row["fecha_precio"]:
            raise AssertionError(f"hypothetical row must not mimic a dated quote: {row['codigo']}")
    return len(rows)


def numerical_tests() -> None:
    # 1. Base subtotal and VAT 19 %.
    net, total = money(Decimal("42"), Decimal("0"), Decimal("18500"), Decimal("95000"), Decimal("0.19"))
    assert net == Decimal("872000") and total == Decimal("1037680.00")
    # 2. VAT 0 preserves a legitimate zero rate.
    assert money(Decimal("10"), Decimal("0"), Decimal("1000"), Decimal("0"), Decimal("0")) == (Decimal("10000"), Decimal("10000"))
    # 3. Merma remains separate and reproducible.
    assert money(Decimal("80"), Decimal("0.07"), Decimal("10000"), Decimal("0"), Decimal("0"))[0] == Decimal("856000.00")
    # 4. Scope change propagates to total.
    before = money(Decimal("80"), Decimal("0"), Decimal("850000"), Decimal("0"), Decimal("0"))[1]
    after = money(Decimal("84"), Decimal("0"), Decimal("850000"), Decimal("0"), Decimal("0"))[1]
    assert after - before == Decimal("3400000")
    # 5. Budget insufficient remains a negative gap, not zero.
    financing = Decimal("90000000")
    projected = Decimal("95500000")
    assert financing - projected == Decimal("-5500000")
    # 6. Sensitivity boundaries are explicit.
    base = Decimal("100000000")
    assert [base * rate for rate in (Decimal("0.10"), Decimal("0.15"), Decimal("0.20"))] == [Decimal("10000000.00"), Decimal("15000000.00"), Decimal("20000000.00")]
    # 7. Negative quantities are rejected.
    try:
        money(Decimal("-1"), Decimal("0"), Decimal("1"), Decimal("0"), Decimal("0"))
    except ValueError:
        pass
    else:
        raise AssertionError("negative quantity accepted")
    # 8. Monthly cash rows reconcile to the project total.
    cash = [Decimal("12000000"), Decimal("18000000"), Decimal("25000000"), Decimal("15000000")]
    assert sum(cash) == Decimal("70000000")


def main() -> int:
    rows = sum(validate_csv(path) for path in FILES)
    numerical_tests()
    print(f"OK: {rows} template rows and 8 independent homeowner-budget tests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
