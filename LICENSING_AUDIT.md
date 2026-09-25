# Auditoría de licenciamiento

**Corte:** 24 de septiembre de 2026  
**Naturaleza:** revisión documental del repositorio; no es asesoría jurídica.

## Resultado ejecutivo

La publicación actual separa las superficies que el repositorio puede licenciar:

- código, scripts, workflows, configuraciones y estilos propios: Apache-2.0;
- clases, documentación y material pedagógico original: CC BY-NC-SA 4.0;
- datos y activos: inventarios específicos;
- referencias, normas y material externo: derechos y términos de sus titulares.

## Evidencia examinada

- 680 clases Markdown y 68 índices de parte;
- scripts, workflows, catálogo y sitio generado;
- lector HTML y PDF de la entrega v1.0;
- 622 URLs externas derivadas de las secciones de fuentes;
- archivos gráficos versionados;
- historial Git disponible y documentos legales de la referencia indicada por el autor.

## Hallazgos y resolución

| Hallazgo | Resolución |
|---|---|
| El repositorio no declaraba licencia | se añadieron `LICENSE` y `LICENSE-CONTENT.md` |
| Código y contenido tenían naturalezas distintas | se separaron Apache-2.0 y CC BY-NC-SA 4.0 |
| Datos, PDF, marca y lector no estaban inventariados | se añadieron `DATA_LICENSES.md` y `ASSET_LICENSES.md` |
| Las referencias podían confundirse con contenido licenciado | se añadieron avisos de terceros y registro central |
| No había política de marcas o respaldo institucional | se añadió `TRADEMARKS.md` |
| Faltaba atribución sugerida | se incorporó en `LICENSE-CONTENT.md` |

## Historial y alcance temporal

Las licencias explícitas se incorporan en esta revisión. Las revisiones anteriores del repositorio no contenían una licencia declarada; este documento no inventa una licencia histórica. La edición actual sí se distribuye con los términos incluidos en sus archivos de licencia.

## Riesgos residuales

- La autoría se apoya en la atribución del repositorio y su historial; no se ejecutó una investigación externa de titularidad.
- Las fuentes externas se enlazan, pero sus términos y vigencia pueden cambiar.
- Los PDF y el lector contienen material generado a partir del programa; cualquier fragmento externo identificado conserva sus derechos.
- No se realizó una opinión legal independiente ni una búsqueda de marcas registradas.

## Validación ejecutada

El validador exige la presencia de licencias, avisos, badges, bibliografía y páginas HTML correspondientes. También verifica enlaces internos, hashes de los artefactos históricos y codificación UTF-8.

## Controles de mantenimiento

1. Registrar licencia y procedencia antes de incorporar un activo o dataset.
2. Enlazar obras externas cuando no exista permiso claro para copiarlas.
3. Regenerar la bibliografía después de modificar fuentes.
4. No cambiar licencias de contenido aportado por terceros sin autorización.
5. Actualizar esta auditoría cuando cambie el régimen de distribución.
