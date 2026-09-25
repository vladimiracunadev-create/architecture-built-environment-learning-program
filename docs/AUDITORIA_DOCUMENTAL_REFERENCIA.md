# Auditoría documental de la referencia

## Alcance

Se leyó el contenido completo de todos los Markdown disponibles en:

- `modern-cybersecurity-program`, commit `fe5c150102bca991fdc0949c407a1f8e00bbbebc`: **515 archivos Markdown**;
- este repositorio antes de la reconstrucción documental: **690 archivos Markdown** —680 clases y 10 documentos o índices.

La inspección recorrió rutas, texto UTF-8, encabezados, enlaces y patrones de cada archivo. No se tomó el README de la referencia como representante de todo el proyecto.

## Qué patrón documental sí aplica

| Patrón de la referencia | Traducción a arquitectura |
|---|---|
| README principal con narrativa y accesos | portada que explica valor, procedencia, fases, uso, rutas, artefactos y límites |
| README por parte | 68 portadas Markdown con preguntas, resultados, clases y navegación |
| anatomía explícita de cada clase | documentar la pauta real de pregunta, resultado, caso, práctica, fuentes y límites |
| procedencia de contenidos | explicar las 611 fichas, 177 dominios y el alcance de una cita |
| rutas por audiencia o rol | presentar 12 recorridos y un mapa de 80 responsabilidades |
| calidad y CI explicados | distinguir qué valida el software y qué requiere revisión profesional |
| documentación auxiliar enlazada | estado, uso, fuentes, rutas, roles, casos y artefactos como documentos de primera clase |
| límites visibles | separar educación, competencia, autorización, normativa y revisión externa |

## Qué no se trasladó

- CTF, exploit labs y soluciones ofensivas;
- mapeo a certificaciones de ciberseguridad;
- aplicación Android;
- secciones legales específicas de hacking autorizado;
- métricas, herramientas o tecnologías que no existen en arquitectura.

Explorar la referencia completa sirve para comprender su estándar documental. No autoriza a copiar superficies ajenas al dominio ni a fingir funcionalidades.

## Diferencia entre las clases

La referencia usa una plantilla casi uniforme en 360 clases: objetivo, resultados, temas, definiciones, herramientas, laboratorio, ejercicios, reto, errores, FAQ y navegación.

Arquitectura tiene otra pauta, adecuada a su contenido: pregunta central, resultado o entrega, caso razonado, práctica, solución o autoevaluación, fuentes con alcance, interfaces y límites. La cobertura no es homogénea en todos los complementos; se publica con cifras exactas en [Estado verificable](ESTADO_VERIFICABLE.md).

## Resultado de la auditoría

La acción correcta no era copiar más secciones al README. Era construir la capa documental que faltaba:

1. índice Markdown general;
2. README narrativo para cada una de las 68 partes;
3. documentación separada de estado, fuentes, uso, rutas, roles y casos;
4. README principal que sintetiza y enlaza, en vez de repetir inventarios;
5. sitio Pages que publique la misma arquitectura documental.

