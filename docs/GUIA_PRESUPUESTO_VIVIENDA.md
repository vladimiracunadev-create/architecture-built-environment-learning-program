# Guía de presupuesto para vivienda nueva y ampliación

## Alcance

Esta guía acompaña ARQ-809, ARQ-816, ARQ-817 y ARQ-827. Las plantillas permiten aprender a cubicar, cotizar, comparar, programar pagos y proyectar el costo a término. No reemplazan cubicaciones, presupuestos, contratos, impuestos ni liquidaciones preparados o revisados por personas competentes.

Los ejemplos de CASA-NUEVA-80 y AMPLIACION-24 están marcados `HIPOTÉTICO`. No afirman precios vigentes de 2026. Para publicar un precio como vigente se exigen fuente accesible, fecha, región/comuna, unidad, calidad, IVA, transporte, plazo y disponibilidad; se comparan tres cotizaciones equivalentes o se declara que no fue posible obtenerlas.

## Cuatro niveles de estimación

| Nivel | Momento | Unidad y base | Uso permitido | No permite |
|---|---|---|---|---|
| A · orden de magnitud | decisión inicial | m² y rango con alcance declarado | comparar alternativas y financiamiento | contratar o comprar |
| B · capítulos | anteproyecto | suma de capítulos | asignar reservas y prioridades | ocultar omisiones en un porcentaje |
| C · partidas y APU | proyecto coordinado | cantidad × recursos y rendimiento | licitar y auditar ofertas | usar rendimientos no comprobados |
| D · control a término | ejecución | base + cambios + compromisos + saldo | decidir pagos y proyectar cierre | confundir factura, pago y avance físico |

Cada nivel conserva la fecha y la versión de planos que lo originó. Cuando cambia el alcance, no se sobreescribe el total anterior: se crea una revisión y una orden de cambio.

## Campos de las plantillas

| Campo | Qué registra | Error que evita |
|---|---|---|
| `caso` | CASA-NUEVA-80 o AMPLIACION-24 | mezclar expedientes |
| `escenario` | económico, estándar o mayor desempeño | comparar calidades sin nombre |
| `capitulo` | grupo de alcance | perder partidas pequeñas |
| `codigo` | identificador único | duplicar una partida |
| `unidad` | m, m², m³, kg, unidad, hora o global | multiplicar magnitudes incompatibles |
| `cantidad_neta` | medición antes de merma | esconder error dentro de compra |
| `merma_pct` | hipótesis separada | inflar cantidad sin explicación |
| `cantidad_compra` | neta × (1 + merma), redondeada si aplica | comprar fracciones imposibles |
| `precio_unitario_clp` | precio sin transporte, con base declarada | confundir catálogo y costo puesto en obra |
| `transporte_clp` | costo por partida o lote | omitir logística |
| `subtotal_neto_clp` | cantidad × precio + transporte | sumar IVA dos veces |
| `iva_pct` | tasa configurable | fijar 19 % a partidas no comprobadas |
| `total_clp` | neto + IVA aplicable | confundir total neto y bruto |
| `fuente_precio` y `fecha_precio` | cotización o estado hipotético | presentar dato antiguo como vigente |
| `estado_precio` | catálogo, cotizado, pagado, estimado o hipotético | borrar la procedencia |

## Fórmulas base

```text
cantidad_compra = cantidad_neta × (1 + merma_pct)
subtotal_neto = cantidad_compra × precio_unitario + transporte
iva = subtotal_neto × iva_pct
total_partida = subtotal_neto + iva
contingencia = base_seleccionada × tasa_hipotética
costo_a_término = costo_real + comprometido_pendiente + estimación_saldo + cambios_probables
brecha_financiera = financiamiento_disponible − costo_a_término
```

La contingencia no se aplica automáticamente sobre cualquier subtotal. La plantilla expone su base y tasa para que el usuario pueda comprobarla. Se prueban 10 %, 15 % y 20 % como sensibilidad didáctica; el valor real depende de madurez del proyecto y riesgos.

## IVA, UF y derechos municipales

CLP es la moneda de registro. Si una cotización usa UF, se añade fecha de la UF y fuente oficial; la equivalencia no se guarda como constante eterna. El IVA se aplica solo a filas marcadas como afectas. Una tasa de 0 % es una entrada deliberada que debe conservarse y no confundirse con dato ausente.

El artículo 130 LGUC registra 1,5 % del presupuesto para obra nueva y ampliación. La operación es una referencia legal, no un porcentaje universal para todos los trámites. La base municipal, descuentos, exenciones, pagos previos y cobros adicionales se verifican en la DOM. Ejemplo didáctico: `CLP 70.000.000 × 1,5 % = CLP 1.050.000`.

## Escenarios y métodos de contratación

Los tres escenarios conservan superficies y funciones comparables. Una mejora se describe mediante material, desempeño, vida útil, prueba o mantenimiento; “premium” no basta. Se contrastan contratista general y contratación por partidas. La segunda opción puede reducir margen aparente, pero agrega coordinación, inspección, interfaces, seguros y riesgo del propietario.

En AMPLIACION-24 se separan demolición selectiva, protecciones, encuentro de cubierta, refuerzos pendientes, redes, continuidad de servicios, limpieza y recuperación. No se usa el costo por m² de la casa nueva como sustituto.

## Flujo de caja y pagos

Cada pago se vincula con alcance, avance físico observado, evidencia, retención si existe y aprobación responsable. Anticipo, material acopiado, trabajo ejecutado, factura y pago son estados distintos. La curva mensual compara previsto, comprometido, pagado y proyección a término.

No se paga una modificación sin orden de cambio que identifique hecho, alternativa, costo, plazo, permiso o nueva aprobación y versión contractual.

## Controles automáticos y manuales

Ejecuta:

```bash
python scripts/validate_homeowner_budget.py
```

El script prueba sumas, IVA 0/19 %, mermas, cambio de alcance, presupuesto insuficiente, sensibilidad, duplicados, cantidades negativas y reconciliación de flujo. Además:

- comprueba manualmente una partida con calculadora independiente;
- busca códigos duplicados;
- filtra precios sin fuente o fecha;
- verifica que ninguna cantidad o precio sea negativo;
- compara total por partidas con total por capítulos;
- cambia merma, IVA y contingencia para confirmar que los resultados reaccionan;
- vuelve a abrir el `.xlsx` y comprueba fórmulas y formato.

## Puerta de detención

El estado es `DETENER` cuando el costo a término supera financiamiento y reserva, o cuando una condición legal/técnica puede cambiar materialmente el alcance. El presupuesto no “cierra” asignando cero a lo desconocido. Se rediseña, financia, estudia o posterga.
