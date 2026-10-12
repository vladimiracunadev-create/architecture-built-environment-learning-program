# PROMPT MAESTRO — Integración de ruta «Construye tu vivienda: de la idea a la recepción definitiva»

**Repositorio objetivo (único):** https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program
**Rama de referencia:** `main` (verificar la rama y el HEAD antes de trabajar).
**País y jurisdicción de los casos:** Chile; las normas aplicables deben revalidarse para la región, comuna, predio, fecha y tipo de intervención.
**Propósito:** integrar educación práctica para un propietario que quiere gestionar la construcción de una vivienda nueva o una ampliación, desde verificar la factibilidad y los permisos hasta ejecutar, presupuestar, controlar, recibir y mantener la obra.
**Naturaleza del encargo:** AMPLIAR el repositorio existente, no crear otro proyecto, no sustituir el programa integral y no modificar nada fuera de este repositorio.

## 0. MANDATO PRINCIPAL

Actúa como un equipo coordinado de:
- arquitecto/a proyectista y coordinador/a;
- especialista en urbanismo, normativa chilena y tramitación municipal;
- ingeniero/a estructural y especialista en geotecnia;
- constructor/a civil o ingeniero/a constructor/a;
- calculista de cubicaciones, analista de precios unitarios y presupuestista;
- planificador/a y administrador/a de contratos y obras;
- prevencionista de riesgos y encargado/a de calidad;
- especialista en instalaciones sanitarias, eléctricas, gas y eficiencia térmica;
- docente de adultos principiantes y diseñador/a instruccional;
- editor/a técnico/a de Markdown, JSON, generadores Python y validación de repositorios;
- auditor/a de fuentes e IA, con obligación de reconocer incertidumbres.

**Advertencia fundamental:** estas son perspectivas para escribir y revisar contenido educativo, NO atribuciones profesionales otorgadas al lector ni sustitutos de firmas, cálculos, dirección, autorizaciones o inspecciones exigidas por la ley. Enseña al propietario a entender, organizar, contratar, verificar y preguntar. Distingue rigurosamente tareas didácticas y tareas que exigen persona legalmente habilitada. Nunca entregues instrucciones operativas peligrosas como si bastara leer una clase para excavar, intervenir muros portantes, subir un segundo piso, trabajar en altura, instalar electricidad o gas, o conectar estructuras existentes.

**Regla de trabajo:** `INSPECCIONAR → CLASIFICAR → REUTILIZAR → AMPLIAR → RELACIONAR → CREAR SOLO LO FALTANTE → VALIDAR → INFORMAR`.

No alegues haber auditado, validado, consultado fuentes o ejecutado herramientas si no lo hiciste. No publiques cambios sin mostrar y revisar su alcance. No cambies la licencia existente sin autorización.

## 1. AUDITORÍA OBLIGATORIA DEL REPOSITORIO REAL

Antes de crear una clase, inspecciona en `main` los archivos reales:
- `README.md`, `ROADMAP_INTEGRAL.md`, `CONTRIBUTING.md`;
- `docs/ARQUITECTURA_DEL_REPOSITORIO.md`;
- `docs/ESTANDAR_DOCUMENTACION_CLASE.md`, `docs/ESTANDAR_DE_FUENTES.md`;
- `docs/ROLES_Y_OFICIOS.md`, `docs/NORMATIVE_BOUNDARY.md`;
- `docs/RUTAS_DE_APRENDIZAJE.md`, `docs/ESTADO_VERIFICABLE.md`;
- `docs/MATRIZ_COBERTURA_INTEGRAL.md`, `docs/MAPA_DE_DEPENDENCIAS.md`;
- `data/program.json`, `data/parts.json`, `data/catalog.json`, `data/pedagogy.json`;
- `classes/README.md`, `studios/README.md`, `learning-paths/`;
- `scripts/` y `.github/workflows/`, especialmente generadores, auditorías y validador;
- `sources/` y los instrumentos en `templates/` y `evidence/`.

Audita concretamente las clases ya existentes **ARQ-141–150, ARQ-181–210, ARQ-301–330, ARQ-381–440 y ARQ-481–490**, sin omitir otras clases relevantes descubiertas por búsqueda. En particular, comprueba:
- `ARQ-144`, `ARQ-149`, `ARQ-381–390`, `ARQ-393–395`, `ARQ-401–410`;
- `ARQ-411–420` (factibilidad, cubicación, APU, costos y caja);
- `ARQ-421–430` (programación, calidad y cierre);
- `ARQ-481`, `ARQ-485`, `ARQ-489`, `ARQ-490`.

**Línea base vista el 10-10-2026 (VOLVER A VERIFICAR):** 800 clases `ARQ-001–800`; 80 partes de 10 clases; 33 rutas; 10 talleres y 60 sesiones; contenido canónico en `classes/`, `data/`; documentación e índices parcialmente generados; archivos `v1.0` e `INDICE_680_CLASES_v1.0.md` históricos e intocables como fotografías editoriales.

Produce primero una matriz con columnas:
`necesidad del propietario | tema preexistente | rutas/IDs consultados | cobertura (YA EXISTE / PARCIAL / FALTA / NO CORRESPONDE) | reutilizar o nuevo | evidencia | justificación`.

La propuesta de 30 clases de este documento es una **meta inicial condicionada a la auditoría**. No dupliques por cumplir un número. Si algo ya existe a profundidad suficiente, referencia la clase actual y sustituye el espacio redundante por una necesidad real o reduce el crecimiento de manera documentada. Conserva las IDs históricas.

## 2. RESULTADO DIDÁCTICO Y PÚBLICO

Diseña una ruta autónoma y accesible desde conocimientos cero, titulada:

**«Construye tu vivienda: de la idea a la recepción definitiva»**.

Al finalizar, un propietario debe poder:
1. Evaluar si es viable construir, ampliar o postergar una obra.
2. Entender el terreno, sus restricciones, los antecedentes de su vivienda y los riesgos.
3. Identificar el procedimiento municipal correcto, sus documentos, costos y estados.
4. Seleccionar profesionales, entender planos y comparar alternativas constructivas.
5. Cubicar, presupuestar y comprobar precios reales sin confundir el dato comercial con un cálculo ficticio.
6. Preparar contratos, pagos, adquisiciones, cronograma y reserva de contingencias.
7. Comprender la secuencia de la construcción y reconocer puntos de inspección, interferencias y decisiones críticas.
8. Diferenciar trabajos apropiados para participación del propietario de tareas restringidas o peligrosas.
9. Controlar cambios, calidad, seguridad, atrasos y desviaciones económicas.
10. Tramitar el cierre, los certificados aplicables, la recepción definitiva y un plan de mantenimiento.

Mantén dos expedientes paralelos y COMPLETOS, sin tratarlos como un mismo permiso o costo:
- **Caso CASA-NUEVA-80:** casa nueva de 80 m², terreno hipotético urbanizado, nivel de terminación medio, localidad y comuna declaradas expresamente como supuestos a verificar.
- **Caso AMPLIACION-24:** ampliación de 24 m² de una vivienda existente, un nivel, con ejemplo alternativo de segundo piso que se aborda solo como evaluación de factibilidad profesional y NO como instrucciones de refuerzo estructural.

Cada caso deberá contar con al menos 3 escenarios: **económico, estándar y mayor desempeño**, con mismos alcances comparables o diferencias declaradas. Incorporar una variante de contingencia y sensibilidad de 10 % a 20 % como hipótesis didáctica; nunca presentarla como tarifa obligatoria universal.

## 3. PROPUESTA DE CLASES NUEVAS — TRES PARTES DE DIEZ

Crear las partes **81–83**, IDs **ARQ-801–830**, solo si están libres y el diagnóstico confirma la ampliación. Preservar correspondencia parte/ID en los archivos fuente y catálogos.

### PARTE 81 — Antes de construir: decisión, terreno, legalidad y permisos

| ID | Clase práctica | Entregable verificable |
|---|---|---|
| ARQ-801 | ¿Construir, ampliar, reparar o comprar? Definir objetivo, alcance y límite económico | Ficha de decisión y necesidades, lista de alternativas |
| ARQ-802 | Documentos del terreno y de la vivienda: dominio, rol, planos, permisos y recepciones existentes | Carpeta de antecedentes y faltantes |
| ARQ-803 | Certificado de Informaciones Previas (CIP), plan regulador y restricciones | Ficha normativa específica de un predio hipotético |
| ARQ-804 | Estado actual: levantamiento, patologías, muros y elementos estructurales que NO deben intervenirse sin diagnóstico | Plano «existente / propuesto» y matriz de riesgos |
| ARQ-805 | Servicios, suelo, topografía, amenazas, entorno, colindancias y acceso de maquinaria | Informe de factibilidad y especialistas necesarios |
| ARQ-806 | Programa de recintos: superficie, habitabilidad, ventilación, accesibilidad, crecimiento y alternativas | Cuadro de superficies, bocetos y criterios de selección |
| ARQ-807 | Árbol de decisiones de trámites: obra nueva, obra menor, ampliación, alteración, obra rural, copropiedad, exenciones y regularización | Árbol de decisión con autoridad, formulario y condiciones |
| ARQ-808 | A quién contratar y cuándo: arquitecto, calculista, constructor, instalaciones, ITO cuando corresponda, asesores y DOM | Matriz RACI de responsabilidades, firmas y costos profesionales |
| ARQ-809 | Presupuesto preliminar y financiación: costo por m² como referencia limitada, costos ocultos y viabilidad | Estimación de orden de magnitud con fuentes y escenarios |
| ARQ-810 | Primera puerta de control: decidir si iniciar el proyecto | Dossier `GO / REDISEÑAR / DETENER` y checklist de legalidad, técnica y financiamiento |

### PARTE 82 — Proyecto, presupuesto detallado, compras y autorización

| ID | Clase práctica | Entregable verificable |
|---|---|---|
| ARQ-811 | Levantamiento con medidas, cotas, deslindes, superficies y fotografías sin invadir atribuciones técnicas | Plano base y registro de incertidumbres |
| ARQ-812 | Leer plantas, cortes, elevaciones, emplazamiento, detalles, escalas y especificaciones técnicas | Set de planos didácticos comentados |
| ARQ-813 | Coordinación de suelo, fundaciones, estructura y sismo; diferencias de casa nueva y ampliación; responsabilidad del calculista | Matriz de entregables y puntos de revisión profesional |
| ARQ-814 | Cubierta y envolvente: aguas lluvias, impermeabilización, ventanas, condensación y exigencias térmicas vigentes | Detalles conceptuales revisables y lista de compatibilidades |
| ARQ-815 | Redes de agua, alcantarillado, electricidad y gas; factibilidades, profesionales y declaraciones que correspondan | Matriz de redes, autorizaciones, puntos de inspección y certificados |
| ARQ-816 | Cubicaciones reales: unidades, pérdidas, materiales, transporte y rendimientos; diferencia entre metrados y compras | Hoja de cantidades auditables con incertidumbres |
| ARQ-817 | Análisis de precios unitarios (APU), presupuesto completo, IVA, gastos generales, honorarios, permisos y contingencias | Presupuesto detallado y comparativo en CLP y UF cuando corresponda |
| ARQ-818 | Expediente de permiso: documentos, ingreso y seguimiento ante DOM, observaciones y cambios | Checklist de presentación y seguimiento de estado real/simulado |
| ARQ-819 | Cotizaciones, contratos, subcontratistas, seguros, garantías, pagos, actas y resolución de conflictos | Matriz comparativa de 3 ofertas y modelo contractual comentado |
| ARQ-820 | Cronograma, compras, ruta crítica y autorización para iniciar: coordinación con vecinos y exigencias de seguridad | Línea base costo/plazo y segunda puerta `NO INICIAR SIN HABILITACIONES APLICABLES` |

### PARTE 83 — Construcción, control de gastos, recepción y mantenimiento

| ID | Clase práctica | Entregable verificable |
|---|---|---|
| ARQ-821 | Instalación de faenas: protección de lo existente, seguridad, cierres, vecinos, accesos y acopios | Checklist de preinicio y roles responsables |
| ARQ-822 | Movimiento de tierra, excavaciones, fundaciones, humedad del suelo y puntos de inspección | Secuencia conceptual e hitos de revisión técnica; nunca instrucciones inseguras |
| ARQ-823 | Obra gruesa: estructura, muros, anclajes, cubierta, conexión segura con edificación existente | Diagrama de dependencias y protocolo de aceptación por especialista |
| ARQ-824 | Envolvente: techumbre, aislación, impermeabilización, vanos, puentes térmicos y escurrimientos | Ficha de inspección y pruebas exigibles según proyecto |
| ARQ-825 | Instalaciones empotradas y visibles, interferencias, pruebas y certificados aplicables | Plan de coordinación y actas de prueba por responsables autorizados |
| ARQ-826 | Terminaciones: revestimientos, pisos, carpinterías, baños, cocina, accesibilidad y mantenimiento | Lista de tolerancias, muestras y recepción de partidas |
| ARQ-827 | Control del presupuesto durante la obra: avance físico, pagos, compras, saldos, cambios, IVA y flujo de caja | Libro de costos con curvas previsto/real y proyección a término |
| ARQ-828 | Seguridad, residuos, ruido, inspecciones, fallas, calidad y trato con la comunidad | Registro de no conformidades, medidas y responsables |
| ARQ-829 | Qué hacer si hay atrasos, sobrecostos o descubrimientos imprevistos; órdenes de cambio y nuevas aprobaciones | Tres incidentes resueltos con trazabilidad y presupuesto revisado |
| ARQ-830 | Término de obra, certificados SEC cuando correspondan, solicitud y obtención de recepción definitiva DOM, garantías, mantención | Carpeta de cierre, manual de mantenimiento y comparación final de ambos casos |

Cada clase debe tener un **apartado de aplicación al caso CASA-NUEVA-80 y otro al caso AMPLIACION-24**, explicitando qué parte se transfiere y qué cambia. En especial, el caso de ampliación debe analizar:
- construcción adosada y compatibilidad de estructuras;
- diferencias entre ampliación de un nivel y segundo piso;
- necesidad de diagnóstico estructural del inmueble existente;
- protección de instalaciones y ocupantes durante las obras;
- cubierta, encuentros, medianeros, humedad y evacuación de aguas;
- uso de permisos y recepciones históricas; no asumir legalidad porque la construcción ya existe;
- tratamiento de espacios existentes que se convierten en cocina, baño o dormitorio;
- costos de demolición selectiva, refuerzos, reubicación temporal, polvo, cortes de suministro y recuperación de terminaciones;
- casos rural, zona de riesgo, patrimonio y copropiedad como bifurcaciones, sin simular que todos tienen un mismo procedimiento.

## 4. RUTA DE APRENDIZAJE Y DISEÑO PEDAGÓGICO

Proponer **RUTA-34: Vivienda propia y ampliación para propietarios** si la numeración sigue libre. La ruta debe:
- comenzar con diagnóstico de alfabetización técnica, lectura de planos, unidades, porcentajes y seguridad;
- seleccionar como prerrequisitos clases actuales en vez de copiarlas;
- incluir `ARQ-801–830` en orden, con nivelación en partes 03, 11, 15, 19–21, 27–28, 31–35, 39–43 y 49 cuando sea necesario;
- incluir dos proyectos de extremo a extremo, diagnóstico, al menos dos checkpoints formales, crítica y recuperación;
- vincular un taller existente pertinente si cubre el objetivo; **no inventar un EST-11** solo para incrementar números. Crear un nuevo taller de seis sesiones únicamente si una brecha comprobada lo justifica y se actualizan manifiestos/generadores;
- ofrecer la ruta del propietario de forma visible en el README principal, `docs/RUTAS_DE_APRENDIZAJE.md`, índices y web generada;
- declarar qué actividades son de simulación, cuáles puede realizar un propietario y cuáles requieren profesional habilitado.

**Estructura de clase:** respetar `docs/ESTANDAR_DOCUMENTACION_CLASE.md`. Cada Markdown completo debe incluir pregunta, problema, resultado observable, prerrequisitos reales, explicación desarrollada, lectura de antecedentes, fuentes, esquema útil, caso numérico cuando proceda, práctica guiada, ejercicio independiente, errores típicos, evaluación por evidencias, recuperación, checklist, criterio de aprobación y continuidad. No basta con título + ocho viñetas. Usar español claro, con definiciones de jerga; nunca ocultar una decisión legal o constructiva esencial detrás de una abreviatura.

Añadir recursos ilustrativos originales y accesibles cuando aporten valor: plano de emplazamiento, planta acotada, corte, elevación, esquema de intersección de cubierta, cronograma Gantt, flujo DOM, secuencia de obra, diagrama de permisos, comparador de contratos y curva de flujo de caja. No presentar un dibujo ficticio como plano ejecutivo apto para obra.

## 5. LEGISLACIÓN Y PERMISOS: REQUISITO BLOQUEANTE

Este bloque debe estar sustentado en **norma vigente consultada al momento de la implementación**, con artículo, organismo, jurisdicción, fecha, enlace, contexto y límite de aplicación. Consultar primero fuentes oficiales:
- **LGUC** en Biblioteca del Congreso Nacional: https://www.bcn.cl/leychile/navegar?idNorma=13560
- **OGUC, DS 47** en BCN: https://www.bcn.cl/leychile/navegar?idNorma=8201
- **Formularios nacionales DOM**: https://www.minvu.gob.cl/elementos-tecnicos/formularios-de-tramites-direcciones-de-obras-municipales-dom/
- **Certificados/CIP**: https://www.minvu.gob.cl/elementos-tecnicos/formularios/0-certificados-y-otros/
- **Obra menor y ampliación hasta 100 m²**: https://www.minvu.gob.cl/elementos-tecnicos/formularios/formularios-de-permisos-de-obra-menor/
- **Obra nueva y ampliación mayor a 100 m²**: https://www.minvu.gob.cl/elementos-tecnicos/formularios/formularios-de-permisos-de-edificacion/
- **DOM en Línea y cobertura comunal**: https://www.minvu.gob.cl/dom-en-linea/
- **SEC e-Declarador, TE1/TC6**: https://www.sec.cl/e-declarador/
- **Nueva reglamentación térmica**: https://www.minvu.gob.cl/nueva-reglamentacion-termica/

Investigar expresamente: título o antecedente de dominio, rol y ubicación, CIP, usos de suelo, límites de predio, ocupación y constructibilidad, distanciamientos/rasantes/adosamientos, altura y exigencias según destino; urbanización y factibilidad sanitaria/eléctrica, accesos, zonas de protección y riesgo, ruralidad y normativa específica; casa nueva, ampliación de hasta 100 m², mayor a 100 m², alteración y ampliación de vivienda social; mecanismos de permiso o declaración jurada aplicables, exenciones, regularización cuando proceda y recepción definitiva. No asumas que una ampliación pequeña esté libre de tramitación: una clasificación depende de condiciones y normativa. No confundir régimen especial con regularización general ni legalizar retrospectivamente por defecto.

**Regla de seguridad jurídica:** la LGUC/OGUC define el marco, pero el expediente depende también del predio, comuna, instrumento de planificación, vigencia, características de la obra y actuación de la DOM. Donde las reglas hayan cambiado, contrastar textos vigentes y disposiciones transitorias. Distinguir claramente `REQUISITO CONFIRMADO`, `VERIFICAR EN DOM / ESPECIALISTA` y `SUPUESTO DIDÁCTICO`. No entregar formulario supuestamente completado por una autoridad ni garantizar aprobaciones.

Incluir **matriz de costos de tramitación**: certificados, estudios, honorarios, derechos municipales, permisos y modificaciones, informes, certificados especializados, copias, notariales/registro si proceden y recepción. Comprobar el texto vigente del **artículo 130 LGUC**: referencia general para obra nueva y ampliación del **1,5 % del presupuesto**; **no** extenderlo mecánicamente a toda categoría ni ignorar exenciones, descuentos, definición del presupuesto, regímenes especiales o cobros adicionales. Documentar un ejemplo con una base ficticia y su resultado, sin presentarlo como liquidación municipal válida.

Explicar declaraciones **TE1** de electricidad y **TC6** de gas cuando correspondan, por profesionales autorizados. Verificar asimismo procedimientos de agua y alcantarillado, factibilidades, recepción y reglamentación térmica según zona, proyecto y fecha. El propietario no declara por su cuenta instalaciones reservadas.

## 6. COSTOS: SISTEMA DE PRESUPUESTACIÓN REALMENTE UTILIZABLE

Los costos NO son una clase decorativa. Deben atravesar los dos casos, desde ARQ-801 hasta ARQ-830. Construir **cuatro niveles de estimación**:

**Nivel A — orden de magnitud:** costo de referencia por m² y sus exclusiones, solo para evaluar viabilidad, nunca presupuesto de ejecución.

**Nivel B — estimación por capítulos:** movimiento de tierras; cimientos/fundaciones; estructura; muros; cubiertas; puertas y ventanas; aislación; impermeabilización; electricidad; gas; agua y alcantarillado; revestimientos; terminaciones; equipamiento; obras exteriores; provisionales; limpieza, retiro y disposición; fletes; y, para ampliación, intervención de lo existente.

**Nivel C — presupuesto ejecutivo con APU:** `cantidad × precio unitario`, desglose de materiales, mermas justificadas, mano de obra, rendimientos, equipos, transporte, subcontratos, gastos generales, utilidad de contratista cuando proceda, impuestos, honorarios profesionales, inspecciones, trámites, riesgos y contingencia. Asegurar que IVA, gastos generales, utilidad, descuentos y fondos de reserva no se dupliquen o se apliquen sobre bases incompatibles.

**Nivel D — control de obra:** presupuesto aprobado, comprometido, contratado, devengado, pagado, avance físico, estimación a término, variaciones de alcance, reajustes y saldo disponible. Mostrar costos reales y estimados separados.

### Estructura obligatoria de presupuesto

Cada ítem debe contener al menos:
`codigo, caso, etapa, partida, subpartida, descripción, especificación, unidad, cantidad, merma, precio_unitario_neto_CLP, subtotal_neto_CLP, IVA_aplicable, total_CLP, proveedor, comuna, región, fecha_cotización, vigencia, URL_o_fuente, observaciones, nivel_confianza, estado_del_gasto`.

Separar tablas para:
1. **Costos del terreno y habilitación**, solo cuando correspondan.
2. **Estudios, arquitectura, ingeniería y especialistas**.
3. **Derechos, certificados y tramitación**.
4. **Construcción**, con APU por partida.
5. **Mano de obra y obligaciones laborales/seguros** según modalidad de contratación.
6. **Equipamiento, instalaciones y certificaciones**.
7. **Contingencias, reajustes, imprevistos y exposición a precios**.
8. **Operación y mantenimiento** después de entrega.
9. **Financiación, intereses y desfases de caja**, si el caso lo necesita.

Calcular:
- costo total sin terreno / con terreno, con sus componentes diferenciados;
- costo directo versus total del proyecto;
- costo/m² y criterio explícito del denominador (útil, construida o intervenida);
- materiales versus mano de obra versus administración y profesionales;
- flujo mensual y caja máxima requerida;
- costo contratado, ejecutado, pagado y proyectado a término;
- impacto de retrasos, aumento de insumos y cambios;
- sensibilidad del ±10 %, ±15 % y ±20 % para variables elegidas;
- tres escenarios de calidad y dos métodos de contratación (general y partidas separadas);
- comparación de los dos proyectos, sin asumir que la ampliación cueste lo mismo por m² que una casa nueva.

### Protocolo de precios

1. Para afirmar «precio vigente», presentar **fuente accesible y cotización fechada**, ubicación, unidad, calidad/especificación, IVA, transporte, plazo y stock si está disponible.
2. Comparar **al menos tres cotizaciones** equivalentes por partida o reconocer explícitamente que no están disponibles.
3. CLP es la moneda de registro. Mostrar UF únicamente con **fecha de valor y fuente oficial**, sin usar equivalencia fija eterna.
4. No inventar precios de 2026. Si no es posible consultar precios reales, usar valores **marcados como HIPOTÉTICOS** y un formulario editable para que el estudiante complete las cotizaciones locales.
5. Separar precio de catálogo, precio cotizado, pagado y estimado.
6. Proporcionar costos de materiales, transporte, mano de obra y rendimientos con incertidumbre; las tarifas cambian por región (p. ej., Arica versus Santiago), accesibilidad, temporada y estándar.
7. Los costos de permisos y honorarios son variables, no porcentajes universales inventados.
8. Agregar partidas olvidadas con frecuencia: limpieza, nivelación, escombros, ensayos, cortes y reconexión de servicios, acopio, seguridad, retiro temporal de ocupantes, humedades y reparación de áreas afectadas.
9. Registrar un **escenario de detención** cuando el costo supera financiamiento disponible o una condición legal/técnica no está resuelta.

### Herramientas y archivos prácticos

Integrar sin romper el entorno existente:
- `templates/presupuesto-vivienda.csv` y `templates/presupuesto-ampliacion.csv` o nomenclatura coherente;
- una plantilla de hoja de cálculo **.xlsx** editable con fórmulas de subtotal, IVA, contingencia, flujo y diferencias, si las herramientas del proyecto permiten generar y validar dicho archivo;
- `docs/GUIA_PRESUPUESTO_VIVIENDA.md` explicando cada campo y sus errores;
- casos trabajados con **supuestos didácticos y cálculos reproducibles**;
- pruebas automatizadas de sumas, unidades, IVA, duplicados, cantidades negativas, conversiones y límites de sensibilidad cuando se creen scripts de cálculo.

Usar Python compatible con el repositorio; si se introduce gestión nueva del entorno, priorizar `uv`, sin exigir `npm` ni migrar a una plataforma JavaScript. No instalar dependencias nuevas sin justificación.

## 7. DOS EXPEDIENTES TERMINADOS Y REUTILIZABLES

Crear fichas educativas, hojas y evidencias en rutas coherentes con el árbol REAL (elegir ubicación después de auditar; no imponer una carpeta inexistente como si ya fuera canónica).

### Expediente A — Vivienda nueva de 80 m²
Debe contener: encargo familiar, ficha de terreno ficticio, CIP simulado claramente marcado, matriz de restricciones, análisis de suelo/servicios como necesidades de estudio, cuadro de superficies, planos didácticos, alternativas, especificaciones, alcance, proyecto de redes a coordinar, lista de profesionales, permisos aplicables, cubicación y presupuesto por 3 escenarios, cronograma, compras, control de obra, carpeta de cierre y mantenimiento.

### Expediente B — Ampliación de 24 m²
Debe contener: antecedentes de edificación existente, diagnóstico de permiso/recepción anterior, levantamiento «antes y después», riesgos de estructura existente y techumbre, encuentro de instalaciones, permisos y profesionales exigibles, presupuesto con partidas propias de intervención, protección de residentes y vecinos, plan de continuidad de servicios, inspecciones, cambios, recepción y mantenimiento.

Cada uno será un «hilo conductor»: documentos de una clase alimentan la clase siguiente y se corrigen cuando cambian las hipótesis. El lector debe poder reconstruir el costo, la decisión y el documento habilitante en cualquier etapa.

## 8. RESPONSABILIDADES, SEGURIDAD Y AUTOCONSTRUCCIÓN

Usa el mapa existente `docs/ROLES_Y_OFICIOS.md` y sus fichas como fuente antes de crear perfiles adicionales. Incorporar una matriz para el lector con columnas:
`tarea | propietario puede aprender/gestionar | puede ejecutar solo si procede | requiere especialista/profesional habilitado | permiso/inspección | evidencia`.

Señalar como **fronteras críticas**:
- inspección, modificación o demolición de elementos estructurales;
- excavaciones, taludes, estabilidad de medianeros, fundaciones y apuntalamientos;
- obras en altura, techumbres, andamios y trabajos eléctricos;
- instalaciones y conexiones de electricidad, gas y otros sistemas regulados;
- ampliaciones en segundo piso y sobrecargas sobre vivienda existente;
- seguridad frente a incendios, sismo, humedad, ventilación y salubridad;
- derechos de vecinos y colindantes, residuos, ruidos, polvo y ocupación de espacios públicos.

No confundir «autoconstrucción» con «obra sin profesionales». Ofrecer escenarios de autogestión del proyecto, trabajo propio permitido, contratación por partidas y contratista general. Para cada modalidad, describir riesgos, costos de supervisión, garantía, coordinación y responsabilidad. No recomendar ejecutar una etapa riesgosa a partir de instrucciones pedagógicas.

## 9. IA: APOYO PERMITIDO, NO SUSTITUTO DE INGENIERÍA

Como extensión transversal, enseñar a usar IA para:
- convertir un programa familiar en checklist de necesidades;
- detectar omisiones documentales de un expediente;
- explicar vocabulario de planos y contratos;
- ayudar a organizar una cubicación sujeta a revisión;
- comparar cotizaciones equivalentes y clasificar exclusiones;
- redactar preguntas a DOM/profesionales sin simular respuestas oficiales;
- generar cronogramas tentativos, listas de compras y controles de caja;
- revisar inconsistencias entre versiones del presupuesto;
- elaborar actas de avances y lista de defectos.

Obligar a validar números, unidades, supuestos y citas con fuentes independientes. Prohibir presentar dimensionamientos estructurales, autorizaciones, criterios de seguridad o certificaciones producidas por IA como aptas para ejecución sin profesional competente.

## 10. IMPLEMENTACIÓN COMPATIBLE CON EL REPOSITORIO

1. Crear una rama específica; no sobreescribir directamente artefactos históricos.
2. Modificar primero **fuentes canónicas**: `data/program.json`, `data/parts.json`, `data/catalog.json` y `data/pedagogy.json` únicamente en los campos validados que correspondan.
3. Si se implementan las 30 clases, revisar la consistencia de conteos propuestos: **830 clases, 83 partes, 34 rutas**; mantener inicialmente **10 talleres y 60 sesiones** si se reutilizan los existentes. Actualizar fases sin reescribir la historia editorial.
4. Crear los contenidos `classes/parte-81/ARQ-801.md` a `classes/parte-83/ARQ-830.md`, respetando la organización de 10 clases/parte.
5. Registrar y enlazar **RUTA-34** en las estructuras canónicas y las salidas derivadas; no limitarse a crear un Markdown aislado.
6. Documentar los dos casos y las plantillas de costos con trazabilidad a clases.
7. Integrar descubribilidad en `README.md`, índice de clases, mapa de dependencias, matriz de cobertura, guía de uso, roles, fuentes y sitio.
8. **No editar manualmente archivos generados** si existe un generador. Examinar los scripts y ejecutar en el orden indicado por `docs/ARQUITECTURA_DEL_REPOSITORIO.md`.
9. Actualizar fechas/cifras en documentación vigente **sin tocar** PDFs, índices, HTML histórico, `STATUS_v1.0.json` ni hashes históricos salvo que la auditoría demuestre y justifique otra necesidad y exista autorización expresa.
10. Conservar las licencias reales: código bajo la licencia existente **Apache-2.0** y contenido educativo bajo **CC BY-NC-SA 4.0**, tal como lo presenta el README verificado; no relicenciar a MIT por inercia. Respetar licencias de imágenes, tablas y datos externos.
11. Validar construcción del sitio y enlaces internos, UTF-8, navegación móvil y acceso a tablas grandes y plantillas.
12. No alterar clases antiguas salvo correcciones comprobadas indispensables para enlaces/dependencias; conservar IDs y enlaces estables.

### Comprobaciones mínimas

Antes de confirmar integración:
- Verificar consecutividad de IDs, que cada parte tenga exactamente 10 clases y que no haya títulos duplicados.
- Ejecutar el conjunto de validaciones realmente definido en `.github/workflows/ci.yml` y `docs/ESTADO_VERIFICABLE.md`. Entre los scripts presentes a revisar: `scripts/validate_repo.py`, `scripts/audit_class_distinctness.py`, `scripts/audit_pedagogical_traceability.py`, `scripts/build_bibliography.py`, `scripts/build_pedagogical_decisions.py`, `scripts/apply_pedagogy.py`, `scripts/generate_curriculum_docs.py`, `scripts/build_site.py`.
- Revisar las diferencias para detectar modificaciones ajenas.
- Verificar que las nuevas fuentes legales tengan jurisdicción, artículo/numeral y fecha de consulta, sin referencias ficticias.
- Validar todas las fórmulas del presupuesto con al menos 5 pruebas numéricas independientes, incluyendo IVA 0/no aplicable, cambios de alcance, presupuesto insuficiente, mermas y diferencias de fecha de precio.
- Comprobar que dos alumnos con el mismo caso y cotizaciones obtengan el mismo subtotal y sepan distinguir incertidumbre.
- Confirmar que las 30 clases no sean resúmenes repetitivos ni transcripciones de contenido existente.
- Las nuevas afirmaciones de seguridad y norma tienen que pasar una revisión profesional externa antes de tratarse como orientación para una obra real. Si no existe, etiquetar como pendiente, no como validado.

## 11. CRITERIOS DE ACEPTACIÓN DEL PRODUCTO

La ampliación solo se considera terminada cuando:

- **A. Aprendizaje:** una persona principiante puede explicar, en orden, qué documentación revisar, qué permisos tramitar, qué profesionales contratar, cuándo pagar y cuáles son las decisiones que jamás debe improvisar.
- **B. Casos:** CASA-NUEVA-80 y AMPLIACION-24 poseen expedientes recorribles desde el primer diagnóstico hasta la recepción/mantenimiento, con «estado de hipótesis» visible.
- **C. Legal:** ninguna clase promete exenciones, aprobación o recepción automática; cada procedimiento tiene fuente legal y condición de aplicabilidad.
- **D. Costos:** existe presupuesto auditable por partidas y APU, escenarios, IVA tratado correctamente, fecha/fuente de precios, imprevistos y flujo de caja.
- **E. Seguridad:** el propietario reconoce claramente cuándo NO ejecutar por sí mismo y qué especialista necesita.
- **F. Integración:** todas las nuevas clases/rutas/casos aparecen en navegación, catálogos y sitio, sin romper la malla de 800 clases heredada.
- **G. Calidad:** las pruebas automatizadas pasan; lo no verificado queda declarado.
- **H. Fuentes:** cada dato regulatorio o precio usado tiene origen, unidad, fecha y alcance; fuentes faltantes quedan `PENDIENTE`, no se inventan.
- **I. Derechos:** ninguna licencia ni obra protegida se utiliza de modo incompatible.
- **J. Auditoría final:** existen resumen de cambios y lista de riesgos remanentes, incluyendo qué requiere revisión por profesionales chilenos.

## 12. FORMATO DE RESPUESTA Y ENTREGABLES DEL AGENTE

Entrega obligatoriamente y en ese orden:

1. **Auditoría inicial** del repositorio real, fecha/HEAD, inventario relevante y matriz `YA EXISTE / PARCIAL / FALTA / NO CORRESPONDE`.
2. **Decisión de alcance**, justificando exactamente cuántas clases nuevas son imprescindibles después de la auditoría; objetivo inicial 30, sin forzar duplicados.
3. **Mapa de integración** que indique IDs, clases antiguas reutilizadas, rutas, prerrequisitos, estudios de caso y salidas generadas.
4. **Material completo** de clases, ejercicios, diagramas, plantillas, casos y ruta de aprendizaje, sin marcadores `TODO` disfrazados de implementación.
5. **Presupuestos** verificables en CLP y fechas de fuentes, con versiones separadas de valores ficticios y cotizaciones reales disponibles.
6. **Matriz de permisos** con organismo, procedimiento, documentos, responsable, condición de aplicabilidad, costo cuando sea verificable y enlace oficial.
7. **Informe de seguridad y límites** para propietario versus especialistas.
8. **Reporte técnico** de archivos añadidos/modificados, comandos realmente ejecutados, resultados de validación, advertencias y próximos pasos.
9. **Cambios listos para una PR**, sin hacer merge ni publicar sin permiso explícito del dueño.

**Instrucción final:** no necesitas preguntarme cuál es el repositorio, si deseas conservarlo o si se deben incluir costos: ya está especificado. Trabaja solo sobre el repositorio indicado, evalúa la estructura real, reutiliza lo existente, añade contenido didáctico profundo y termina con una ruta práctica que lleve al propietario de la factibilidad al presupuesto, la construcción controlada y la recepción definitiva, sin invadir funciones profesionales.

---

## Fuentes iniciales para verificar, no sustitutos de la consulta actualizada

- Repositorio: https://github.com/vladimiracunadev-create/architecture-built-environment-learning-program
- LGUC: https://www.bcn.cl/leychile/navegar?idNorma=13560
- OGUC: https://www.bcn.cl/leychile/navegar?idNorma=8201
- Formularios DOM: https://www.minvu.gob.cl/elementos-tecnicos/formularios-de-tramites-direcciones-de-obras-municipales-dom/
- Certificados y CIP: https://www.minvu.gob.cl/elementos-tecnicos/formularios/0-certificados-y-otros/
- Formularios obra menor: https://www.minvu.gob.cl/elementos-tecnicos/formularios/formularios-de-permisos-de-obra-menor/
- Formularios obra nueva: https://www.minvu.gob.cl/elementos-tecnicos/formularios/formularios-de-permisos-de-edificacion/
- DOM en Línea: https://www.minvu.gob.cl/dom-en-linea/
- SEC e-declarador: https://www.sec.cl/e-declarador/
- Reglamentación térmica: https://www.minvu.gob.cl/nueva-reglamentacion-termica/
