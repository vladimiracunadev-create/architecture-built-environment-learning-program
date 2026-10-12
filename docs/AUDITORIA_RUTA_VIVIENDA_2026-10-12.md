# Auditoría e integración de la ruta para propietarios

**Fecha:** 12 de octubre de 2026
**Rama y HEAD inicial verificados:** `main` · `f5ad0df0d3e020af3d05c16fecd6cd4cd841c651` · sincronizado con `origin/main` antes de editar.
**Línea base:** 800 clases ARQ-001–800, 80 partes, 33 rutas, 10 talleres y 60 sesiones.

## 1. Auditoría inicial

Se inspeccionaron las fuentes canónicas, estándares, generadores, CI, plantillas y los rangos ARQ-141–150, ARQ-181–210, ARQ-301–330, ARQ-381–440 y ARQ-481–490. Se revisaron especialmente ARQ-144, ARQ-149, ARQ-381–390, ARQ-393–395, ARQ-401–430, ARQ-481, ARQ-485, ARQ-489 y ARQ-490.

| Necesidad del propietario | Tema preexistente | Rutas/IDs consultados | Cobertura | Reutilizar o nuevo | Evidencia | Justificación |
|---|---|---|---|---|---|---|
| Decidir construir, ampliar, reparar o comprar | encargo, vivienda, asequibilidad y factibilidad | ARQ-031, 111, 141–150, 411, RUTA-12, RUTA-15 | PARCIAL | nuevo ARQ-801 y 809–810 | ficha y puerta GO / REDISEÑAR / DETENER | existían fundamentos, no una decisión doméstica integrada |
| Reconstruir situación jurídica y predial | LGUC/OGUC, permisos y antecedentes | ARQ-391–400 | PARCIAL | nuevo ARQ-802–803 y 807 | carpeta predial, ficha normativa y árbol | faltaba el hilo predio–actuación–formulario–cierre |
| Diagnosticar vivienda existente sin intervenir peligrosamente | suelo, estructuras y rehabilitación | ARQ-181–210, 381–390, 489 | PARCIAL | nuevo ARQ-804–805 | mapa de riesgos y factibilidad | los bloques disciplinares no estaban traducidos a límites del propietario |
| Programar recintos y crecimiento | vivienda unifamiliar, incremental y accesible | ARQ-142, 144–145, 481, 485 | YA EXISTE | reutilizar como prerrequisito y aplicar en ARQ-806 | cuadro y alternativas de 80/24 m² | duplicar teoría de vivienda no aportaba valor |
| Contratar profesionales y asignar firmas | responsabilidades, contratos y coordinación | ARQ-395, 401–410 | PARCIAL | nuevo ARQ-808 y 819 | RACI y comparador contractual | faltaba secuencia de contratación para ambos casos |
| Leer y coordinar proyecto | planos, estructura, envolvente e instalaciones | ARQ-191–210, 271–280, 301–330, 401–403 | PARCIAL | nuevo ARQ-811–815 | set comentado y matrices | se reutiliza teoría; se crea integración propietaria |
| Cubicar y presupuestar | factibilidad, cubicación, APU, caja y sensibilidad | ARQ-411–420 | PARCIAL | nuevo ARQ-816–817, 827 y herramientas | CSV, XLSX, APU y flujo | faltaban dos presupuestos longitudinales editables |
| Tramitar permiso y observaciones | permisos, documentos y versiones | ARQ-393–395, 401, 403, 409–410 | PARCIAL | nuevo ARQ-818 | checklist de expediente | faltaba distinguir formularios y técnicas habilitantes por actuación |
| Programar y autorizar inicio | planificación, logística y seguridad | ARQ-421–427 | PARCIAL | nuevo ARQ-820–821 | línea base y checklist de preinicio | faltaba una puerta explícita de no inicio |
| Comprender secuencia sin convertirla en manual peligroso | oficios, obra gruesa, calidad e instalaciones | ARQ-381–390, 424–426 | PARCIAL | nuevo ARQ-822–826 | secuencias conceptuales y puntos de espera | la ruta exige inspección y preguntas, no instrucciones de ejecución |
| Controlar cambios, atrasos y sobrecostos | cambios, avance y conflictos | ARQ-408–409, 416–417, 428–429 | PARCIAL | nuevo ARQ-827–829 | libro de costos y órdenes de cambio | faltaba aplicación continua a vivienda ocupada y casa nueva |
| Recibir, cerrar y mantener | pruebas, documentación y operación | ARQ-309, 319–320, 330, 410, 430, 490 | PARCIAL | nuevo ARQ-830 | carpeta de cierre doble | no existía un cierre DOM/SEC/mantenimiento de ambos casos |
| Crear un taller nuevo | diez talleres ya cubren vivienda, obra y documentación | EST-03, EST-06, EST-10 | NO CORRESPONDE | reutilizar EST-03 y EST-06 | checkpoints de RUTA-34 | un EST-11 duplicaría una estructura existente |

## 2. Decisión de alcance

Se justifican las 30 clases ARQ-801–830. No repiten teoría disciplinar: transforman clases existentes en una cadena de decisiones y evidencias para una persona propietaria. La brecha es longitudinal. Reducir el bloque dejaría uno de los dos expedientes sin continuidad entre factibilidad, proyecto, costo, obra y recepción.

La ampliación forma una Fase IV de aplicación práctica. Se conservan intactas las 800 IDs históricas y todos los artefactos `v1.0`. El estado actual pasa a 830 clases, 83 partes y 34 rutas; talleres y sesiones permanecen en 10 y 60.

## 3. Mapa de integración

| Bloque | IDs nuevos | Clases reutilizadas | Caso y salida |
|---|---|---|---|
| factibilidad y puerta 1 | ARQ-801–810 | 141–150, 181–210, 393–395, 411–420, 481, 485, 489 | dossier de ambos casos y decisión GO / REDISEÑAR / DETENER |
| proyecto, costo y puerta 2 | ARQ-811–820 | 271–280, 301–330, 401–423 | planos didácticos, matriz de redes, cubicación, presupuesto, contrato y NO INICIAR |
| obra, control y cierre | ARQ-821–830 | 381–390, 424–430, 490 | libro de obra, costos, cambios, recepción y mantenimiento |
| ruta | RUTA-34 | partes 03, 11, 15, 19–21, 27–28, 31–35, 39–43 y 49 | diagnóstico, ARQ-801–830, checkpoints EST-03/EST-06 y dos casos |

Los casos están en [`cases/CASA-NUEVA-80.md`](../cases/CASA-NUEVA-80.md) y [`cases/AMPLIACION-24.md`](../cases/AMPLIACION-24.md). Las plantillas CSV y el libro XLSX comparten campos y fórmulas documentados en la [guía de presupuesto](GUIA_PRESUPUESTO_VIVIENDA.md).

## 4. Verificación normativa realizada

Se consultaron en vivo fuentes oficiales de BCN, MINVU y SEC. La LGUC vigente confirma la regla general de permiso en el artículo 116, la tabla de derechos del artículo 130 —1,5 % para obra nueva y ampliación sobre el presupuesto aplicable— y la recepción/archivo habilitante de los artículos 144–145. MINVU mantiene familias separadas de formularios para ampliación hasta 100 m² y para obra nueva o ampliación mayor; ambas páginas incluyen también declaraciones juradas, por lo que la técnica exacta debe revalidarse para fecha y caso.

La página MINVU de reglamentación térmica declara vigente desde el 28 de noviembre de 2025 la actualización del artículo 4.1.10 OGUC. SEC identifica TE1 y TC6 dentro de e-Declarador para instaladores y profesionales autorizados. Ninguna clase garantiza aprobación, exención o aplicabilidad automática.

## 5. Estado de revisión y riesgos remanentes

- Revisión normativa: fuentes oficiales consultadas y límites documentados; la aplicación a predios reales sigue pendiente.
- Revisión profesional externa: **pendiente**. Las clases no deben presentarse como orientación ejecutiva hasta que especialistas chilenos revisen normativa, estructura, geotecnia, construcción, prevención e instalaciones.
- Precios reales: no incorporados. Los ejemplos están marcados `HIPOTÉTICO`; deben sustituirse por cotizaciones locales comparables.
- Piloto con estudiantes: pendiente. La carga horaria y efectividad no se declaran.
- Formularios y técnicas habilitantes: pueden cambiar; comprobar fecha, transición y cobertura de DOM en Línea antes de cada ingreso.

## 6. Regla de publicación

La integración debe regenerar bibliografía, decisiones, pedagogía, índices y sitio; ejecutar todos los controles de CI; revisar el diff; confirmar `main`; publicar solo con autorización explícita; y comprobar el resultado remoto sin dejar ramas de trabajo pendientes.
