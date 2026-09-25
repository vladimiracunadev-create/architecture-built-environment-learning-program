# Descargas y artefactos

## Lectura

- [Catálogo HTML de las 680 clases](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/catalogo.html): páginas rápidas, enlazables e imprimibles.
- [Lector offline v1.0](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/lector-offline-v1.0.html): aplicación monolítica autosuficiente con búsqueda, filtros y progreso local.

## PDF

- [Clases ARQ-661–680](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/Arquitectura_20_Clases_Finales_v1.0.pdf).
- [ARQ-680 · clase completa](https://vladimiracunadev-create.github.io/architecture-built-environment-learning-program/ARQ-680_Clase_Completa_v1.0.pdf).

## Integridad

El repositorio conserva [`SHA256SUMS.txt`](https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program/blob/main/SHA256SUMS.txt) para comprobar los entregables originales. El workflow de integración continua vuelve a verificar esos hashes en cada cambio.

## Fuente editable

Las 680 clases viven en `classes/parte-XX/ARQ-XXX.md`. El sitio se regenera con:

```bash
python -m pip install -r requirements-build.txt
python scripts/generate_curriculum_docs.py
python scripts/build_site.py
python scripts/validate_repo.py
```
