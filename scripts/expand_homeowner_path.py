#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Add the homeowner learning path (ARQ-801..830) and its canonical manifests.

This is an authored expansion helper, not a site generator.  It is deliberately
idempotent: existing lesson files are preserved unless --refresh is supplied.
Derived indexes, pedagogy, bibliography and site output remain the responsibility
of the repository's existing generators.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "catalog.json"
PARTS = ROOT / "data" / "parts.json"
PEDAGOGY = ROOT / "data" / "pedagogy.json"
PROGRAM = ROOT / "data" / "program.json"
CONSULTED = "12 de octubre de 2026"


PART_DEFINITIONS = {
    81: (
        "Antes de construir: decisión, terreno, legalidad y permisos",
        "convertir una intención doméstica en una decisión GO, REDISEÑAR o DETENER sustentada por antecedentes del predio, riesgos, atribuciones y capacidad financiera",
        "dossier de factibilidad con antecedentes, consultas, responsables, alternativas y puerta formal de decisión",
    ),
    82: (
        "Proyecto, presupuesto detallado, compras y autorización",
        "coordinar información técnica, cantidades, precios, contratos y habilitaciones sin confundir una estimación educativa con proyecto ejecutable o autorización",
        "expediente coordinado de proyecto, presupuesto, contratación, cronograma y autorización de inicio",
    ),
    83: (
        "Construcción, control de gastos, recepción y mantenimiento",
        "seguir la obra mediante hitos verificables de seguridad, calidad, costo y cambio hasta formar una carpeta de recepción y mantenimiento",
        "libro de control de obra, carpeta de cierre y plan de mantenimiento para ambos casos",
    ),
}


LESSONS = [
    {
        "title": "Construir, ampliar, reparar o comprar: definir objetivo, alcance y límite económico",
        "evidence": "ficha de decisión con necesidades priorizadas, cuatro alternativas comparables, límite financiero y regla GO / REDISEÑAR / DETENER",
        "focus": ["necesidad familiar", "alternativas equivalentes", "costo total", "tiempo de uso", "condición de abandono"],
        "critical": "una preferencia no puede presentarse como necesidad ni el financiamiento esperado como dinero disponible",
        "prereqs": ["ARQ-031", "ARQ-111", "ARQ-141", "ARQ-149", "ARQ-411"],
        "guided": "Compara construir 80 m², ampliar 24 m², reparar y comprar manteniendo igual horizonte familiar. Usa un techo hipotético de CLP 95.000.000, reserva 15 % y registra qué alternativa queda fuera antes de diseñar.",
        "new_case": "El hogar necesita tres dormitorios y continuidad de uso por quince años. La parcela urbanizada, la comuna y la disponibilidad de servicios son supuestos pendientes de CIP y factibilidades.",
        "extension_case": "La vivienda existente parece admitir 24 m² en un nivel, pero su permiso, recepción, estructura y redes aún no están comprobados; la alternativa de segundo piso permanece detenida hasta diagnóstico profesional.",
    },
    {
        "title": "Documentos del terreno y de la vivienda: dominio, rol, planos, permisos y recepciones existentes",
        "evidence": "índice de carpeta predial con documento, emisor, fecha, versión, estado, discrepancia y acción de obtención",
        "focus": ["identidad del predio", "título y rol", "archivo DOM", "permiso y recepción", "cadena de versiones"],
        "critical": "la existencia física de una construcción no demuestra que esté permitida o recibida",
        "prereqs": ["ARQ-004", "ARQ-393", "ARQ-394", "ARQ-481"],
        "guided": "Clasifica doce antecedentes simulados: escritura, inscripción, certificado de avalúo, CIP, plano de loteo, permiso, recepción, planos, certificado de número, factibilidades y dos documentos contradictorios.",
        "new_case": "CASA-NUEVA-80 parte con terreno ficticio sin edificaciones declaradas; debe comprobar dominio, rol, deslindes, urbanización y correspondencia entre catastro y realidad antes del encargo profesional.",
        "extension_case": "AMPLIACION-24 exige reconstruir la historia de la vivienda: permiso original, modificaciones, recepciones, superficies y diferencias entre el archivo municipal, la escritura y el levantamiento actual.",
    },
    {
        "title": "Certificado de Informaciones Previas, plan regulador y restricciones del predio",
        "evidence": "ficha normativa de predio que separa texto del CIP, medición del proyecto, interpretación profesional y preguntas pendientes a la DOM",
        "focus": ["CIP", "uso de suelo", "ocupación y constructibilidad", "rasante y distanciamiento", "vigencia del instrumento"],
        "critical": "un parámetro copiado sin predio, comuna, instrumento y fecha no autoriza una solución",
        "prereqs": ["ARQ-123", "ARQ-124", "ARQ-393", "ARQ-394"],
        "guided": "Lee un CIP simulado que declara uso residencial, líneas, afectación y normas. Marca cada dato como transcripción, cálculo, inferencia o pendiente y formula cinco preguntas que el certificado no responde.",
        "new_case": "La ficha hipotética de CASA-NUEVA-80 usa una comuna y dirección deliberadamente ficticias. Ningún coeficiente se traslada a un predio real; el ejercicio enseña dónde registrarlo y cómo detectar incompatibilidades.",
        "extension_case": "La ampliación debe recalcular superficie total y relaciones con deslindes después de sumar 24 m². Un adosamiento aparente o una obra vecina no constituyen precedente autorizante.",
    },
    {
        "title": "Estado actual: levantamiento, patologías y elementos que no deben intervenirse sin diagnóstico",
        "evidence": "plano didáctico existente / propuesto con fotografías referenciadas, mapa de daños, incertidumbres y matriz de derivación a especialistas",
        "focus": ["levantamiento", "patología", "muro portante", "humedad", "evidencia antes de intervenir"],
        "critical": "ningún dibujo del propietario autoriza demoler, perforar o sobrecargar un elemento posiblemente estructural",
        "prereqs": ["ARQ-026", "ARQ-181", "ARQ-191", "ARQ-201", "ARQ-489"],
        "guided": "Sobre un croquis de 8 × 9 m ubica grietas, deformaciones, humedad, tableros y recorridos visibles. Asigna nivel de incertidumbre y define qué observación detiene cualquier demolición.",
        "new_case": "En terreno vacío el levantamiento se concentra en límites, cotas, árboles, rellenos, servicios y construcciones vecinas; no se inventa una condición de suelo a partir de la superficie.",
        "extension_case": "La ampliación registra la vivienda ocupada, muros y techumbre existentes, cortes de servicio y daños previos. El segundo piso solo se representa como pregunta de factibilidad estructural.",
    },
    {
        "title": "Servicios, suelo, topografía, amenazas, entorno y acceso de maquinaria",
        "evidence": "informe de factibilidad con mapa de consultas, especialistas, accesos, amenazas, servicios y condiciones que cambian costo o detienen el proyecto",
        "focus": ["factibilidad sanitaria", "energía", "mecánica de suelos", "topografía", "logística y amenazas"],
        "critical": "desconocido no equivale a disponible, firme, seguro ni incluido en el precio",
        "prereqs": ["ARQ-121", "ARQ-181", "ARQ-183", "ARQ-187", "ARQ-301", "ARQ-321"],
        "guided": "Construye una matriz de veinte verificaciones para un sitio con 8 % de pendiente y acceso de 2,8 m. Distingue visita visual, certificado, estudio profesional y coordinación con empresa de servicio.",
        "new_case": "CASA-NUEVA-80 supone urbanización, pero debe verificar agua, alcantarillado, electricidad, acceso y nivelación. El suelo y la amenaza no se deducen del valor comercial del terreno.",
        "extension_case": "AMPLIACION-24 añade interferencias con redes en servicio, ocupantes y acceso restringido. Las conexiones existentes se inspeccionan; no se presume capacidad remanente.",
    },
    {
        "title": "Programa de recintos, superficie, habitabilidad, accesibilidad y crecimiento",
        "evidence": "cuadro de superficies y tres esquemas comparables con relaciones, prioridades, accesibilidad, ventilación y crecimiento declarado",
        "focus": ["programa familiar", "superficie útil", "habitabilidad", "accesibilidad", "crecimiento por etapas"],
        "critical": "la suma de recintos no reemplaza comprobar circulación, orientación, ventilación, estructura y norma",
        "prereqs": ["ARQ-033", "ARQ-111", "ARQ-142", "ARQ-144", "ARQ-145"],
        "guided": "Distribuye 80 m² construidos entre recintos, circulación, muros y almacenamiento. Produce tres alternativas con la misma necesidad y registra qué sacrifica cada una.",
        "new_case": "La casa nueva compara esquema compacto, patio protegido y crecimiento futuro, manteniendo explícitos los metros útiles y construidos y la relación con el terreno.",
        "extension_case": "La ampliación prueba dormitorio, estar y recinto húmedo alternativos. Si un espacio existente cambia a cocina, baño o dormitorio, se reevalúan ventilación, redes, evacuación y habitabilidad.",
    },
    {
        "title": "Árbol de decisiones de trámites para obra nueva, ampliación y situaciones especiales",
        "evidence": "árbol de decisión con tipo de actuación, autoridad, técnica habilitante o permiso, formulario oficial, condición, responsable y evidencia de cierre",
        "focus": ["artículo 116 LGUC", "obra menor", "obra nueva", "declaración jurada", "bifurcaciones rural, riesgo, patrimonio y copropiedad"],
        "critical": "una ampliación pequeña no se declara exenta solo por su superficie",
        "prereqs": ["ARQ-391", "ARQ-392", "ARQ-393", "ARQ-394", "ARQ-395"],
        "guided": "Clasifica ocho situaciones: obra nueva, ampliación 24 m², ampliación sobre 100 m², alteración, vivienda social, rural, copropiedad y patrimonio. En cada hoja deja una salida VERIFICAR cuando falte una condición.",
        "new_case": "CASA-NUEVA-80 sigue el grupo oficial de obra nueva y requiere confirmar antecedentes y técnica habilitante vigente con el profesional y la DOM del predio.",
        "extension_case": "AMPLIACION-24 se contrasta con formularios de ampliación hasta 100 m², pero su estructura, situación jurídica y emplazamiento pueden activar antecedentes o procedimientos adicionales.",
    },
    {
        "title": "A quién contratar y cuándo: matriz de responsabilidades, firmas y coordinación",
        "evidence": "matriz RACI con encargo, entregable, autoridad, firma, revisión, costo, momento de contratación y conflicto de interés",
        "focus": ["propietario", "arquitecto", "calculista", "constructor", "especialidades e inspección"],
        "critical": "coordinar o pagar un servicio no transfiere al propietario la competencia ni la responsabilidad legal del profesional",
        "prereqs": ["ARQ-395", "ARQ-406", "ARQ-481"],
        "guided": "Asigna veinticinco tareas entre propietario, arquitecto, calculista, especialista de suelo, instaladores autorizados, constructor, ITO cuando corresponda y DOM. Resuelve cinco conflictos de doble aprobación.",
        "new_case": "La casa nueva requiere definir tempranamente arquitectura, cálculo, especialidades y construcción; las responsabilidades se vinculan a entregables y no solo a nombres o honorarios.",
        "extension_case": "La ampliación añade diagnóstico de lo existente, compatibilidad estructural, protección de residentes y verificación de permisos históricos. El segundo piso exige una evaluación específica antes de cotizar ejecución.",
    },
    {
        "title": "Presupuesto preliminar, financiación, costos ocultos y viabilidad",
        "evidence": "estimación de orden de magnitud en CLP con fecha, alcance, fuente o etiqueta HIPOTÉTICO, tres escenarios, contingencia y brecha de financiamiento",
        "focus": ["costo por metro cuadrado", "alcance comparable", "honorarios y permisos", "contingencia", "financiamiento y detención"],
        "critical": "un precio por metro cuadrado sin alcance, ubicación, fecha e incertidumbre no es presupuesto",
        "prereqs": ["ARQ-149", "ARQ-411", "ARQ-415", "ARQ-418", "ARQ-420"],
        "guided": "Modela tres referencias hipotéticas de CLP 850.000, 1.150.000 y 1.500.000 por m² sin llamarlas precios vigentes. Agrega partidas externas y sensibilidad ±15 %; compara con financiamiento disponible.",
        "new_case": "CASA-NUEVA-80 separa edificio, obras exteriores, profesionales, estudios, permisos, conexiones, contingencia y equipamiento no incluido.",
        "extension_case": "AMPLIACION-24 no hereda el costo por m² de una casa nueva: suma demolición selectiva, protecciones, encuentros, interrupciones, refuerzos pendientes y recuperación de terminaciones.",
    },
    {
        "title": "Primera puerta de control: decidir si iniciar el proyecto",
        "evidence": "dossier GO / REDISEÑAR / DETENER firmado como decisión del ejercicio, con condiciones legales, técnicas, financieras y familiares",
        "focus": ["criterio de entrada", "condición crítica", "evidencia mínima", "alternativa de rediseño", "registro de decisión"],
        "critical": "ningún promedio favorable compensa una condición legal, estructural o financiera no resuelta",
        "prereqs": ["ARQ-801", "ARQ-802", "ARQ-803", "ARQ-804", "ARQ-805", "ARQ-806", "ARQ-807", "ARQ-808", "ARQ-809"],
        "guided": "Revisa un expediente con 18 criterios, tres rojos y cinco amarillos. Justifica si el resultado es GO condicionado, REDISEÑAR o DETENER sin convertir los rojos en puntos compensables.",
        "new_case": "La casa avanza solo si el predio, servicios, programa, equipo y financiamiento tienen evidencia suficiente para contratar anteproyecto; de otro modo se rediseña o posterga.",
        "extension_case": "La ampliación se detiene ante permiso histórico incierto, diagnóstico estructural pendiente o imposibilidad de proteger ocupantes. La alternativa de segundo piso conserva un NO INICIAR explícito.",
    },
    {
        "title": "Levantamiento con medidas, cotas, deslindes, superficies y fotografías",
        "evidence": "plano base didáctico con método de medición, control de cierre, escala, cotas, fotografías y registro de incertidumbres",
        "focus": ["referencia y escala", "triangulación", "control de cierre", "deslinde", "incertidumbre de levantamiento"],
        "critical": "un levantamiento educativo no reemplaza el levantamiento profesional exigible ni permite fijar un deslinde",
        "prereqs": ["ARQ-021", "ARQ-026", "ARQ-381", "ARQ-804"],
        "guided": "Levanta un recinto simple con dos diagonales y calcula el error de cierre. Relaciona seis fotografías con el croquis y separa dimensión observada, estimada y obtenida de plano anterior.",
        "new_case": "CASA-NUEVA-80 usa el levantamiento para ubicar accesos, cotas, vecinos y servicios; las dimensiones legales del predio se toman de antecedentes competentes.",
        "extension_case": "AMPLIACION-24 necesita capas antes / después, espesores no confirmados, niveles de piso, cubierta, vanos y redes visibles, sin perforaciones exploratorias del propietario.",
    },
    {
        "title": "Leer plantas, cortes, elevaciones, emplazamiento, detalles y especificaciones",
        "evidence": "set de planos didácticos comentados con referencias cruzadas, escalas, versiones, contradicciones y preguntas de coordinación",
        "focus": ["planta", "corte", "elevación", "detalle", "especificación y versión"],
        "critical": "una vista aislada nunca demuestra por sí sola geometría, material, desempeño y autorización",
        "prereqs": ["ARQ-022", "ARQ-024", "ARQ-401", "ARQ-403"],
        "guided": "Sigue diez llamadas entre una planta, dos cortes, cuatro elevaciones y detalles. Detecta una cota incompatible, una especificación ambigua y una revisión antigua.",
        "new_case": "El set de la casa muestra emplazamiento, recorridos, sección de cubierta y relación con terreno como dibujos educativos que deben ser desarrollados y firmados por profesionales competentes.",
        "extension_case": "La ampliación compara existente y propuesto, y exige que cada encuentro con muro, piso, cubierta y red tenga referencia a una revisión específica.",
    },
    {
        "title": "Coordinación de suelo, fundaciones, estructura y sismo",
        "evidence": "matriz de entregables estructurales y geotécnicos con entradas, interfaces, revisores, puntos de espera y preguntas al calculista",
        "focus": ["modelo de suelo", "camino de cargas", "fundación", "junta y encuentro", "responsabilidad del calculista"],
        "critical": "un esquema conceptual o resultado de IA no dimensiona fundaciones, refuerzos ni conexiones",
        "prereqs": ["ARQ-181", "ARQ-186", "ARQ-189", "ARQ-191", "ARQ-210", "ARQ-395"],
        "guided": "Ordena veinte entradas entre estudio de suelo, arquitectura, cálculo y obra. Identifica cinco puntos donde una modificación arquitectónica exige reconsulta estructural.",
        "new_case": "La casa nueva coordina cota de piso, drenaje, suelo, fundaciones y sistema resistente desde el anteproyecto sin fijar dimensiones didácticas como solución.",
        "extension_case": "La ampliación compara adosada y separada mediante interfaces. Cualquier segundo piso o apertura en muro existente queda sujeto a diagnóstico, cálculo y detalle profesional.",
    },
    {
        "title": "Cubierta y envolvente: lluvia, impermeabilización, ventanas, condensación y exigencia térmica",
        "evidence": "detalle conceptual de encuentro de cubierta y matriz de agua, aire, vapor, calor, mantenimiento y verificación normativa",
        "focus": ["escurrimiento", "continuidad de barreras", "puente térmico", "condensación", "zona térmica y fecha"],
        "critical": "una capa dibujada sin continuidad, pendiente, salida de agua y criterio de comprobación no controla humedad",
        "prereqs": ["ARQ-205", "ARQ-271", "ARQ-272", "ARQ-273", "ARQ-316", "ARQ-398"],
        "guided": "Traza agua, aire, vapor y calor a través de un encuentro muro-cubierta. Marca tres discontinuidades y consulta la zona térmica aplicable sin copiar valores de otra localidad.",
        "new_case": "CASA-NUEVA-80 compara tres niveles de desempeño con alcance equivalente y aplica la actualización del artículo 4.1.10 OGUC vigente desde noviembre de 2025 según zona y expediente.",
        "extension_case": "AMPLIACION-24 concentra riesgo en el encuentro de techumbres, medianero, canaletas y diferencias de aislación; se documenta cómo inspeccionar sin prescribir una solución estructural.",
    },
    {
        "title": "Redes de agua, alcantarillado, electricidad y gas: factibilidades y declaraciones",
        "evidence": "matriz de redes con demanda, capacidad a verificar, responsable autorizado, interferencias, pruebas, declaración y certificado aplicable",
        "focus": ["factibilidad", "agua y alcantarillado", "TE1", "TC6", "pruebas y recepción"],
        "critical": "el propietario no firma ni declara instalaciones reservadas a instaladores o profesionales autorizados",
        "prereqs": ["ARQ-301", "ARQ-304", "ARQ-309", "ARQ-321", "ARQ-324", "ARQ-330"],
        "guided": "Coordina veinte puntos de consumo y evacuación de forma conceptual. Para cada red registra entrada, cruce, prueba, responsable y documento, sin calcular diámetros ni protecciones.",
        "new_case": "La casa nueva solicita factibilidades y coordina trazados antes de cerrar estructura y envolvente. TE1 y TC6 aparecen solo cuando correspondan y los gestiona personal autorizado.",
        "extension_case": "La ampliación debe verificar capacidad y estado de redes existentes, mantener continuidad de servicios y prever cortes controlados; no basta conectarse al punto más cercano.",
    },
    {
        "title": "Cubicaciones auditables: unidades, pérdidas, transporte y rendimientos",
        "evidence": "hoja de cantidades por partida con geometría, unidad, cantidad neta, merma separada, compra redondeada, fuente y revisor",
        "focus": ["unidad de medición", "cantidad neta", "merma", "redondeo de compra", "trazabilidad al plano"],
        "critical": "la merma no corrige una medición sin geometría ni debe esconderse dentro del precio unitario",
        "prereqs": ["ARQ-003", "ARQ-412", "ARQ-413", "ARQ-812"],
        "guided": "Cubica 80 m² de piso con 7 % de merma y cajas de 1,44 m²; separa área neta, área con merma y número entero de cajas. Repite con una abertura y documenta la deducción.",
        "new_case": "CASA-NUEVA-80 organiza movimiento de tierra, estructura, envolvente, redes, terminaciones y exteriores con reglas de medición visibles.",
        "extension_case": "AMPLIACION-24 agrega desmontajes, protecciones y recuperación. Las cantidades de refuerzo permanecen PENDIENTE PROFESIONAL hasta existir proyecto.",
    },
    {
        "title": "Análisis de precios unitarios, presupuesto completo, IVA y contingencia",
        "evidence": "presupuesto en CLP con APU de materiales, mano de obra, equipos, transporte, subtotal, IVA configurable, indirectos, honorarios, permisos y contingencia",
        "focus": ["APU", "rendimiento", "precio cotizado", "IVA", "contingencia y total a término"],
        "critical": "una cotización comercial no demuestra cantidad, rendimiento, alcance completo ni costo final",
        "prereqs": ["ARQ-414", "ARQ-415", "ARQ-416", "ARQ-417", "ARQ-816"],
        "guided": "Calcula una partida con 42 unidades, 3 % de pérdida, precio unitario hipotético CLP 18.500, transporte CLP 95.000 e IVA 19 % configurable. Comprueba el resultado por una segunda operación.",
        "new_case": "La casa compara económico, estándar y mayor desempeño con el mismo alcance. Las diferencias de especificación se declaran y las cifras de ejemplo se rotulan HIPOTÉTICAS.",
        "extension_case": "La ampliación incorpora demolición selectiva, polvo, cortes, reubicación temporal, encuentros y reposición. Su costo unitario no se fuerza a coincidir con la casa nueva.",
    },
    {
        "title": "Expediente de permiso: documentos, ingreso, observaciones y seguimiento DOM",
        "evidence": "checklist de expediente con formulario vigente, responsable, versión, fecha, estado, observación, respuesta y trazabilidad de reingreso",
        "focus": ["Formulario Único Nacional", "antecedente exigible", "ingreso", "acta de observaciones", "versión aprobada"],
        "critical": "un expediente simulado no acredita ingreso, permiso, declaración archivada ni aprobación de autoridad",
        "prereqs": ["ARQ-394", "ARQ-401", "ARQ-403", "ARQ-409", "ARQ-807"],
        "guided": "Ordena un expediente ficticio con cinco versiones y un acta de observaciones. Traza cada respuesta al plano o documento que cambia y evita sustituir al profesional firmante.",
        "new_case": "CASA-NUEVA-80 usa el formulario oficial de obra nueva que corresponda al régimen vigente y conserva comprobantes y resolución separados de borradores.",
        "extension_case": "AMPLIACION-24 contrasta el formulario de ampliación hasta 100 m² con su condición real. Si el archivo histórico es incompleto, el pendiente no se disfraza como regularización automática.",
    },
    {
        "title": "Cotizaciones, contratos, subcontratistas, seguros, garantías y pagos",
        "evidence": "comparador de tres ofertas normalizadas y modelo contractual comentado con alcance, exclusiones, hitos, cambios, garantías, seguros y cierre",
        "focus": ["alcance comparable", "exclusión", "hito de pago", "orden de cambio", "garantía y controversia"],
        "critical": "el menor total no es comparable si omite cantidades, impuestos, transporte, permisos, pruebas o cierre",
        "prereqs": ["ARQ-404", "ARQ-405", "ARQ-406", "ARQ-407", "ARQ-417"],
        "guided": "Normaliza tres ofertas: una con IVA, otra sin transporte y otra con alcance parcial. Calcula precio comparable y redacta diez consultas antes de adjudicar.",
        "new_case": "La casa evalúa contratista general y contratación por partidas, incluyendo capacidad de coordinación, seguridad, garantías y costo de administración del propietario.",
        "extension_case": "La ampliación exige reglas para protección de ocupantes, descubrimientos imprevistos, cortes, daños a terminaciones y restitución diaria de condiciones seguras.",
    },
    {
        "title": "Cronograma, compras, ruta crítica y autorización para iniciar",
        "evidence": "línea base costo-plazo con dependencias, hitos de compra, restricciones, responsables y puerta NO INICIAR SIN HABILITACIONES",
        "focus": ["desglose del trabajo", "dependencia", "ruta crítica", "compra de largo plazo", "permiso para iniciar"],
        "critical": "una fecha contractual no autoriza iniciar sin antecedentes, responsables y habilitaciones aplicables",
        "prereqs": ["ARQ-421", "ARQ-422", "ARQ-423", "ARQ-426", "ARQ-818", "ARQ-819"],
        "guided": "Ordena quince actividades con tres compras de largo plazo y dos inspecciones. Calcula holguras simples y mueve una entrega siete días para observar la consecuencia.",
        "new_case": "CASA-NUEVA-80 coordina permiso, servicios, estudios, fundaciones, estructura, cierre de agua, instalaciones, terminaciones y recepción.",
        "extension_case": "AMPLIACION-24 agrega mudanza temporal, protección diaria, cortes de suministro y ventanas de trabajo vecinal. La ruta crítica incluye la interfaz con la vivienda ocupada.",
    },
    {
        "title": "Instalación de faenas, protección de lo existente, cierres, vecinos, accesos y acopios",
        "evidence": "checklist de preinicio y plano logístico con zonas, accesos, servicios temporales, emergencias, acopios, residuos y responsables",
        "focus": ["segregación", "acceso seguro", "acopio", "servicio temporal", "comunicación vecinal"],
        "critical": "la instalación de faena no comienza mientras personas, tránsito, energía, excavaciones o emergencias carezcan de control responsable",
        "prereqs": ["ARQ-381", "ARQ-389", "ARQ-423", "ARQ-426", "ARQ-427"],
        "guided": "Dibuja una faena pequeña con acceso de camión, peatones, acopio, residuos y tablero temporal. Detecta seis cruces incompatibles y asigna quién debe resolverlos.",
        "new_case": "La casa dispone cierres y acopios sin invadir espacio público ni bloquear drenajes. El esquema es de coordinación, no un plan de seguridad ejecutable.",
        "extension_case": "La ampliación separa obra y vivienda ocupada, define rutas limpias, control de polvo, mascotas, niños, cortes y restitución al final de cada jornada.",
    },
    {
        "title": "Movimiento de tierra, excavaciones, fundaciones, humedad y puntos de inspección",
        "evidence": "secuencia conceptual con puntos de espera, evidencia de suelo, inspecciones, registro fotográfico y aceptación por responsables competentes",
        "focus": ["replanteo", "excavación", "estabilidad", "sello de fundación", "agua y punto de espera"],
        "critical": "el propietario no excava, entiba, socalza ni acepta el sello de fundación a partir de esta clase",
        "prereqs": ["ARQ-181", "ARQ-183", "ARQ-186", "ARQ-187", "ARQ-382"],
        "guided": "Ordena doce hitos desde replanteo hasta fundación. Inserta puntos de espera antes de cubrir suelo, armaduras, pasadas y barreras de humedad.",
        "new_case": "CASA-NUEVA-80 documenta discrepancias entre terreno, estudio y excavación para que el profesional decida antes de hormigonar.",
        "extension_case": "AMPLIACION-24 incorpora cercanía a fundaciones y medianeros existentes; cualquier socalzado, excavación profunda o pérdida de apoyo detiene el trabajo.",
    },
    {
        "title": "Obra gruesa: estructura, muros, anclajes, cubierta y conexión con lo existente",
        "evidence": "diagrama de dependencias y protocolo de aceptación con planos vigentes, tolerancias, inspecciones, no conformidades y firma competente",
        "focus": ["secuencia resistente", "anclaje", "apuntalamiento", "tolerancia", "aceptación estructural"],
        "critical": "ninguna conexión estructural se improvisa en obra ni se acepta solo por apariencia",
        "prereqs": ["ARQ-191", "ARQ-201", "ARQ-205", "ARQ-383", "ARQ-424"],
        "guided": "Relaciona veinte controles con cinco etapas de obra gruesa. Para cada desviación define registrar, proteger, consultar, corregir y volver a inspeccionar.",
        "new_case": "La casa nueva conserva continuidad del camino de cargas y controla pasadas antes de ejecutar. Los detalles provienen del proyecto competente.",
        "extension_case": "La ampliación controla encuentro, junta, apoyo y cubierta sin cortar muros ni cerchas hasta recibir instrucción. El segundo piso sigue fuera del alcance ejecutable.",
    },
    {
        "title": "Envolvente: techumbre, aislación, impermeabilización, vanos y escurrimientos",
        "evidence": "ficha de inspección de envolvente con muestra aprobada, continuidad, pruebas, fotografías, responsable, resultado y reparación",
        "focus": ["muestra", "continuidad", "vano", "sellado", "prueba de agua y mantenimiento"],
        "critical": "cubrir una interfaz antes de inspeccionarla elimina evidencia y puede convertir una falla local en daño oculto",
        "prereqs": ["ARQ-271", "ARQ-272", "ARQ-273", "ARQ-388", "ARQ-424", "ARQ-814"],
        "guided": "Prepara una ficha para diez interfaces. Define evidencia antes, durante y después, condición meteorológica y criterio para repetir la prueba.",
        "new_case": "CASA-NUEVA-80 vincula techumbre, muros, vanos, sobrecimientos y drenaje exterior con la zona térmica y especificación vigente.",
        "extension_case": "AMPLIACION-24 prioriza el encuentro de cubiertas, canaletas compartidas, medianeros y diferencias de nivel que pueden devolver agua hacia lo existente.",
    },
    {
        "title": "Instalaciones empotradas y visibles, interferencias, pruebas y certificados",
        "evidence": "plan de coordinación con zonas de reserva, cruces, pruebas antes de cerrar, actas, declaraciones y responsables autorizados",
        "focus": ["reserva", "interferencia", "prueba previa al cierre", "TE1 y TC6", "manual y trazabilidad"],
        "critical": "una instalación no se energiza, conecta, oculta ni recibe sin prueba y responsable autorizado cuando corresponda",
        "prereqs": ["ARQ-308", "ARQ-309", "ARQ-317", "ARQ-321", "ARQ-324", "ARQ-330"],
        "guided": "Coordina quince cruces entre estructura, agua, alcantarillado, electricidad, gas y ventilación. Registra prioridad, responsable, revisión y prueba antes de cerrar.",
        "new_case": "La casa nueva reserva recorridos y registros desde el proyecto, evitando perforaciones tardías y manteniendo documentos para recepción.",
        "extension_case": "La ampliación identifica redes activas, programa cortes y verifica empalmes. Toda modificación conserva referencia a la instalación original y su declaración cuando corresponda.",
    },
    {
        "title": "Terminaciones: revestimientos, pisos, carpinterías, baños, cocina y accesibilidad",
        "evidence": "lista de tolerancias y muestras con soporte, preparación, apariencia, uso, limpieza, mantenimiento, defecto y aceptación",
        "focus": ["muestra aprobada", "soporte", "tolerancia", "accesibilidad", "mantenimiento"],
        "critical": "una terminación aceptable visualmente puede fallar por soporte, humedad, pendiente, seguridad o imposibilidad de mantenerla",
        "prereqs": ["ARQ-274", "ARQ-385", "ARQ-388", "ARQ-424"],
        "guided": "Compara tres muestras de piso con igual área útil. Verifica soporte, juntas, resbalamiento, encuentro, limpieza y repuesto; registra una muestra rechazada.",
        "new_case": "CASA-NUEVA-80 alinea terminaciones con tres escenarios sin cambiar silenciosamente durabilidad, accesibilidad o alcance de recintos.",
        "extension_case": "AMPLIACION-24 incluye reparación de superficies afectadas y transición entre material nuevo y existente; se acuerda hasta dónde llega cada reposición.",
    },
    {
        "title": "Control del presupuesto durante la obra: avance, pagos, compras, cambios y flujo de caja",
        "evidence": "libro de costos con presupuesto base, comprometido, pagado, avance físico, saldo, cambios, IVA y proyección a término",
        "focus": ["línea base", "avance físico", "compromiso", "pago", "estimación a término"],
        "critical": "pagar según calendario o factura sin comprobar alcance y avance rompe el vínculo entre dinero y obra",
        "prereqs": ["ARQ-416", "ARQ-417", "ARQ-429", "ARQ-817", "ARQ-820"],
        "guided": "Con presupuesto hipotético CLP 100.000.000, avance planificado 45 %, físico 38 %, comprometido 60 % y pagado 35 %, calcula desviaciones y formula preguntas antes del próximo pago.",
        "new_case": "La casa sigue costos por capítulo y curva mensual, separando anticipos, acopios verificados, retenciones y trabajo aceptado.",
        "extension_case": "La ampliación reserva partidas para descubrimientos y reposición. Cada cambio muestra impacto en vivienda ocupada, plazo, costo y nueva aprobación necesaria.",
    },
    {
        "title": "Seguridad, residuos, ruido, inspecciones, fallas, calidad y comunidad",
        "evidence": "registro de no conformidades e incidentes con peligro, evidencia, contención, responsable, plazo, verificación y comunicación",
        "focus": ["peligro", "control", "no conformidad", "residuo", "vecinos y cierre verificable"],
        "critical": "el propietario no sustituye la gestión preventiva del empleador, constructor ni especialistas responsables",
        "prereqs": ["ARQ-425", "ARQ-426", "ARQ-427", "ARQ-828"],
        "guided": "Clasifica doce eventos entre peligro, incidente, defecto, reclamo y cambio. Define contención inmediata y evidencia para cerrar sin borrar el registro original.",
        "new_case": "La casa coordina tránsito, altura, excavación, polvo, ruido y retiro de residuos con responsables de faena y comunicación vecinal.",
        "extension_case": "La ampliación incorpora residentes, bienes, rutas compartidas y continuidad de servicios. Una barrera de polvo no compensa un riesgo estructural o eléctrico.",
    },
    {
        "title": "Atrasos, sobrecostos y descubrimientos imprevistos: órdenes de cambio",
        "evidence": "tres incidentes resueltos mediante registro de hecho, contención, alternativas, costo, plazo, autorización, versión y cierre",
        "focus": ["hecho imprevisto", "aviso", "alternativa", "orden de cambio", "nueva autorización"],
        "critical": "una instrucción verbal no modifica de forma controlada alcance, costo, plazo ni permiso",
        "prereqs": ["ARQ-408", "ARQ-409", "ARQ-417", "ARQ-428", "ARQ-827"],
        "guided": "Resuelve hallazgo de tubería, entrega tardía y daño oculto. En cada caso compara detener, reparar, rediseñar o aceptar, y documenta quién puede decidir.",
        "new_case": "CASA-NUEVA-80 registra diferencia de suelo y atraso de ventana como eventos separados; ninguno se absorbe sin revisar costo, secuencia y responsabilidad.",
        "extension_case": "AMPLIACION-24 trata humedad oculta y red no documentada. Si cambia estructura, superficie o solución autorizada, se consulta la modificación aplicable antes de seguir.",
    },
    {
        "title": "Término de obra, certificados, recepción definitiva, garantías y mantenimiento",
        "evidence": "carpeta de cierre de ambos casos con planos finales, certificados, recepción o archivo aplicable, garantías, pendientes, manual y comparación final",
        "focus": ["as-built", "certificado", "recepción", "garantía", "mantenimiento y reapertura"],
        "critical": "terminar físicamente o pagar el saldo no equivale a contar con recepción, certificados y expediente de operación",
        "prereqs": ["ARQ-309", "ARQ-330", "ARQ-410", "ARQ-430", "ARQ-490"],
        "guided": "Audita una carpeta con treinta ítems y cinco ausencias. Clasifica qué impide recepción, qué impide uso seguro, qué queda como pendiente contractual y qué alimenta mantenimiento.",
        "new_case": "CASA-NUEVA-80 compara presupuesto inicial y final, obtiene la recepción o técnica habilitante aplicable y entrega manual con garantías y frecuencias sin prometer aprobación.",
        "extension_case": "AMPLIACION-24 cierra modificaciones de planos, redes, cubierta y superficies afectadas; la recepción histórica de la casa se conserva separada de la actuación nueva.",
    },
]


SOURCES = [
    {
        "id": "CL-LGUC",
        "title": "Ley General de Urbanismo y Construcciones, DFL 458",
        "publisher": "Biblioteca del Congreso Nacional de Chile",
        "url": "https://www.bcn.cl/leychile/navegar?idNorma=13560",
        "scope": "texto vigente consultado; artículos 1, 4, 5, 9, 16–18, 116, 127, 130 y 143–145 según la afirmación de la clase",
        "support": "marco nacional, competencias, responsabilidades, regla general de permiso, base de derechos municipales, control de obra y recepción",
        "limit": "no identifica por sí sola el procedimiento completo del predio ni reemplaza OGUC, instrumento territorial, circulares, formularios, DOM o asesoría profesional",
    },
    {
        "id": "CL-OGUC",
        "title": "Ordenanza General de Urbanismo y Construcciones, DS 47",
        "publisher": "Biblioteca del Congreso Nacional de Chile",
        "url": "https://www.bcn.cl/leychile/navegar?idNorma=8201",
        "scope": "texto oficial localizado; artículos 1.4.3, 1.6.4, 4.1.10 y 5.1.4 se deben revalidar en el expediente concreto",
        "support": "procedimientos, formularios, condiciones técnicas y categorías reglamentarias citadas por MINVU",
        "limit": "la clase no asegura vigencia de una redacción aislada ni determina aplicabilidad sin fecha, predio, actuación y revisión competente",
    },
    {
        "id": "CL-DOM-FORMS",
        "title": "Formularios de trámites de Direcciones de Obras Municipales",
        "publisher": "Ministerio de Vivienda y Urbanismo de Chile",
        "url": "https://www.minvu.gob.cl/elementos-tecnicos/formularios-de-tramites-direcciones-de-obras-municipales-dom/",
        "scope": "página oficial y familias de certificados, obras menores y obras de edificación disponibles en la fecha de consulta",
        "support": "localiza Formularios Únicos Nacionales y distingue actuaciones del solicitante y de la DOM",
        "limit": "un formulario no prueba que el caso cumpla condiciones, que el expediente esté completo ni que la autoridad lo apruebe",
    },
    {
        "id": "CL-DOM-MINOR",
        "title": "Formularios de permisos de obras menores",
        "publisher": "Ministerio de Vivienda y Urbanismo de Chile",
        "url": "https://www.minvu.gob.cl/elementos-tecnicos/formularios/formularios-de-permisos-de-obra-menor/",
        "scope": "listado oficial de ampliación hasta 100 m², modificaciones y regímenes especiales, con referencias a OGUC 5.1.4 y LGUC 166",
        "support": "diferencia solicitudes, declaraciones juradas, modificaciones y recepción de categorías de obra menor",
        "limit": "la superficie no concede exención automática; ruralidad, copropiedad, patrimonio, riesgo, estructura y otras leyes pueden cambiar el expediente",
    },
    {
        "id": "CL-DOM-BUILD",
        "title": "Formularios de obras de edificación",
        "publisher": "Ministerio de Vivienda y Urbanismo de Chile",
        "url": "https://www.minvu.gob.cl/elementos-tecnicos/formularios/formularios-de-permisos-de-edificacion/",
        "scope": "listado oficial de obra nueva, ampliación mayor a 100 m², alteración, reparación y reconstrucción",
        "support": "ubica solicitudes de anteproyecto, permiso, modificación, recepción y comprobantes de declaraciones juradas",
        "limit": "la selección final depende del régimen vigente y de la clasificación realizada con profesional competente y DOM",
    },
    {
        "id": "CL-CIP",
        "title": "Formularios de certificados y Certificado de Informaciones Previas",
        "publisher": "Ministerio de Vivienda y Urbanismo de Chile",
        "url": "https://www.minvu.gob.cl/elementos-tecnicos/formularios/0-certificados-y-otros/",
        "scope": "solicitud y formato oficial de CIP, certificados de número, afectación y copropiedad disponibles",
        "support": "identifica la familia documental para solicitar y registrar información normativa del predio",
        "limit": "el ejemplo educativo no es un certificado emitido, no fija deslindes y no reemplaza lectura profesional del instrumento territorial",
    },
    {
        "id": "CL-SEC",
        "title": "e-Declarador SEC",
        "publisher": "Superintendencia de Electricidad y Combustibles de Chile",
        "url": "https://www.sec.cl/e-declarador/",
        "scope": "servicio oficial y descripción de TE1 para instalaciones eléctricas interiores y TC6 para instalaciones interiores de gas",
        "support": "confirma que e-Declarador está dirigido a instaladores y profesionales autorizados y localiza los trámites aplicables",
        "limit": "la mención de TE1 o TC6 no determina que ambos correspondan en todo proyecto ni habilita al propietario para diseñar, ejecutar o declarar la instalación",
    },
    {
        "id": "CL-THERMAL",
        "title": "Nueva Reglamentación Térmica",
        "publisher": "Ministerio de Vivienda y Urbanismo de Chile",
        "url": "https://www.minvu.gob.cl/nueva-reglamentacion-termica/",
        "scope": "resumen oficial de la modificación del artículo 4.1.10 OGUC publicada el 27 de mayo de 2024 y vigente desde el 28 de noviembre de 2025",
        "support": "documenta nueve zonas y nuevas exigencias de envolvente, ventanas, puertas, sobrecimientos y condensación",
        "limit": "la página de síntesis no sustituye el texto normativo, sus transitorios, la zonificación del predio ni el cálculo del proyecto",
    },
]


def source_block(source: dict) -> str:
    return f"""### [[{source['id']}]] {source['title']}

{source['publisher']}. [{source['url']}]({source['url']})

**Consulta:** {source['scope']}. **Apoyo:** {source['support']}. **Límite:** {source['limit']}. **Fecha de consulta:** {CONSULTED}."""


def lesson_markdown(number: int, spec: dict) -> str:
    part = (number - 1) // 10 + 1
    position = (number - 1) % 10 + 1
    class_id = f"ARQ-{number:03d}"
    previous = f"ARQ-{number - 1:03d}"
    following = f"ARQ-{number + 1:03d}" if number < 830 else "RUTA-34 y EST-06"
    part_title, purpose, product = PART_DEFINITIONS[part]
    steps = spec["focus"]
    graph_nodes = [chr(ord("A") + index) for index in range(len(steps))]
    graph = ["flowchart TD"]
    for index, label in enumerate(steps):
        graph.append(f'    {graph_nodes[index]}["{label}"]')
        if index:
            graph.append(f"    {graph_nodes[index - 1]} --> {graph_nodes[index]}")
    graph.append(f'    {graph_nodes[-1]} --> Z["Evidencia · {spec["evidence"]}"]')
    graph.append(f'    X["Condición crítica · {spec["critical"]}"] --> {graph_nodes[-1]}')
    prereqs = ", ".join(f"`{item}`" for item in spec["prereqs"])

    development = []
    for index, focus in enumerate(steps, 1):
        before = steps[index - 2] if index > 1 else "el encargo y los antecedentes disponibles"
        after = steps[index] if index < len(steps) else "la evidencia verificable"
        development.append(
            f"""### {index}. {focus.capitalize()}

En **{class_id}**, {focus} se trabaja como una operación comprobable y no como una etiqueta. La entrada es {before}; se anotan origen, fecha, responsable, unidad y estado de cada dato. Después se ejecuta una comparación o verificación visible y se entrega una salida utilizable por {after}. Cuando falta información se escribe `PENDIENTE` junto con quién puede resolverla y qué decisión permanece detenida. Este tratamiento impide que una ausencia adopte el valor cero o que una hipótesis se vuelva requisito por repetición.

La revisión de {focus} conserva al menos dos alternativas con el mismo alcance. Se comprueba qué cambia en plazo, costo, seguridad, habitabilidad, permiso, construcción y mantenimiento. Una ventaja no compensa una condición crítica: si **{spec['critical']}**, la decisión se reabre aunque la opción parezca económica o rápida. La comparación debe permitir que otra persona repita el razonamiento sin depender de una explicación oral del autor.

El propietario puede organizar documentos, formular preguntas, comparar ofertas y observar si la evidencia prometida existe. No puede asumir por ello atribuciones de arquitectura, cálculo, construcción, prevención o instalaciones reguladas. En {focus}, la entrega debe indicar quién propone, quién revisa, quién autoriza, quién ejecuta y quién conserva el registro. Esa asignación forma parte del aprendizaje porque una tarea técnicamente correcta sin responsable o versión sigue siendo incontrolable.
"""
        )

    case_table = "\n".join(
        [
            "| Variable | CASA-NUEVA-80 | AMPLIACION-24 | Comprobación antes de usar |",
            "|---|---|---|---|",
            f"| Punto de partida | Terreno hipotético urbanizado; comuna, CIP y servicios por verificar | Vivienda existente ocupada; permiso, recepción, estructura y redes por verificar | Antecedente fechado y responsable competente |",
            f"| Aplicación de {steps[0]} | Se documenta desde cero y se coordina con el predio | Se compara existente / propuesto sin asumir legalidad previa | Registro de dato, hipótesis y discrepancia |",
            "| Escenario económico | Prioriza suficiencia y simplicidad, sin rebajar condiciones críticas | Reduce intervención y reposición, sin improvisar conexiones | Alcance igual o diferencias expresas |",
            "| Escenario estándar | Equilibra inversión inicial, durabilidad y mantenimiento | Coordina encuentros y continuidad de uso | Cotizaciones equivalentes y fecha |",
            "| Mayor desempeño | Mejora envolvente, control, durabilidad o mantenibilidad demostrable | Mejora el conjunto sin trasladar patologías a lo existente | Métrica, ensayo o criterio verificable |",
            "| Contingencia didáctica | 10 %, 15 % y 20 % como sensibilidad, no tarifa universal | 10 %, 15 % y 20 %, con mayor atención a condiciones ocultas | Fórmula separada del costo base |",
            "| Puerta de detención | Falta de factibilidad, permiso, competencia o financiamiento | Daño, incompatibilidad, ocupación insegura o antecedente histórico no resuelto | Acta GO / REDISEÑAR / DETENER |",
        ]
    )

    errors = "\n".join(
        [
            f"- **Cerrar demasiado pronto:** en {class_id}, una apariencia convincente no demuestra {steps[-1]}. Vuelve al primer dato sin origen o al primer cambio sin autorización.",
            f"- **Copiar el caso trabajado:** las superficies 80 m² y 24 m² son hipótesis didácticas. Repite {steps[0]} y {steps[1]} para otro predio antes de transferir el método.",
            f"- **Mezclar presupuesto y caja:** el costo total, el compromiso, el pago y el financiamiento disponible son estados distintos. Registra fecha y base de cada uno.",
            f"- **Usar IA como autoridad:** una salida de IA puede ordenar preguntas o detectar omisiones, pero no firma, calcula, inspecciona, declara ni autoriza {spec['title'].lower()}.",
            f"- **Perder la versión:** una cotización, plano, formulario o instrucción sin revisión y fecha puede corresponder a otro alcance. Conserva reemplazos y deja obsoletos visibles.",
            f"- **Normalizar un peligro:** {spec['critical'].capitalize()}. Detén la actividad y deriva la decisión a la persona competente.",
        ]
    )

    checklist = "\n".join(
        f"- [ ] {item.capitalize()}: dato, fuente, fecha, responsable, alternativa y condición de revisión." for item in steps
    )

    return f"""# {class_id} · {spec['title']}

**Parte {part:02d} · Aplicación para propietarios · Chile · Edición 2026.10.**

Material educativo. Enseña a organizar, contratar, comparar y verificar; no entrega licencia, firma, cálculo, dirección, autorización ni inspección profesional. Toda aplicación real debe revalidarse para región, comuna, predio, fecha, actuación y condiciones de la obra.

**Prerrequisitos recomendados:** {prereqs}. La entrada inmediata es `{previous}`; la continuidad es `{following}`.

## Pregunta central

¿Cómo puede una persona propietaria abordar **{spec['title'].lower()}**, producir {spec['evidence']} y demostrar que {spec['critical']}?

**Fallo crítico de esta clase:** {spec['critical']}.

## Problema y resultado observable

Esta clase existe porque el conocimiento disciplinar ya cubierto en {prereqs} no forma por sí solo una secuencia doméstica de decisión. Dentro de **{part_title}**, la tarea es {purpose}. El lector no ejecuta trabajos reservados o peligrosos: construye un expediente que permita contratar, preguntar, comparar, detener y exigir evidencia.

Al terminar podrás identificar entradas y desconocidos, separar requisito de preferencia, comparar tres escenarios, asignar responsabilidades y producir **{spec['evidence']}**. La entrega se incorpora al **{product}** y debe poder ser revisada sin explicación oral adicional.

## Lectura de antecedentes y vocabulario

Lee primero el documento que posee autoridad: certificado, permiso, plano aprobado, especificación, cotización, contrato, acta o informe. Registra emisor, destinatario, predio, fecha, revisión, alcance y anexos. Después compara el documento con la realidad observable sin corregirlo silenciosamente. Una discrepancia se convierte en pregunta y responsable, no en una cifra inventada.

En esta clase, **requisito confirmado** significa que existe una fuente competente vigente y aplicable al caso; **verificar en DOM / especialista** significa que la clasificación o solución depende de autoridad o competencia; **supuesto didáctico** permite calcular o comparar dentro del ejercicio, pero no viajar a una obra real. **Precio de catálogo**, **precio cotizado**, **precio pagado** y **estimación** se registran por separado.

Para cualquier documento de costo se usa CLP como moneda de registro. Si se añade UF, debe conservar fecha de valor y fuente oficial. El IVA se mantiene como campo configurable porque la base, inclusión y tratamiento dependen del documento. La sensibilidad de 10 % a 20 % es una hipótesis pedagógica y nunca una tarifa, garantía o sustituto de estudiar riesgos.

## Desarrollo paso a paso

{''.join(development)}

## Mapa específico de la decisión

```mermaid
{chr(10).join(graph)}
```

El diagrama no representa una secuencia ejecutiva de construcción. Permite localizar dónde falta evidencia o autoridad en **{spec['title'].lower()}**. La flecha de condición crítica entra antes del cierre para que pueda detener el proceso.

## Aplicación al caso CASA-NUEVA-80

**Estado del caso:** supuesto didáctico. {spec['new_case']} La localización, la comuna, el instrumento territorial, el CIP, el suelo, los servicios y los precios deben reemplazarse por antecedentes reales antes de cualquier decisión.

El expediente aplica {steps[0]}, {steps[1]} y {steps[2]} sobre una vivienda nueva de 80 m². El escenario económico conserva la misma necesidad con soluciones simples; el estándar equilibra inversión, durabilidad y mantenimiento; el de mayor desempeño justifica cada incremento mediante una métrica o evidencia. Ninguno puede rebajar permiso, estabilidad, seguridad, salubridad o responsabilidades.

El propietario prepara preguntas, ordena documentos y comprueba que las alternativas sean comparables. El arquitecto y los especialistas desarrollan y suscriben los proyectos de su competencia; la DOM y otros organismos actúan dentro de sus atribuciones. Si una respuesta altera el alcance, se actualizan cantidades, presupuesto, cronograma y versión del expediente.

## Aplicación al caso AMPLIACION-24

**Estado del caso:** supuesto didáctico. {spec['extension_case']} Se distingue siempre la ampliación de un nivel de la hipótesis de segundo piso; esta última no contiene instrucciones de refuerzo y queda detenida hasta diagnóstico y proyecto estructural profesional.

La aplicación debe considerar construcción adosada, compatibilidad con la estructura existente, techumbre y evacuación de aguas, medianeros, humedad, redes activas, residentes, polvo, ruido, cortes, demolición selectiva y recuperación de terminaciones. Permiso y recepción históricos son antecedentes a comprobar: que la vivienda exista o figure en una cotización no demuestra su legalidad.

Cuando un recinto existente pasa a cocina, baño o dormitorio, se revisan uso, habitabilidad, ventilación, instalaciones, estructura, accesibilidad y autorización. Las bifurcaciones rural, zona de riesgo, patrimonio y copropiedad se registran como consultas específicas; no se fuerza un único procedimiento ni costo.

## Comparación de los dos expedientes

{case_table}

La tabla conserva el mismo método, pero no iguala parámetros. La ampliación puede costar más por metro cuadrado por protección, demoliciones, encuentros, baja escala y trabajo con redes o residentes. La casa nueva puede concentrar mayores costos exteriores, urbanización, estudios y habilitaciones. Cualquier cifra requiere fuente, fecha, unidad, IVA, transporte, stock y alcance.

## Caso numérico y práctica guiada

{spec['guided']}

Trabaja en una hoja que conserve fórmula y unidades. Realiza una segunda comprobación independiente: suma por capítulos frente a suma por partidas, cantidad geométrica frente a compra, o presupuesto frente a flujo, según corresponda. Redondea solo al final y explica el criterio. Si falta un precio real, escribe `HIPOTÉTICO` y deja una celda editable para cotización local.

La práctica se completa en cuatro rondas. Primero registra datos y desconocidos. Después construye tres alternativas equivalentes o declara sus diferencias. Luego pide a otra persona que reconstruya una operación y ubique el punto de detención. Finalmente corrige la entrega y conserva ambas versiones con la objeción que produjo el cambio.

## Uso permitido de IA y verificación independiente

La IA puede convertir necesidades en checklist, explicar vocabulario, comparar exclusiones, buscar inconsistencias entre versiones y redactar preguntas para la DOM o profesionales. En {class_id}, guarda instrucción, salida original, revisión humana, fuente contrastada y cambio realizado. No uses una respuesta generada como precio vigente, permiso, dimensionamiento, criterio de seguridad, declaración TE1/TC6, certificado o aceptación de obra.

Verifica de forma independiente números, unidades y citas. Un cálculo simple se repite con otra fórmula o suma manual; un requisito se contrasta con la fuente oficial y el expediente específico; una decisión técnica se remite al profesional competente. Si la respuesta de IA contradice una fuente o no puede citarla, queda como pregunta y no como conclusión.

## Ejercicio independiente

Aplica el método a un tercer caso: una reparación o ampliación de superficie distinta en otra comuna hipotética. Produce {spec['evidence']}. Cambia al menos dos supuestos y muestra qué celdas, documentos y decisiones deben revisarse. Incluye una alternativa que se detenga por falta de evidencia y explica por qué no puede rescatarse mediante un promedio.

Entrega un índice de archivos, una página de síntesis y los anexos necesarios. Otra persona debe localizar la fuente de una afirmación, repetir una operación, distinguir lo confirmado de lo supuesto y saber quién debe resolver cada pendiente. No se evalúa la apariencia si la cadena documental está rota.

## Errores típicos y recuperación

{errors}

Para recuperar, vuelve al expediente después de 24–48 horas. Reconstruye de memoria **{' → '.join(steps)}** y compáralo con la versión guardada. Corrige una unidad, una responsabilidad y una condición de detención. Después transfiere el método entre CASA-NUEVA-80 y AMPLIACION-24 sin copiar sus cifras.

## Evaluación por evidencias

La entrega se acepta cuando responde la pregunta central, contiene {spec['evidence']}, distingue confirmado / verificar / supuesto, compara escenarios con fronteras explícitas y permite repetir al menos una operación. Debe asignar responsables, registrar fuente y fecha, conservar una revisión sustantiva y demostrar que **{spec['critical']}**.

Se usa la rúbrica común, con umbral 80/100 y ninguna dimensión bajo 60 %. Sin embargo, una condición crítica de permiso, estructura, instalación, seguridad, salubridad o financiamiento mantiene la evidencia pendiente aunque el promedio supere el umbral.

## Checklist de aprobación

{checklist}
- [ ] CASA-NUEVA-80 y AMPLIACION-24 tienen aplicaciones separadas y trazables.
- [ ] Los tres escenarios conservan alcance comparable o declaran diferencias.
- [ ] Todo precio es cotizado con fecha y fuente o está marcado HIPOTÉTICO.
- [ ] El expediente conserva versiones, objeciones, responsables y condición de reapertura.
- [ ] Ninguna actividad atribuye al propietario una firma, cálculo, instalación o autorización profesional.

## Continuidad

`{following}` recibe la evidencia de esta clase, no sus cifras. El siguiente paso debe volver a comprobar predio, fecha, versión, alcance y responsable. Si una condición nueva invalida {steps[-1]}, el expediente vuelve al punto correspondiente y registra el cambio.

## Fuentes y alcance de uso

{chr(10).join(source_block(source) + chr(10) for source in SOURCES)}
"""


def update_manifests() -> None:
    program = json.loads(PROGRAM.read_text(encoding="utf-8"))
    program["class_count"] = 830
    program["part_count"] = 83
    program["route_count"] = 34
    phases = [phase for phase in program["phases"] if phase["id"] != "IV"]
    phases.append(
        {
            "id": "IV",
            "title": "aplicación práctica para propietarios",
            "first_part": 81,
            "last_part": 83,
            "first_class": "ARQ-801",
            "last_class": "ARQ-830",
        }
    )
    program["phases"] = phases
    PROGRAM.write_text(json.dumps(program, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    parts = json.loads(PARTS.read_text(encoding="utf-8"))
    parts["parts"] = [item for item in parts["parts"] if item["number"] <= 80]
    parts["parts"].extend(
        {"number": number, "title": values[0]} for number, values in PART_DEFINITIONS.items()
    )
    PARTS.write_text(json.dumps(parts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    catalog = [item for item in catalog if int(item["id"][4:]) <= 800]
    for offset, spec in enumerate(LESSONS, 801):
        part = (offset - 1) // 10 + 1
        catalog.append(
            {
                "id": f"ARQ-{offset:03d}",
                "title": spec["title"],
                "part": part,
                "is_new": True,
                "source": f"classes/parte-{part:02d}/ARQ-{offset:03d}.md",
            }
        )
    CATALOG.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    pedagogy = json.loads(PEDAGOGY.read_text(encoding="utf-8"))
    for studio in pedagogy["studios"]:
        studio["route_ids"] = [route_id for route_id in studio["route_ids"] if route_id != "RUTA-34"]
        if studio["id"] in {"EST-03", "EST-06"}:
            studio["route_ids"].append("RUTA-34")
    pedagogy["routes"] = [route for route in pedagogy["routes"] if route["id"] != "RUTA-34"]
    pedagogy["routes"].append(
        {
            "id": "RUTA-34",
            "title": "Vivienda propia y ampliación para propietarios",
            "parts": [3, 11, 15, 19, 20, 21, 27, 28, 31, 32, 33, 34, 35, 39, 40, 41, 42, 43, 49, 81, 82, 83],
            "entry": "Para personas propietarias sin formación técnica. Diagnóstico inicial de lectura de planos, unidades, porcentajes, seguridad y capacidad de distinguir dato, hipótesis, requisito y decisión profesional.",
            "exit": "Organizar y defender dos expedientes educativos —CASA-NUEVA-80 y AMPLIACION-24— desde factibilidad hasta recepción y mantenimiento, con costos, permisos, responsabilidades y límites verificables.",
            "capstone": "EST-06",
            "class_sequence": [f"ARQ-{number:03d}" for number in range(801, 831)],
            "case_files": ["cases/CASA-NUEVA-80.md", "cases/AMPLIACION-24.md"],
            "formal_checkpoints": [
                "ARQ-810 · puerta GO / REDISEÑAR / DETENER",
                "ARQ-820 · puerta NO INICIAR SIN HABILITACIONES",
                "ARQ-830 · auditoría de cierre y mantenimiento",
            ],
            "activity_boundary": "Las actividades son simulaciones de gestión y revisión. El propietario puede organizar antecedentes, registrar observaciones y comparar ofertas; proyectos, cálculos, instalaciones, firmas, inspecciones y autorizaciones corresponden a profesionales, instaladores u organismos competentes cuando la normativa lo exige.",
        }
    )
    PEDAGOGY.write_text(json.dumps(pedagogy, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="Rewrite ARQ-801..830 from this authored source")
    args = parser.parse_args()
    if len(LESSONS) != 30:
        raise SystemExit("The homeowner expansion must define exactly 30 lessons")
    for number, spec in enumerate(LESSONS, 801):
        part = (number - 1) // 10 + 1
        path = ROOT / "classes" / f"parte-{part:02d}" / f"ARQ-{number:03d}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists() and not args.refresh:
            raise SystemExit(f"Refusing to overwrite {path.relative_to(ROOT)} without --refresh")
        path.write_text(lesson_markdown(number, spec).rstrip() + "\n", encoding="utf-8", newline="\n")
    update_manifests()
    print("Authored ARQ-801..830, Parts 81..83 and RUTA-34 canonical metadata")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
