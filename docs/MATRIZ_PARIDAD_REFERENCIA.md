# Matriz de paridad documental con la referencia

**Referencia auditada:** `modern-cybersecurity-program`  
**Corte:** 24 de septiembre de 2026  
**Alcance leído:** 515 archivos Markdown de la referencia y todo el corpus Markdown original de este repositorio.

Esta matriz evita dos errores: omitir un patrón documental útil y copiar una función que no corresponde al contexto de arquitectura.

## Elementos aplicados

| Patrón de la referencia | Implementación en este repositorio | Estado |
|---|---|---|
| Portada visual, badges y accesos principales | README con CI, Pages, clases, rutas, fuentes, idioma y licencias | Aplicado |
| Índice curricular completo | `classes/README.md` con 68 partes | Aplicado |
| Portada de cada parte | 68 README generados desde sus diez clases | Aplicado |
| Conversión Markdown → HTML | 680 clases, 68 partes y documentación en Pages | Aplicado |
| Explicación de origen del material | `docs/PROCEDENCIA_EDITORIAL.md` | Aplicado |
| Bibliografía central trazable | `sources/bibliography.json`: 622 URLs vinculadas con sus clases | Aplicado |
| Fuentes con alcance y límites | sección dedicada en 680/680 clases | Aplicado |
| Cómo usar el programa | guía para perfiles y recorridos | Aplicado |
| Rutas por interés o responsabilidad | 12 rutas y mapa de 80 roles/oficios | Aplicado |
| Estado comprobable y brechas | cobertura exacta, comandos y límites explícitos | Aplicado |
| Licencia separada de código y contenido | Apache-2.0 + CC BY-NC-SA 4.0 | Aplicado |
| Licencias de datos y activos | inventarios dedicados | Aplicado |
| Avisos de terceros | `THIRD_PARTY_NOTICES.md` | Aplicado |
| Contribución, seguridad y ética | `CONTRIBUTING.md`, `SECURITY.md` y guía de ética profesional | Aplicado |
| Política de marcas y auditoría legal | `TRADEMARKS.md` y `LICENSING_AUDIT.md` | Aplicado |
| CI que detecta deriva documental | índices, bibliografía, enlaces, hashes, cobertura y sitio | Aplicado |
| Cierre con estrella, forks, seguimiento y autor | pie visual del README; estrella y licencias en todo Pages | Aplicado |

## Elementos adaptados

| Patrón | Adaptación |
|---|---|
| Laboratorios ejecutables | prácticas documentales y casos dentro de las clases; no se afirma que existan laboratorios de obra |
| Soluciones separadas | soluciones razonadas embebidas cuando existen; cobertura publicada como 650/680 |
| Manual único | lector offline v1.0 y portal HTML; se conserva la fuente Markdown por clase |
| Rutas laborales | rutas temáticas y mapa de responsabilidades, sin prometer empleabilidad ni habilitación |
| Seguridad y ética ofensiva | alcance profesional, seguridad de contenido y límites de actuación en obra y emergencias |

## Elementos no aplicables

| Elemento de ciberseguridad | Razón de exclusión |
|---|---|
| CTF, flags y retos ofensivos | no existe equivalente honesto en este programa |
| Laboratorios Docker de redes, malware o pentesting | ajenos al dominio y a los artefactos disponibles |
| Aplicación Android | el repositorio no contiene una aplicación móvil |
| Certificaciones de ciberseguridad | no corresponden y el programa no es una acreditación |
| Game Security y plataformas de práctica | no forman parte del alcance arquitectónico |
| Advertencias de autorización para atacar sistemas | sustituidas por límites profesionales, normativos y de seguridad del entorno construido |

## Regla de mantenimiento

Un elemento nuevo de la referencia no se copia automáticamente. Se evalúa por su función documental. Si ayuda a explicar, navegar, atribuir, licenciar o verificar este programa, se adapta; si simula una capacidad inexistente, se registra aquí como no aplicable.
