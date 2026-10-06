#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Create the reviewed Phase III source lessons without touching ARQ-001..680.

The expansion is deliberately data driven.  Re-running the script is idempotent:
it refuses to replace an existing Phase III lesson whose content differs from the
generated source, and it preserves the complete historical curriculum.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "catalog.json"

SOURCES = {
    "UIA": (
        "UNESCO–UIA Charter for Architectural Education, revisión 2026",
        "Unión Internacional de Arquitectos",
        "https://www.uia-architectes.org/en/news/unesco-uia-charter-for-architectural-education-revised-edition-2026/",
        "Amplitud formativa, juicio profesional y relación entre diseño, técnica, sociedad y ambiente.",
        "Noticia y materiales públicos de la revisión; no acredita este programa ni sustituye el texto íntegro de la Carta.",
    ),
    "GOV-RESEARCH": (
        "Using moderated usability testing",
        "Government Digital Service, Reino Unido",
        "https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing",
        "Planificación de pruebas con personas, observación y registro de hallazgos.",
        "Guía de servicios digitales transferida como método; no constituye protocolo clínico ni normativa chilena.",
    ),
    "RIBA-PLAN": (
        "RIBA Plan of Work 2020",
        "Royal Institute of British Architects",
        "https://www.riba.org/work/insights-and-resources/riba-plan-of-work/",
        "Etapas, intercambios de información, estrategias y responsabilidades durante el proyecto.",
        "Marco británico usado para comparación; contratos, permisos y atribuciones deben verificarse en la jurisdicción aplicable.",
    ),
    "ARB-CONFLICT": (
        "Managing Conflicts of Interest",
        "Architects Registration Board",
        "https://arb.org.uk/wp-content/uploads/Conflict-of-Interest-guidance-document.pdf",
        "Identificación, comunicación y gestión documentada de conflictos de interés.",
        "Guía profesional británica; no sustituye deberes legales, contractuales ni éticos vigentes en Chile.",
    ),
    "NPS-DOC": (
        "Heritage Documentation Programs — Documentation Guidelines",
        "U.S. National Park Service",
        "https://www.nps.gov/subjects/heritagedocumentation/guidelines.htm",
        "Principios de levantamiento, dibujo, fotografía y archivo de documentación patrimonial.",
        "Guía estadounidense; su método no convierte una representación en levantamiento certificado ni autorización de intervención.",
    ),
    "WCAG": (
        "Web Content Accessibility Guidelines 2.2",
        "World Wide Web Consortium",
        "https://www.w3.org/TR/WCAG22/",
        "Criterios públicos para contenido digital perceptible, operable, comprensible y robusto.",
        "Se aplica a productos digitales; no reemplaza requisitos espaciales, sensoriales o de evacuación del entorno construido.",
    ),
    "IFC": (
        "Industry Foundation Classes: IFC 4.3 / ISO 16739-1:2024",
        "buildingSMART International",
        "https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/",
        "Estructura abierta de intercambio de información para activos construidos.",
        "La existencia del estándar no garantiza interoperabilidad, calidad semántica ni adecuación del modelo a un uso concreto.",
    ),
    "NASA-VERIFY": (
        "NASA Systems Engineering Handbook: Product Realization",
        "National Aeronautics and Space Administration",
        "https://www.nasa.gov/reference/5-0-product-realization/",
        "Distinción entre verificación, validación, requisitos, producto y uso previsto.",
        "Método de ingeniería de sistemas transferido con límites; no valida automáticamente un edificio o una simulación.",
    ),
    "NIST-AI": (
        "Artificial Intelligence Risk Management Framework 1.0",
        "National Institute of Standards and Technology",
        "https://www.nist.gov/itl/ai-risk-management-framework",
        "Gobernar, mapear, medir y gestionar riesgos de sistemas de inteligencia artificial.",
        "Marco voluntario y general; no certifica herramientas, resultados ni cumplimiento sectorial o local.",
    ),
    "NIST-OT": (
        "NIST SP 800-82 Revision 3: Guide to Operational Technology Security",
        "National Institute of Standards and Technology",
        "https://csrc.nist.gov/pubs/sp/800/82/r3/final",
        "Riesgos y controles para tecnología operacional y sistemas ciberfísicos.",
        "Guía estadounidense de ciberseguridad; debe adaptarse al activo, amenaza, contrato y regulación aplicables.",
    ),
    "NIST-AM": (
        "What is Additive Manufacturing?",
        "National Institute of Standards and Technology",
        "https://www.nist.gov/additive-manufacturing/what-additive-manufacturing",
        "Definición y principios de fabricación aditiva como proceso por capas desde datos digitales.",
        "La descripción general no demuestra aptitud estructural, durabilidad, certificación ni escala edificatoria.",
    ),
    "OSHA-ROBOT": (
        "Robotics — Overview",
        "Occupational Safety and Health Administration",
        "https://www.osha.gov/robotics",
        "Reconocimiento de peligros y responsabilidades alrededor de robots y sistemas automatizados.",
        "Referencia laboral estadounidense; no reemplaza evaluación de riesgos, normativa local ni instrucciones del fabricante.",
    ),
    "UNHAB-CITIES": (
        "World Cities Report 2024: Cities and Climate Action",
        "UN-Habitat",
        "https://unhabitat.org/world-cities-report-2024-cities-and-climate-action",
        "Relación entre urbanización, desigualdad, acción climática, vivienda e infraestructura.",
        "Informe global; sus tendencias no sustituyen datos locales, participación ni instrumentos territoriales vigentes.",
    ),
    "CL-LGUC": (
        "Ley General de Urbanismo y Construcciones — texto consolidado",
        "Biblioteca del Congreso Nacional de Chile",
        "https://www.bcn.cl/leychile/navegar?idNorma=13560",
        "Marco legal chileno para planificación urbana, urbanización y construcción.",
        "Debe comprobarse texto vigente, aplicabilidad, reglamentos, instrumentos y pronunciamientos para cada caso real.",
    ),
    "UNDRR-INFRA": (
        "Hoja de Ruta para la Resiliencia de la Infraestructura en la República de Chile",
        "Oficina de las Naciones Unidas para la Reducción del Riesgo de Desastres",
        "https://www.undrr.org/es/publication/hoja-de-ruta-para-la-resiliencia-de-la-infraestructura-en-la-republica-de-chile",
        "Dependencias, gobernanza y continuidad de servicios de infraestructura en Chile.",
        "Hoja de ruta estratégica; no reemplaza diseño de ingeniería, evaluación de amenaza ni decisión de autoridad.",
    ),
    "EPA-GI": (
        "Green Infrastructure Planning, Design, and Implementation",
        "U.S. Environmental Protection Agency",
        "https://www.epa.gov/green-infrastructure/green-infrastructure-planning-design-and-implementation",
        "Planificación, diseño e implementación de infraestructura verde para gestión de agua.",
        "Referencia estadounidense; clima, suelo, operación, permisos y desempeño deben verificarse localmente.",
    ),
    "ISO-ADAPT": (
        "ISO 14090:2019 — Adaptation to climate change",
        "International Organization for Standardization",
        "https://www.iso.org/standard/68507.html",
        "Principios, requisitos y directrices públicas de adaptación al cambio climático.",
        "La ficha pública confirma alcance y edición; no equivale a lectura íntegra, certificación ni solución de proyecto.",
    ),
    "ISO-LCA": (
        "ISO 14040:2006 — Life cycle assessment: principles and framework",
        "International Organization for Standardization",
        "https://www.iso.org/standard/37456.html",
        "Estructura conceptual de objetivo, alcance, inventario, evaluación e interpretación del ciclo de vida.",
        "La ficha pública no entrega todos los requisitos ni valida inventarios, factores o comparaciones del ejercicio.",
    ),
    "NPS-REHAB": (
        "Standards for Rehabilitation",
        "U.S. National Park Service",
        "https://www.nps.gov/articles/000/treatment-standards-rehabilitation.htm",
        "Principios de rehabilitación, compatibilidad, conservación y reconocimiento de cambios históricos.",
        "Criterios estadounidenses usados para comparación; no sustituyen protección patrimonial ni permisos en Chile.",
    ),
    "NPS-HSR": (
        "Preservation Brief 43 — Historic Structure Reports",
        "U.S. National Park Service",
        "https://www.nps.gov/orgs/1739/upload/preservation-brief-43-historic-structure-reports.pdf",
        "Investigación, documentación, diagnóstico y planificación de intervenciones en edificios históricos.",
        "Guía metodológica; no autoriza intervención ni reemplaza especialistas, ensayos o normativa aplicable.",
    ),
    "WHO-AGE": (
        "Global age-friendly cities: a guide",
        "World Health Organization",
        "https://www.who.int/publications/i/item/9789241547307",
        "Participación de personas mayores y dimensiones de entornos favorables al envejecimiento.",
        "Guía global; no representa por sí sola a una comunidad ni fija parámetros dimensionales locales.",
    ),
    "WHO-HOUSING": (
        "WHO Housing and health guidelines",
        "World Health Organization",
        "https://www.who.int/publications/i/item/9789241550376",
        "Relación entre condiciones de vivienda y resultados relevantes para la salud.",
        "Guía sanitaria global; no reemplaza diagnóstico, norma de edificación ni evaluación específica de un hogar.",
    ),
    "NASA-MOON": (
        "Moon Base Systems",
        "National Aeronautics and Space Administration",
        "https://www.nasa.gov/moonbase-systems/",
        "Arquitectura de sistemas, operaciones, logística, autonomía y desafíos ambientales para presencia lunar sostenida.",
        "Material de programa espacial; se estudia como caso avanzado y no desplaza competencias terrestres fundamentales.",
    ),
    "UNDRR-RISK": (
        "Disaster risk terminology",
        "Oficina de las Naciones Unidas para la Reducción del Riesgo de Desastres",
        "https://www.undrr.org/terminology/disaster-risk",
        "Vocabulario de amenaza, exposición, vulnerabilidad y capacidad.",
        "La terminología ordena el análisis; no produce por sí sola un mapa, cálculo o certificación de seguridad.",
    ),
}


PARTS = [
    (69, "Investigación avanzada, evidencia y tesis", "formular conocimiento arquitectónico reproducible sin confundir evidencia, interpretación y opinión", "protocolo de investigación y capítulo de tesis auditable", ("UIA", "GOV-RESEARCH"), [
        "Preguntas investigables y problemas de arquitectura", "Hipótesis, proposiciones y preguntas abiertas", "Revisión bibliográfica y búsqueda sistemática", "Fuentes primarias, secundarias y cadenas de citación", "Métodos cualitativos: observación, entrevista y codificación", "Métodos cuantitativos: muestra, medición y estadística", "Métodos mixtos y triangulación", "Estudios de caso y comparación responsable", "Reproducibilidad, datos, ética y consentimiento", "Tesis: argumento, método, resultados y defensa",
    ]),
    (70, "Práctica profesional, oficina, negocio y negociación", "gestionar encargos, relaciones, riesgos y recursos sin ocultar responsabilidades ni conflictos", "plan de práctica profesional con alcance, honorarios, riesgos y control documental", ("RIBA-PLAN", "ARB-CONFLICT"), [
        "Modelos de práctica y propósito de una oficina", "Brief comercial, propuesta y selección de encargos", "Honorarios, alcance, exclusiones y cambios", "Contratos, seguros y distribución de responsabilidades", "Clientes, usuarios, mandantes y gobernanza", "Negociación basada en intereses y registro de acuerdos", "Marketing profesional, reputación y límites éticos", "Finanzas de oficina, flujo de caja y capacidad", "Liderazgo, equipos, bienestar y aprendizaje", "Simulación de encargo: propuesta, reunión y cierre",
    ]),
    (71, "Representación avanzada, narrativa y experiencias inmersivas", "comunicar espacio, tiempo, incertidumbre y decisiones a audiencias distintas mediante medios verificables y accesibles", "relato multiformato con planos, sección, datos, interacción y versión accesible", ("NPS-DOC", "WCAG"), [
        "Dibujo analítico y selección de punto de vista", "Sección narrativa y secuencias de recorrido", "Collage, montaje y procedencia de imágenes", "Fotografía arquitectónica y sesgos de encuadre", "Visualización de datos espaciales y escalas", "Storytelling para crítica, comunidad y cliente", "Animación, tiempo y estados operativos", "Realidad aumentada y superposición situada", "Realidad virtual, presencia y pruebas de uso", "Publicación accesible y portafolio multiformato",
    ]),
    (72, "Programación, geometría y diseño computacional", "transformar reglas de diseño en modelos legibles, comprobables y transferibles sin delegar el juicio", "modelo paramétrico versionado con pruebas, sensibilidad y alternativas", ("IFC", "NASA-VERIFY"), [
        "Pensamiento algorítmico para proyectistas", "Datos, tipos, unidades y estructuras", "Coordenadas, vectores, matrices y transformaciones", "Curvas, superficies, mallas y tolerancias", "Parametrización y dependencias del modelo", "Scripting para automatizar tareas repetibles", "Diseño generativo y espacio de soluciones", "Optimización multiobjetivo y frentes de Pareto", "Pruebas, versiones y reproducibilidad del código", "Proyecto computacional: regla, modelo y fabricación",
    ]),
    (73, "Inteligencia artificial aplicada al ciclo de vida", "usar IA como sistema sujeto a propósito, procedencia, evaluación y supervisión humana en cada fase del activo", "expediente de IA con datos, riesgos, pruebas, revisión humana y criterio de retiro", ("NIST-AI", "NIST-OT"), [
        "Cartografía de usos de IA y decisiones indelegables", "Datos de entrenamiento, procedencia y representatividad", "Ideación y generación de alternativas con restricciones", "Análisis de sitio y visión computacional", "Distribución espacial, optimización y explicabilidad", "IA en BIM, planos y detección de inconsistencias", "IA en costos, planificación y control de obra", "IA en operación, mantenimiento y gemelos digitales", "Sesgos, copyright, privacidad y seguridad", "Auditoría profesional: IA frente a análisis independiente",
    ]),
    (74, "Captura digital, fabricación avanzada y robótica", "conectar medición, modelo, máquina, tolerancia, seguridad y control de calidad en procesos físicos digitales", "prototipo fabricable con cadena de datos, riesgos, tolerancias e inspección", ("NIST-AM", "OSHA-ROBOT"), [
        "Drones: planificación, captura, permisos y seguridad", "LiDAR: nubes de puntos, densidad y oclusiones", "Escaneo 3D y registro de múltiples estaciones", "Fotogrametría avanzada y control de calidad", "Del levantamiento al modelo semántico", "Corte láser, CNC y preparación de archivos", "Impresión 3D: proceso, orientación y soportes", "Fabricación aditiva a escala edilicia", "Robótica de obra y zonas de interacción", "Prototipo 1:1: fabricar, medir, corregir y documentar",
    ]),
    (75, "Política urbana, datos, vivienda y justicia espacial", "relacionar decisiones espaciales con instituciones, mercados, derechos y experiencias sin reducir la ciudad a indicadores", "diagnóstico urbano con datos, participación, alternativas y efectos distributivos", ("UNHAB-CITIES", "CL-LGUC"), [
        "Gobernanza urbana, poder y derecho a la ciudad", "Política de suelo, captura de valor y regulación", "Mercados de vivienda, arriendo y asequibilidad", "Campamentos, informalidad y seguridad de tenencia", "Segregación, gentrificación y desplazamiento", "Género, cuidados y movilidad cotidiana", "Migración, interculturalidad y acceso a servicios", "Datos urbanos, privacidad y sesgos de medición", "Participación vinculante y resolución de conflictos", "Plan urbano: escenarios, inversión y evaluación distributiva",
    ]),
    (76, "Redes territoriales e infraestructura pública", "leer infraestructuras como servicios interdependientes que articulan territorio, operación, mantenimiento y equidad", "estrategia territorial de servicio con dependencias, fases y continuidad", ("UNDRR-INFRA", "EPA-GI"), [
        "Sistemas de infraestructura y niveles de servicio", "Calles completas, jerarquía vial y seguridad", "Carreteras, autopistas y relación con asentamientos", "Ferrocarriles regionales y logística territorial", "Represas, embalses y decisiones socioambientales", "Abastecimiento, saneamiento y drenaje a escala territorial", "Energía, almacenamiento y generación distribuida", "Residuos, recuperación de recursos y localización", "Telecomunicaciones e infraestructura digital", "Plan integrado de redes y continuidad regional",
    ]),
    (77, "Adaptación climática, regeneración y materiales emergentes", "diseñar transiciones ambientales que declaren fronteras, desempeño, incertidumbre y justicia entre generaciones", "estrategia regenerativa con escenarios climáticos, balances y verificación posocupacional", ("ISO-ADAPT", "ISO-LCA"), [
        "Adaptación climática basada en escenarios", "Desempeño pasivo bajo clima futuro", "Net-zero: alcance, balance y tiempo", "Carbono incorporado, biogénico y almacenamiento", "Economía circular a escala de edificio y ciudad", "Biomateriales y materiales biofabricados", "Materiales inteligentes, sensores y respuesta", "Nanotecnología: prestaciones, exposición y cautela", "Soluciones basadas en naturaleza y regeneración", "Proyecto climático: evitar, reducir, adaptar y reparar",
    ]),
    (78, "Reutilización masiva, patrimonio digital y transformación", "intervenir edificios existentes desde el conocimiento material, el valor cultural, el desempeño y el cambio de uso", "plan de transformación con diagnóstico, compatibilidad, fases y archivo digital", ("NPS-REHAB", "NPS-HSR"), [
        "Inventario de edificios existentes y potencial de reutilización", "Levantamiento histórico, archivos y arqueología arquitectónica", "Diagnóstico material y mapa de incertidumbre", "Escaneo, fotogrametría y HBIM", "Compatibilidad, reversibilidad y mínima intervención", "Refuerzo, accesibilidad e incendio en preexistencias", "Rehabilitación energética sin trasladar patologías", "Patrimonio industrial, moderno e indígena", "Deconstrucción selectiva y bancos de componentes", "Proyecto de reutilización adaptativa y seguimiento",
    ]),
    (79, "Salud, cuidados, diversidad y cambio demográfico", "proyectar entornos que sostengan capacidades diversas, redes de cuidado y salud a lo largo del tiempo", "proyecto de cuidado evaluado con personas, escenarios y cadena completa de accesibilidad", ("WHO-AGE", "WHO-HOUSING"), [
        "Envejecimiento poblacional y autonomía cotidiana", "Vivienda con apoyos y continuidad de cuidados", "Neurodiversidad, orientación y carga sensorial", "Salud mental, privacidad y espacios restaurativos", "Infancia, juego, riesgo y autonomía gradual", "Discapacidad múltiple y diseño centrado en capacidades", "Baños, higiene y cuidados dignos", "Arquitectura para personas sin hogar y transición", "Refugios, emergencia y reunificación familiar", "Proyecto intergeneracional de barrio y cuidados",
    ]),
    (80, "Entornos extremos, autonomía y proyecto interdisciplinario final", "transferir fundamentos terrestres a condiciones extremas sin convertir especulación en certeza técnica", "proyecto final interdisciplinario con misión, interfaces, pruebas, operación y defensa", ("NASA-MOON", "UNDRR-RISK"), [
        "Arquitectura en desiertos, altura y aislamiento", "Bases antárticas y logística estacional", "Arquitectura marítima y asentamientos flotantes", "Hábitats subterráneos y protección ambiental", "Construcción autónoma y mantenimiento remoto", "Sistemas cerrados de agua, aire, energía y residuos", "Hábitat lunar: misión, polvo, radiación y logística", "Hábitat marciano: demora, autonomía y reparación", "Seguridad física y ciberseguridad de edificios conectados", "Proyecto final: integrar, verificar, defender y transferir",
    ]),
]

EXTRA_STUDIOS = [
    {
        "id": "EST-09",
        "title": "Investigación, datos y prototipo avanzado",
        "checkpoint_after_part": 74,
        "purpose": "Integrar investigación, representación, código, IA, captura y fabricación en un prototipo cuya cadena de evidencia pueda auditarse.",
        "brief": "Investigar una necesidad del entorno construido, desarrollar dos alternativas y fabricar o simular un prototipo con datos, versiones, pruebas y revisión humana.",
        "product": "protocolo, conjunto de datos documentado, modelo reproducible, prototipo y registro de validación",
        "route_ids": ["RUTA-09", "RUTA-16", "RUTA-17", "RUTA-31", "RUTA-32", "RUTA-33"],
    },
    {
        "id": "EST-10",
        "title": "Proyecto interdisciplinario, especialización y transferencia",
        "checkpoint_after_part": 80,
        "purpose": "Cerrar la Fase III mediante un proyecto que conecte una especialización con el núcleo común, responsabilidades reales y aprendizaje posterior.",
        "brief": "Elegir un problema complejo, formar un mapa de actores y especialidades, comparar alternativas, verificar una interfaz crítica y defender la transferencia a otro contexto.",
        "product": "proyecto final interdisciplinario, dossier técnico, portafolio de versiones, defensa y agenda de investigación",
        "route_ids": [f"RUTA-{number:02d}" for number in range(1, 34)],
    },
]

PART_DEPTH = {
    69: {
        "lens": "pregunta, unidad de análisis, diseño de método, calidad de datos, inferencia y reproducibilidad",
        "case": "la evaluación posocupacional de un conjunto de vivienda social donde planos, entrevistas, mediciones y observaciones no coinciden",
        "evidence": "protocolo con pregunta falsable, muestra razonada, instrumento, plan de análisis, consentimiento, limitaciones y registro reproducible",
    },
    70: {
        "lens": "encargo, alcance, exclusión, honorario, autoridad, conflicto de interés, cambio y archivo contractual",
        "case": "una oficina pequeña que debe decidir si acepta un encargo con programa inestable, plazo fijo y responsabilidades mal asignadas",
        "evidence": "propuesta profesional con matriz de responsabilidades, supuestos comerciales, cambios, riesgos, minuta y criterio de aceptación del encargo",
    },
    71: {
        "lens": "audiencia, punto de vista, escala, secuencia, procedencia, accesibilidad y correspondencia entre representación y evidencia",
        "case": "la comunicación de una intervención urbana a vecinos, equipo técnico y autoridad mediante medios que deben conservar el mismo argumento",
        "evidence": "sistema multiformato con plano, sección, secuencia, dato, texto alternativo, versión de baja tecnología y prueba con usuarios",
    },
    72: {
        "lens": "dato, tipo, unidad, relación geométrica, dependencia, algoritmo, tolerancia, prueba y versión",
        "case": "un sistema de protección solar paramétrico que debe responder a orientación, modulación, fabricación y mantenimiento sin ocultar reglas",
        "evidence": "modelo versionado con entradas, unidades, dependencias, pruebas límite, comparación de alternativas y salida interoperable",
    },
    73: {
        "lens": "propósito, procedencia de datos, desempeño, sesgo, explicabilidad, supervisión, seguridad, trazabilidad y retiro",
        "case": "un equipo que propone IA para revisar planos y priorizar mantenimiento, con falsos positivos que afectan decisiones y personas",
        "evidence": "ficha de sistema con uso previsto, datos, riesgos, benchmark, análisis independiente, responsables, monitoreo y condición de retiro",
    },
    74: {
        "lens": "captura, referencia espacial, resolución, oclusión, modelo, trayectoria de máquina, tolerancia, peligro e inspección",
        "case": "el levantamiento y prototipado de una unión existente donde errores de registro digital pueden propagarse hasta la fabricación",
        "evidence": "cadena archivo–máquina–pieza con calibración, tolerancias, zonas de riesgo, inspección dimensional y corrección documentada",
    },
    75: {
        "lens": "institución, suelo, mercado, derecho, experiencia cotidiana, dato, participación, distribución de beneficios y desplazamiento",
        "case": "un plan de regeneración alrededor de transporte público que aumenta acceso y valor del suelo, pero puede desplazar residentes y cuidados",
        "evidence": "diagnóstico multiescalar con escenarios, actores, datos desagregados, participación, efectos distributivos y medidas de seguimiento",
    },
    76: {
        "lens": "servicio, demanda, capacidad, dependencia, redundancia, accesibilidad, mantenimiento, gobernanza y recuperación",
        "case": "una interrupción regional que combina agua, energía, telecomunicaciones y transporte y obliga a priorizar servicios críticos",
        "evidence": "mapa de redes con niveles de servicio, dependencias, escenarios de falla, fases de inversión, responsables y continuidad",
    },
    77: {
        "lens": "escenario climático, frontera de balance, vida útil, carbono, agua, biodiversidad, exposición, adaptación y verificación",
        "case": "la rehabilitación climática de un edificio público que debe comparar reducción de demanda, materiales, naturaleza y operación futura",
        "evidence": "estrategia con línea base, escenarios, balances sin doble conteo, sensibilidad, co-beneficios, cargas desplazadas y medición posocupacional",
    },
    78: {
        "lens": "significancia, estratigrafía, condición material, compatibilidad, reversibilidad, desempeño, uso, fase y archivo",
        "case": "la conversión de una estructura industrial vacante con contaminación, valores patrimoniales, exigencias de uso y datos incompletos",
        "evidence": "expediente de transformación con levantamiento, mapa de incertidumbre, diagnóstico, alternativas, pruebas, fases y seguimiento",
    },
    79: {
        "lens": "capacidad, autonomía, apoyo, percepción, orientación, privacidad, cuidado, evacuación, participación y cambio temporal",
        "case": "un entorno residencial y comunitario compartido por infancia, personas mayores, neurodivergentes y redes formales e informales de cuidado",
        "evidence": "cadena de experiencia y accesibilidad evaluada con personas, escenarios de día y emergencia, conflictos, ajustes y revisión ética",
    },
    80: {
        "lens": "misión, ambiente extremo, soporte vital, logística, autonomía, redundancia, reparación, factor humano y transferencia terrestre",
        "case": "un hábitat remoto que debe sostener vida y trabajo durante una interrupción logística sin confundir analogía terrestre con certificación espacial",
        "evidence": "proyecto interdisciplinario con requisitos, interfaces, presupuestos de recursos, modos de falla, pruebas, operación, defensa y agenda de transferencia",
    },
}

STAGE_ROLES = (
    "delimita el problema y las variables que pertenecen al sistema",
    "separa datos, unidades, categorías y supuestos antes de modelar",
    "construye una representación capaz de revelar relaciones y ausencias",
    "explica mecanismos, dependencias y consecuencias entre escalas",
    "formula alternativas comparables y condiciones críticas",
    "ensaya una medición, cálculo, simulación o contraste apropiado",
    "busca fallos, sesgos, incertidumbres y efectos no deseados",
    "coordina actores, responsabilidades, interfaces y documentación",
    "valida mediante un método independiente y define seguimiento",
    "integra, defiende y transfiere el aprendizaje sin copiar parámetros",
)

LESSON_DESIGNS = {
    69: [
        ("situación observada → brecha de conocimiento → pregunta delimitada → factibilidad", "mapa del problema y una pregunta investigable con escala, población y tiempo", "la pregunta debe poder responderse con la evidencia disponible"),
        ("fenómeno → proposición → indicador observable → posible refutación", "tabla de hipótesis, proposiciones y preguntas abiertas", "una afirmación que no admite contraste permanece como opinión"),
        ("vocabulario → bases de datos → cadena de búsqueda → selección justificada", "protocolo de búsqueda con consultas, filtros y registro de exclusiones", "la conveniencia de acceso no puede sustituir la pertinencia"),
        ("documento original → interpretación → cita secundaria → uso en el argumento", "mapa de procedencia y cadena de citación de cinco afirmaciones", "una fuente secundaria no debe presentarse como evidencia primaria"),
        ("situación → pauta de observación o entrevista → codificación → patrón", "instrumento cualitativo pilotado y libro de códigos inicial", "el consentimiento y la voz discrepante son condiciones críticas"),
        ("población → muestra → variable → medición → inferencia limitada", "plan de medición con unidades, muestra y estadística descriptiva", "una muestra pequeña no autoriza generalizaciones poblacionales"),
        ("pregunta → evidencia cualitativa → evidencia cuantitativa → integración", "matriz de triangulación que conserva acuerdos y contradicciones", "dos métodos no corrigen automáticamente el mismo sesgo"),
        ("caso → regla de selección → dimensiones comunes → comparación", "protocolo comparativo para dos casos con fronteras equivalentes", "la elección del caso debe declararse antes de conocer el resultado"),
        ("dato → permiso → anonimización → transformación → reproducción", "paquete reproducible con diccionario de datos, decisiones éticas y bitácora", "anonimizar no basta si el contexto permite reidentificar personas"),
        ("pregunta → método → resultados → argumento → objeciones", "índice razonado de tesis y guion de defensa con límites", "la conclusión no puede exceder el método ni ocultar resultados adversos"),
    ],
    70: [
        ("propósito de la oficina → servicios → capacidades → modelo de práctica", "mapa de servicios, competencias, aliados y límites de una oficina", "la promesa comercial debe coincidir con la capacidad real"),
        ("necesidad del cliente → criterio de selección → propuesta → decisión de participar", "brief comercial y matriz aceptar, negociar o rechazar", "un encargo incompatible con la ética no se corrige sólo con honorarios"),
        ("entregable → esfuerzo → honorario → exclusión → cambio", "desglose de alcance y honorarios con supuestos y mecanismo de cambios", "una exclusión crítica debe ser comprendida y asignada"),
        ("riesgo → parte responsable → contrato → seguro → evidencia", "matriz contractual de riesgos, responsabilidades y coberturas por verificar", "el seguro no sustituye prevención ni competencia profesional"),
        ("cliente → usuario → mandante → autoridad → instancia de decisión", "mapa de gobernanza y protocolo de decisiones y escalamiento", "quien paga no representa necesariamente a todas las personas usuarias"),
        ("interés → alternativa → concesión → acuerdo → seguimiento", "guion de negociación y minuta con compromisos, responsables y plazos", "un acuerdo oral relevante debe quedar confirmado y trazable"),
        ("promesa pública → evidencia → derecho de uso → reputación", "pieza de comunicación revisada con matriz de afirmaciones y permisos", "el marketing no puede atribuir autoría, resultados o respaldo inexistentes"),
        ("capacidad → costo fijo → ingreso probable → caja → decisión", "flujo de caja de doce semanas con tres escenarios de carga", "facturación no equivale a liquidez disponible"),
        ("rol → carga → coordinación → conflicto → aprendizaje", "plan de equipo con responsabilidades, bienestar, revisión y continuidad", "la sobrecarga sostenida es un riesgo de calidad y seguridad"),
        ("consulta → propuesta → reunión → ajuste → cierre documentado", "expediente simulado de encargo desde propuesta hasta acta de cierre", "ningún cierre es válido con alcance, autoridad o siguiente paso ambiguos"),
    ],
    71: [
        ("pregunta → relación espacial → punto de vista → trazo analítico", "serie de tres dibujos que cambian deliberadamente el punto de vista", "el dibujo debe revelar una relación y no sólo embellecerla"),
        ("sección → cuerpo → umbral → tiempo → secuencia", "sección narrativa con episodios, cotas, luz, uso y transición", "la secuencia debe corresponder a una geometría comprobable"),
        ("fuente visual → recorte → montaje → argumento → atribución", "collage con registro de procedencia y lectura crítica de cada fragmento", "una imagen sin permiso o contexto no puede sostener el argumento"),
        ("posición de cámara → lente → luz → edición → lectura", "ensayo fotográfico comparado que hace visibles dos sesgos de encuadre", "la edición no debe ocultar condiciones relevantes del espacio"),
        ("dato → escala → codificación → comparación → incertidumbre", "gráfico espacial con leyenda, fuente, rango y dato desconocido", "color y tamaño no deben exagerar diferencias ni borrar ausencias"),
        ("audiencia → pregunta → arco narrativo → evidencia → llamada a decisión", "relato de cinco minutos adaptado a crítica, comunidad y cliente", "la simplificación no puede cambiar el grado de certeza"),
        ("estado inicial → transición → duración → operación → estado final", "animación breve con tiempo, eventos y supuestos visibles", "la velocidad de reproducción no debe falsear la experiencia"),
        ("lugar real → registro → capa digital → alineación → prueba situada", "prototipo de RA con anclas, escala y comprobación en terreno", "una desalineación puede convertir una ayuda en información peligrosa"),
        ("escena → navegación → interacción → presencia → prueba de confort", "prototipo de RV y pauta de prueba con rutas alternativas", "mareo, desorientación y exclusión requieren salida equivalente"),
        ("contenido maestro → formatos → accesibilidad → publicación → archivo", "portafolio multiformato con texto alternativo y versión de baja tecnología", "la versión accesible debe conservar la información esencial"),
    ],
    72: [
        ("problema repetible → entradas → reglas → pasos → prueba manual", "pseudocódigo y diagrama de flujo comprobados con dos ejemplos", "automatizar una tarea mal definida sólo acelera el error"),
        ("dato → tipo → unidad → estructura → validación", "diccionario de datos y conjunto mínimo con entradas válidas e inválidas", "número sin unidad y nulo convertido en cero son fallos críticos"),
        ("coordenada → vector → matriz → transformación → comprobación", "cuaderno de transformaciones con resultado directo e inverso", "el orden de transformaciones debe permanecer explícito"),
        ("primitiva → continuidad → discretización → tolerancia → intercambio", "comparación de curva, superficie y malla bajo dos tolerancias", "más polígonos no garantizan mejor geometría ni fabricación"),
        ("parámetro → dependencia → restricción → variante → sensibilidad", "grafo paramétrico con entradas, salidas y prueba de valores límite", "un parámetro sin significado de diseño es ruido de control"),
        ("tarea → API o archivo → script → registro → revisión humana", "script pequeño con instrucciones, ejemplo y manejo de errores", "la automatización debe fallar de forma visible y recuperable"),
        ("objetivos → variables → reglas → población de soluciones → selección", "espacio generativo de alternativas con criterios y descarte trazable", "generar cantidad no equivale a producir diversidad útil"),
        ("objetivos en conflicto → restricciones → evaluación → frente de Pareto → elección", "comparación multiobjetivo sin reducir todo a una suma opaca", "una condición crítica no puede convertirse en peso compensatorio"),
        ("caso normal → borde → error esperado → versión → reproducción", "suite mínima de pruebas y bitácora de versiones del modelo", "un resultado visual correcto no demuestra que el algoritmo sea correcto"),
        ("regla → modelo → archivo de fabricación → pieza → retroalimentación", "proyecto computacional completo con prototipo medido y corrección", "la cadena debe conservar unidades y tolerancias hasta la pieza"),
    ],
    73: [
        ("decisión → posible apoyo de IA → consecuencia → supervisión → exclusión", "mapa de usos permitidos, condicionados y prohibidos durante el ciclo de vida", "una decisión de seguridad o derecho no puede quedar sin responsable humano"),
        ("origen → permiso → población representada → transformación → brecha", "ficha de datos con procedencia, licencia, ausencias y uso previsto", "datos abundantes no compensan una población mal representada"),
        ("brief → variantes generadas → restricciones → crítica → selección humana", "comparación de alternativas con registro de prompts, versiones y descarte", "la novedad visual no sustituye habitabilidad ni autoría responsable"),
        ("captura territorial → etiqueta → modelo → detección → verificación de campo", "protocolo de análisis de sitio con muestra de falsos positivos y negativos", "ninguna detección remota reemplaza confirmar condiciones críticas"),
        ("programa → representación → propuesta → explicación → prueba independiente", "ensayo de distribución espacial con restricciones y explicación de decisión", "una explicación plausible no prueba causalidad ni cumplimiento"),
        ("modelo BIM o plano → regla de revisión → hallazgo → clasificación → responsable", "benchmark de detección de inconsistencias contra revisión manual", "la ausencia de alerta no demuestra ausencia de error"),
        ("dato de obra → predicción → umbral → acción → seguimiento", "tablero simulado con costos, plazo, incertidumbre y protocolo de escalamiento", "una predicción no autoriza ocultar el rango ni la fuente del dato"),
        ("sensor → modelo del activo → anomalía → orden de trabajo → cierre", "flujo de mantenimiento predictivo con gemelo digital y evidencia de cierre", "una alerta automática sin contexto puede aumentar fallas y carga operativa"),
        ("dato personal u obra protegida → procesamiento → salida → exposición → control", "registro de riesgos de sesgo, copyright, privacidad y ciberseguridad", "un uso técnicamente posible puede ser jurídicamente o éticamente inaceptable"),
        ("salida de IA → análisis independiente → discrepancia → corrección → retiro", "auditoría comparada con casos de prueba, métricas y decisión de continuidad", "el mismo sistema no debe producir y validar su propia respuesta"),
    ],
    74: [
        ("misión de vuelo → permiso → plan de captura → riesgo → producto", "plan de vuelo académico con zonas, clima, privacidad y contingencia", "no se opera sin autorización, competencia y evaluación local"),
        ("pulso → retorno → nube → densidad → superficie interpretable", "sección de nube de puntos con densidad, oclusiones y precisión declarada", "un vacío de puntos no equivale a un vacío físico"),
        ("estación → solape → registro → error → nube unificada", "registro de dos estaciones con informe de error y zonas no observadas", "cerrar visualmente la nube no corrige una mala referencia"),
        ("imágenes → control → correspondencias → modelo → comprobación", "modelo fotogramétrico con escala, control y mapa de error", "textura realista no demuestra exactitud geométrica"),
        ("captura → clasificación → objeto → atributo → uso del modelo", "modelo semántico mínimo con origen y confianza de cada atributo", "nombrar un objeto no valida su condición ni material"),
        ("geometría → herramienta → trayectoria → sujeción → corte", "archivo CNC o láser con nesting, kerf, prueba y plan seguro", "la simulación de trayectoria no reemplaza control de máquina"),
        ("modelo → orientación → soporte → capa → pieza inspeccionada", "cupón impreso con registro de parámetros, defectos y medida", "una pieza visible no demuestra resistencia ni aptitud de uso"),
        ("mezcla o material → deposición → junta → curado → control", "protocolo conceptual de fabricación aditiva edilicia con ensayos requeridos", "escala mayor introduce estructura, clima y certificación no resueltos"),
        ("tarea → robot → persona → zona → parada → recuperación", "layout de celda robótica con peligros, barreras y secuencia de emergencia", "la productividad no puede compensar una interacción insegura"),
        ("necesidad → prototipo → fabricación → medición → iteración", "prototipo 1:1 con tolerancias previstas y reales, fallas y segunda versión", "la entrega incluye lo que falló y cómo cambió el diseño"),
    ],
    75: [
        ("actor → institución → recurso urbano → conflicto → derecho", "mapa de gobernanza y poder sobre una decisión de barrio", "participar no equivale a tener capacidad real de decisión"),
        ("norma de suelo → valor → inversión → carga → retorno público", "diagrama de captura de valor con beneficiarios y riesgos de desplazamiento", "el aumento de valor no demuestra mejora distribuida"),
        ("ingreso → precio o arriendo → gasto del hogar → localización → acceso", "perfil de asequibilidad que incorpora transporte y servicios", "precio de compra aislado no mide carga habitacional"),
        ("ocupación → tenencia → servicio → amenaza → estrategia incremental", "diagnóstico de asentamiento informal sin criminalizar a residentes", "regularizar suelo no resuelve por sí solo habitabilidad y riesgo"),
        ("inversión → cambio de demanda → alza de valor → desplazamiento → mitigación", "indicadores tempranos de gentrificación y plan de seguimiento", "renovación física no justifica expulsión directa o indirecta"),
        ("cadena de cuidados → viaje → tiempo → seguridad → acceso", "mapa temporal de movilidad cotidiana desagregado por género y cuidado", "promedios diarios pueden ocultar viajes encadenados"),
        ("trayectoria migratoria → red cultural → servicio → barrera → mediación", "mapa de acceso intercultural con puntos de exclusión y apoyo", "una categoría administrativa no representa una cultura homogénea"),
        ("fenómeno → dato → método de captura → población ausente → decisión", "auditoría de un dataset urbano con sesgos y límites de uso", "lo no medido no puede tratarse como inexistente"),
        ("información → deliberación → incidencia → acuerdo o disenso → retorno", "plan participativo con reglas de influencia y devolución pública", "una consulta sin efecto declarado es extracción de tiempo y conocimiento"),
        ("escenario → inversión → efecto espacial → efecto distributivo → monitoreo", "plan urbano con tres escenarios y matriz de impactos por grupo", "el escenario preferido debe superar derechos y condiciones críticas"),
    ],
    76: [
        ("necesidad → servicio → capacidad → indicador → nivel aceptable", "ficha de nivel de servicio con usuarios, umbral y degradación", "la capacidad instalada no demuestra servicio efectivo"),
        ("función vial → velocidad → cruce → estancia → seguridad", "sección de calle completa con conflicto modal y alternativa", "el flujo vehicular no puede borrar seguridad y accesibilidad"),
        ("corredor → acceso → barrera → actividad → mitigación", "mapa de autopista y asentamientos con conectividad y externalidades", "ahorro de tiempo agregado puede ocultar daños locales"),
        ("origen y destino → red ferroviaria → nodo → transbordo → logística", "esquema regional de ferrocarril de pasajeros y carga con interfaces", "una línea no funciona sin operación, acceso y última milla"),
        ("cuenca → almacenamiento → usuarios → ecosistema → emergencia", "balance conceptual de embalse con actores y consecuencias aguas abajo", "el volumen útil no resume impactos sociales y ecológicos"),
        ("fuente → tratamiento → distribución → uso → retorno y drenaje", "diagrama territorial del ciclo urbano del agua y puntos de falla", "resolver abastecimiento sin saneamiento traslada el riesgo"),
        ("demanda → generación → red → almacenamiento → isla", "escenario de energía distribuida con cargas críticas y recuperación", "renovable no equivale automáticamente a continua o inocua"),
        ("flujo material → separación → recuperación → rechazo → localización", "mapa de residuos y recuperación con distancias, salud y mercado", "una tasa de reciclaje no describe toxicidad ni destino final"),
        ("conectividad → nodo → redundancia → servicio crítico → seguridad", "mapa de infraestructura digital con dependencias físicas y ciberfísicas", "la nube depende de energía, agua, territorio y personas"),
        ("redes superpuestas → falla común → prioridad → fase → gobernanza", "plan integrado regional con escenarios de interrupción y recuperación", "optimizar cada red por separado puede debilitar el sistema completo"),
    ],
    77: [
        ("amenaza futura → exposición → vulnerabilidad → opción → ruta adaptativa", "ruta de adaptación con umbrales, decisiones reversibles y seguimiento", "usar sólo el clima histórico subestima condiciones futuras"),
        ("archivo climático → escenario → estrategia pasiva → horas de fallo → ajuste", "comparación térmica conceptual para clima actual y futuro", "una estrategia hoy útil puede provocar sobrecalentamiento mañana"),
        ("demanda → generación → periodo → frontera → balance residual", "balance net-zero con alcance, tiempo, pérdidas y energía importada", "un balance anual no demuestra operación continua ni cero impacto"),
        ("material → cantidad → factor → almacenamiento → fin de vida", "inventario de carbono incorporado con escenarios biogénicos", "carbono almacenado no puede descontarse sin tiempo y destino"),
        ("stock → uso → mantenimiento → desmontaje → nuevo ciclo", "pasaporte material y escenario de circularidad de un componente", "reciclable en teoría no equivale a recuperación real"),
        ("materia prima viva → proceso → propiedad → exposición → degradación", "ficha crítica de biomaterial con ensayos y condiciones de uso", "origen biológico no garantiza baja toxicidad o durabilidad"),
        ("estímulo → respuesta → control → energía → modo de falla", "protocolo de material inteligente con respuesta y posición segura", "la novedad no reemplaza mantenibilidad ni comportamiento pasivo seguro"),
        ("nanoescala → prestación → incorporación → exposición → cautela", "matriz prestación-riesgo para una aplicación nanotecnológica", "una mejora de laboratorio no demuestra inocuidad del sistema"),
        ("proceso ecológico → intervención → co-beneficio → mantenimiento → medición", "sección de solución basada en naturaleza con indicadores", "vegetación decorativa no equivale a función ecológica"),
        ("evitar → reducir → adaptar → reparar → verificar", "proyecto climático integrado con balances y plan posocupacional", "no se puede declarar regeneración sin línea base y medición"),
    ],
    78: [
        ("stock existente → condición → ubicación → adaptabilidad → prioridad", "inventario georreferenciado de potencial de reutilización", "vacancia no significa disponibilidad jurídica o material"),
        ("archivo → huella física → fase histórica → significado → laguna", "cronología estratigráfica con fuentes y contradicciones", "una ausencia documental no autoriza completar la historia"),
        ("síntoma → material → mecanismo → prueba → nivel de certeza", "mapa patológico con hipótesis y plan de ensayos", "reparar el síntoma sin causa puede agravar el daño"),
        ("captura → registro → semántica → HBIM → consulta", "modelo patrimonial con confianza y procedencia por elemento", "detalle geométrico no equivale a conocimiento histórico"),
        ("valor → intervención → compatibilidad → reversibilidad → seguimiento", "matriz de alternativas de intervención y pérdida potencial", "mínima intervención no significa ausencia de acción"),
        ("preexistencia → demanda estructural → acceso → evacuación → coordinación", "mapa de conflictos entre refuerzo, accesibilidad e incendio", "cumplir un frente no puede degradar otro requisito crítico"),
        ("envolvente existente → humedad → energía → detalle → monitoreo", "estrategia energética con análisis higrotérmico por verificar", "aislar sin diagnosticar humedad puede trasladar condensación"),
        ("comunidad → valor industrial, moderno o indígena → autoría → tratamiento", "declaración de significancia con voces, límites y desacuerdos", "la etiqueta patrimonial no reemplaza consentimiento ni contexto"),
        ("edificio → desmontaje → componente → evaluación → nuevo uso", "plan de deconstrucción y banco de componentes trazable", "recuperar cantidad no garantiza calidad para reutilizar"),
        ("diagnóstico → nuevo uso → fases → obra → operación → revisión", "proyecto de reutilización adaptativa con seguimiento posocupacional", "el éxito se comprueba en uso, no sólo al inaugurar"),
    ],
    79: [
        ("capacidad → barrera → apoyo → elección → autonomía", "recorrido cotidiano de una persona mayor con alternativas de apoyo", "proteger no debe eliminar decisión y participación"),
        ("hogar → intensidad de apoyo → red de cuidado → adaptación → transición", "escenarios de vivienda con apoyos crecientes sin mudanza forzada", "el espacio no sustituye servicios, vínculos ni recursos"),
        ("estímulo → procesamiento → sobrecarga → regulación → orientación", "mapa sensorial y de wayfinding con rutas de recuperación", "reducir estímulos para todos puede empobrecer la experiencia"),
        ("privacidad → contacto → naturaleza → control → crisis", "secuencia de espacios restaurativos con grados de retiro", "un ambiente tranquilo no reemplaza atención clínica"),
        ("edad → juego → desafío → riesgo aceptable → supervisión", "mapa de juego y autonomía gradual con peligros diferenciados", "eliminar todo riesgo también elimina aprendizaje y agencia"),
        ("capacidades combinadas → tarea → barreras → apoyos → evacuación", "cadena de accesibilidad para una persona con discapacidad múltiple", "resolver una sola discapacidad puede crear otra barrera"),
        ("práctica cultural → identidad → uso espacial → conflicto → mediación", "programa intercultural construido con escenarios y voces diversas", "una referencia cultural no representa a todas las personas"),
        ("cuidador → tarea → tiempo → carga física → descanso", "mapa de trabajo de cuidado formal e informal y ajustes espaciales", "eficiencia institucional no debe transferir carga invisible"),
        ("desplazamiento → llegada → refugio → servicio → integración", "protocolo espacial de acogida con privacidad, información y continuidad", "la condición temporal no justifica soluciones indignas"),
        ("persona → escenario cotidiano → emergencia → retroalimentación → corrección", "proyecto de cuidados con evaluación participativa y dos versiones", "la participación requiere consentimiento, devolución y cambios visibles"),
    ],
    80: [
        ("ambiente polar o desértico → misión → envolvente → logística → rescate", "comparación de dos bases terrestres extremas y sus dependencias", "lo extremo no justifica ignorar bienestar y evacuación"),
        ("medio marino → flotación → corrosión → servicio → evacuación", "sección de asentamiento flotante con accesos y mantenimiento", "estabilidad conceptual no equivale a ingeniería naval"),
        ("terreno → excavación → protección → ventilación → salida", "esquema de hábitat subterráneo con modos de falla", "protección exterior puede aumentar riesgo interior"),
        ("tarea remota → máquina → autonomía → excepción → reparación", "plan de construcción autónoma con intervención humana segura", "autónomo no significa sin supervisión ni recuperación"),
        ("entrada → proceso → almacenamiento → pérdida → cierre de ciclo", "presupuesto de agua, aire, energía y residuos con pérdidas explícitas", "un ciclo nunca se declara cerrado ocultando reposición"),
        ("misión lunar → polvo → radiación → logística → mantenimiento", "arquitectura de sistema lunar con interfaces y supuestos", "el caso avanzado no constituye diseño certificado"),
        ("demora de comunicación → recurso local → fallo → reparación → refugio", "escenario marciano con autonomía y piezas críticas", "la autosuficiencia total es una hipótesis que debe cuantificarse"),
        ("activo físico → sensor → red → amenaza → respuesta segura", "modelo de amenazas físico-ciberfísicas para un edificio conectado", "seguridad digital y seguridad de vida deben coordinarse"),
        ("encargo → especialidades → interfaces → pruebas → operación", "matriz del proyecto final con requisitos y verificaciones", "una interfaz sin propietario es una falla pendiente"),
        ("problema → alternativas → verificación → defensa → transferencia", "proyecto final, portafolio de versiones y agenda de investigación", "defender incluye reconocer límites y condiciones de reapertura"),
    ],
}

EXTRA_ROUTES = [
    {"id":"RUTA-13","title":"Urbanismo","parts":[4,9,11,12,36,38,45,48,75,76],"entry":"Fundamentos de sitio, representación y lectura social del espacio.","exit":"Formular escenarios urbanos y evaluar efectos espaciales, distributivos, ambientales y operativos.","capstone":"EST-10"},
    {"id":"RUTA-14","title":"Paisaje","parts":[9,11,13,28,36,37,38,45,75,77],"entry":"Lectura de topografía, agua, vegetación, escalas y procesos temporales.","exit":"Coordinar ecología, uso, mantenimiento, riesgo y experiencia en una estrategia de paisaje.","capstone":"EST-10"},
    {"id":"RUTA-15","title":"Vivienda","parts":[4,9,12,15,18,28,40,42,47,49,75,79],"entry":"Programa, representación, sitio y diversidad de hogares.","exit":"Defender una propuesta habitacional situada desde habitabilidad, asequibilidad, cuidado y ciclo de vida.","capstone":"EST-10"},
    {"id":"RUTA-16","title":"Diseño computacional","parts":[2,3,11,14,20,44,66,69,71,72,73,74],"entry":"Geometría, unidades, representación digital y capacidad básica de formular reglas.","exit":"Construir y validar un modelo paramétrico reproducible con sensibilidad y alternativas.","capstone":"EST-09"},
    {"id":"RUTA-17","title":"Fabricación digital","parts":[2,20,22,23,24,25,26,39,43,44,66,72,74],"entry":"Lectura de detalle, materiales, tolerancias y seguridad de procesos.","exit":"Transformar un modelo en prototipo fabricado, inspeccionado y documentado sin perder trazabilidad.","capstone":"EST-09"},
    {"id":"RUTA-18","title":"Arquitectura bioclimática","parts":[3,11,13,27,28,29,30,32,37,45,47,77],"entry":"Balances básicos, clima, sección y representación de flujos.","exit":"Comparar estrategias pasivas bajo clima actual y futuro mediante evidencia y medición.","capstone":"EST-10"},
    {"id":"RUTA-19","title":"Iluminación","parts":[2,3,10,18,28,29,30,33,47,59,71],"entry":"Geometría solar, percepción, unidades y lectura de planos y secciones.","exit":"Coordinar luz natural y artificial con tarea, energía, control, accesibilidad y operación.","capstone":"EST-10"},
    {"id":"RUTA-20","title":"Acústica","parts":[3,10,18,26,27,30,32,47,51,53,58,59],"entry":"Ondas, unidades, percepción y lectura de materialidad y recintos.","exit":"Diagnosticar y comparar decisiones acústicas desde fuente, trayectoria, receptor y uso.","capstone":"EST-10"},
    {"id":"RUTA-21","title":"Interiores","parts":[2,4,10,14,16,18,26,30,33,47,59,64,71,79],"entry":"Representación, programa, ergonomía, materialidad y accesibilidad.","exit":"Diseñar interiores coordinando uso, percepción, sistemas, salud, mantenimiento y cambio.","capstone":"EST-10"},
    {"id":"RUTA-22","title":"Arquitectura hospitalaria","parts":[4,16,18,30,31,32,33,34,38,40,47,53,79],"entry":"Programa complejo, flujos, instalaciones, accesibilidad y continuidad.","exit":"Coordinar una tipología sanitaria mediante escenarios clínicos y operativos sin asumir competencia médica.","capstone":"EST-10"},
    {"id":"RUTA-23","title":"Arquitectura educacional","parts":[4,12,14,16,18,28,30,34,47,65,71,79],"entry":"Programa, participación, confort y observación de usos.","exit":"Defender un entorno de aprendizaje flexible, inclusivo, saludable y vinculado a su comunidad.","capstone":"EST-10"},
    {"id":"RUTA-24","title":"Transporte","parts":[3,11,12,17,18,34,36,38,42,47,54,55,62,75,76],"entry":"Escalas territoriales, flujos, capacidad, accesibilidad y riesgo.","exit":"Integrar nodos y cadenas de viaje con operación, interfaces, continuidad y efectos urbanos.","capstone":"EST-10"},
    {"id":"RUTA-25","title":"Infraestructura","parts":[3,11,12,13,17,19,20,21,31,33,35,36,38,42,43,56,57,62,67,76],"entry":"Matemática, territorio, camino de cargas y lectura de sistemas.","exit":"Formular un anteproyecto de infraestructura con niveles de servicio, dependencias y ciclo de vida.","capstone":"EST-10"},
    {"id":"RUTA-26","title":"Arquitectura industrial y logística","parts":[17,19,20,21,31,32,33,34,39,42,43,47,60,61,62,74,76],"entry":"Procesos, flujos, riesgos, estructura e instalaciones.","exit":"Coordinar una instalación productiva desde proceso, seguridad, expansión, mantenimiento y logística.","capstone":"EST-10"},
    {"id":"RUTA-27","title":"Centros de datos","parts":[17,20,21,29,31,32,33,34,38,44,47,60,73,76,80],"entry":"Sistemas técnicos, energía, información, continuidad y gestión de riesgos.","exit":"Evaluar un edificio digital crítico desde capacidad, redundancia, seguridad física y ciberfísica.","capstone":"EST-10"},
    {"id":"RUTA-28","title":"Arquitectura sísmica","parts":[3,9,19,20,21,22,23,24,25,27,34,35,38,40,46,47,78],"entry":"Equilibrio, materiales, suelo, representación y límites del modelo.","exit":"Coordinar forma, sistema resistente, componentes, continuidad y recuperación con especialistas.","capstone":"EST-10"},
    {"id":"RUTA-29","title":"Resiliencia y emergencia","parts":[4,9,12,13,18,31,33,34,35,36,37,38,45,47,76,77,79,80],"entry":"Lectura territorial, personas, sistemas y vocabulario de riesgo.","exit":"Comparar medidas de reducción, preparación, continuidad y recuperación para escenarios múltiples.","capstone":"EST-10"},
    {"id":"RUTA-30","title":"Desarrollo inmobiliario","parts":[1,4,11,12,14,15,40,41,42,43,47,49,50,64,70,75],"entry":"Ciclo del proyecto, programa, sitio, costo, normativa y ética.","exit":"Evaluar una oportunidad con factibilidad, financiamiento, riesgo, impactos y estrategia de salida.","capstone":"EST-10"},
    {"id":"RUTA-31","title":"Investigación y academia","parts":[1,3,4,5,8,9,11,12,30,45,46,47,48,69,71,73],"entry":"Lectura crítica, escritura, unidades y distinción entre evidencia y opinión.","exit":"Diseñar, ejecutar y defender una investigación reproducible y éticamente documentada.","capstone":"EST-09"},
    {"id":"RUTA-32","title":"Visualización","parts":[2,3,10,11,14,30,44,66,69,71,72,74],"entry":"Dibujo técnico, composición, escala y alfabetización digital.","exit":"Comunicar espacio, datos, tiempo e incertidumbre mediante un sistema visual accesible y verificable.","capstone":"EST-09"},
    {"id":"RUTA-33","title":"Inteligencia artificial aplicada","parts":[1,4,8,11,14,40,41,42,43,44,47,48,60,69,72,73,74,75,80],"entry":"Pensamiento crítico, datos, versiones, privacidad y responsabilidad profesional.","exit":"Diseñar y auditar un uso de IA con propósito, datos, riesgos, pruebas, supervisión y retiro.","capstone":"EST-09"},
]


def update_pedagogy() -> None:
    path = ROOT / "data" / "pedagogy.json"
    pedagogy = json.loads(path.read_text(encoding="utf-8"))
    studios = [item for item in pedagogy["studios"] if int(item["id"].split("-")[1]) <= 8]
    routes = [item for item in pedagogy["routes"] if int(item["id"].split("-")[1]) <= 12]
    pedagogy["studios"] = studios + EXTRA_STUDIOS
    pedagogy["routes"] = routes + EXTRA_ROUTES
    path.write_text(json.dumps(pedagogy, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def lesson_markdown(number: int, part: int, part_title: str, purpose: str, product: str, source_ids: tuple[str, str], title: str) -> str:
    class_id = f"ARQ-{number:03d}"
    previous = f"ARQ-{number - 1:03d}"
    following = f"ARQ-{number + 1:03d}" if number < 800 else "EST-10"
    position = number - (part - 1) * 10
    scenario = f"EXP-{number:03d}"
    depth = PART_DEPTH[part]
    stage_role = STAGE_ROLES[position - 1]
    sequence, specific_evidence, critical_condition = LESSON_DESIGNS[part][position - 1]
    visual_steps = [step.strip() for step in sequence.split("→")]
    if not 4 <= len(visual_steps) <= 6:
        raise ValueError(f"{class_id} must define a four-to-six-step visual sequence")
    question = (
        f"¿Cómo abordar {title.lower()} y comprobar esta condición crítica: "
        f"{critical_condition}?"
    )
    node_ids = [chr(ord("A") + index) for index in range(len(visual_steps))]
    graph_lines = ["flowchart TD"]
    for index in range(len(visual_steps) - 1):
        graph_lines.append(
            f'    {node_ids[index]}["{visual_steps[index]}"] --> '
            f'{node_ids[index + 1]}["{visual_steps[index + 1]}"]'
        )
    graph_lines.append(
        f'    {node_ids[-1]} --> Z["Evidencia · {specific_evidence}"]'
    )
    graph_lines.append(
        f'    X["Condición crítica · {critical_condition}"] --> {node_ids[-2]}'
    )
    topic_graph = "\n".join(graph_lines)
    last_step = visual_steps[-1]
    check_step = visual_steps[-2]
    return f"""# {class_id} · {title}

**Parte {part:02d} · Fase III · Profundización y especialización · Edición 2026.10.**

Material educativo independiente. Esta clase no sustituye formación acreditada, experiencia supervisada, encargo profesional, normativa vigente, cálculo firmado, permiso ni revisión de especialistas. Los datos del caso son didácticos y deben reemplazarse por antecedentes verificables antes de una aplicación real.

## Pregunta central

{question}

## Propósito, prerrequisitos y resultados de aprendizaje

La clase profundiza en **{title.lower()}** para {purpose}. Recibe de `{previous}` un registro de decisiones, fuentes y pendientes. No basta con reconocer vocabulario: el estudiante debe transformar una pregunta en un procedimiento que otra persona pueda reconstruir, criticar y corregir.

Al terminar podrás:

1. **identificar** los datos, actores, escalas y límites que condicionan una decisión sobre {title.lower()};
2. **comparar** al menos dos alternativas con una función común y criterios no intercambiables;
3. **producir** una evidencia propia para el portafolio de Fase III;
4. **justificar** qué parte puede resolver arquitectura, qué requiere colaboración especializada y qué permanece abierta;
5. **revisar** la decisión cuando cambie un supuesto, una fuente, una necesidad o una condición de uso.

La evidencia de salida será un componente del **{product}** de la Parte {part:02d}.

## Conceptos y distinciones fundamentales

### Núcleo disciplinar de esta clase

Esta clase no trata el tema como una etiqueta. Su núcleo operativo articula **{depth["lens"]}**. Dentro de esa cadena, **{title.lower()}** ocupa la posición {position} de la parte y {stage_role}. La pregunta decisiva es qué cambia en el proyecto cuando cambia una de esas entradas, cómo se observa el efecto y quién tiene autoridad para aceptar la consecuencia.

La secuencia propia de la clase es **{sequence}**. Su resultado concreto será **{specific_evidence}**. La revisión debe comprobar que **{critical_condition}**. Estas tres frases funcionan como guía de lectura: el texto explica la secuencia, el ejercicio construye la evidencia y la evaluación intenta refutar una conclusión demasiado amplia.

El expediente específico debe poder aplicarse a **{depth["case"]}**. Cada elemento debe conservar escala, fecha, versión, responsable y relación con el producto acumulativo de la Parte {part:02d}. Cuando el dato no existe, se registra el método para obtenerlo; cuando una atribución corresponde a otra disciplina, se documenta la interfaz y el punto de coordinación.

El título nombra un campo, pero una clase necesita una decisión. En {title.lower()} conviene separar el **objeto observado**, la **representación** que construimos de él, el **método** usado para examinarlo y la **conclusión** que ese método permite sostener. Una imagen detallada puede provenir de datos débiles; un modelo preciso puede responder una pregunta irrelevante; una fuente autorizada puede quedar fuera de contexto. La calidad empieza cuando esas capas permanecen visibles.

También deben distinguirse **requisito**, **preferencia**, **hipótesis** y **restricción**. Un requisito tiene una autoridad, una versión y una condición de aplicación. Una preferencia expresa valor o intención y puede entrar en conflicto con otras. Una hipótesis permite avanzar provisionalmente y necesita una prueba. Una restricción delimita el espacio de soluciones, pero puede cambiar cuando cambia el sitio, el presupuesto, la tecnología o el acuerdo entre actores. Mezclarlas produce decisiones que parecen cerradas antes de estarlo.

La profundidad no consiste en acumular términos. Consiste en explicar relaciones causales: qué entrada modifica qué resultado, a través de qué mecanismo, con qué incertidumbre y para quién. En esta clase se usa la secuencia **pregunta → evidencia → alternativa → prueba → decisión → seguimiento**. Si falta una etapa, debe registrarse como pendiente y asignarse a una persona o disciplina capaz de resolverla.

## Contexto histórico, social y profesional

Las prácticas asociadas a {title.lower()} cambian con los instrumentos, las instituciones y las expectativas sociales. La disponibilidad de modelos digitales, sensores o automatización puede ampliar lo observable, pero también desplaza trabajo, crea dependencias y concentra decisiones en datos o plataformas que no siempre son transparentes. La historia del campo se lee como transformación de problemas, responsabilidades y medios, no como una sucesión inevitable de herramientas.

En la práctica profesional, una decisión rara vez pertenece a una sola persona. El arquitecto puede formular el problema espacial, coordinar interfaces, representar alternativas y conservar el registro. Especialistas, comunidades, autoridades, constructores, operadores y mandantes aportan evidencia diferente. Coordinar significa declarar quién origina un dato, quién lo revisa, quién decide y qué modificación obliga a reabrir el expediente. No significa asumir atribuciones reguladas de otras disciplinas.

## Método: de la observación a una decisión trazable

1. **Delimitar.** Escribe la pregunta, el usuario o servicio afectado, la escala, el horizonte temporal y la jurisdicción.
2. **Inventariar.** Separa antecedentes confirmados, datos por medir, supuestos de trabajo, preferencias y restricciones.
3. **Representar.** Elige planta, sección, mapa, diagrama, modelo, tabla o prototipo según la relación que necesitas comprobar.
4. **Comparar.** Mantén igual la función de las alternativas; si cambian las fronteras, explica el cambio antes de puntuar.
5. **Probar.** Define una observación, cálculo, simulación, revisión o ensayo y anticipa qué resultado refutaría la hipótesis.
6. **Decidir.** Vincula la elección con evidencia y conserva las alternativas descartadas junto con la razón.
7. **Revisar.** Establece responsable, fecha, condición de reapertura y destino de la evidencia en operación o investigación.

Este método evita que la herramienta se convierta en autoridad. Una simulación, render, modelo o respuesta automática es una representación condicionada por entradas y reglas. Debe verificarse por un medio independiente proporcional al riesgo. Para consecuencias críticas, la revisión humana y especializada forma parte del sistema y no es una nota al pie.

## Mapa visual de la decisión

```mermaid
{topic_graph}
```

El diagrama es específico de **{title.lower()}**. Se lee de arriba abajo y permite localizar un salto. Si el expediente pasa del primer al último nodo sin documentar los pasos intermedios, la conclusión todavía no es reproducible. La condición crítica entra antes del cierre porque debe cambiar o detener la decisión, no aparecer como advertencia tardía.

## Caso trabajado: {scenario}

El caso se sitúa en **{depth["case"]}**. El equipo debe abordar **{title.lower()}** y entregar **{specific_evidence}**. La primera versión salta desde **{visual_steps[0]}** hasta **{last_step}**: presenta una respuesta terminada, pero no permite saber cómo se tomaron las decisiones intermedias.

La revisión devuelve el trabajo a **{visual_steps[1]}** y **{visual_steps[2]}**. El equipo separa datos confirmados, hipótesis y desconocidos; identifica qué representación hace visible el mecanismo y asigna a una persona la comprobación de **{check_step}**. Esa corrección cambia la evidencia: deja de ser una afirmación ilustrada y se convierte en un procedimiento que otra persona puede repetir.

Antes de cerrar, la crítica aplica la condición **“{critical_condition}”**. Si no se satisface, la entrega permanece abierta aunque su presentación sea convincente. El resultado del caso {scenario} es una versión revisada de **{specific_evidence}**, acompañada por la objeción que produjo el cambio y por un asunto que todavía requiere investigación o revisión especializada.

## Práctica guiada

Construye una primera versión de **{specific_evidence}** siguiendo los {len(visual_steps)} pasos del diagrama. Bajo cada paso escribe una entrada, una operación y una salida. Marca con un signo de interrogación lo que todavía no conoces; no lo conviertas en cero, promedio o supuesto oculto.

Intercambia el trabajo con otra persona. Debe poder señalar dónde se comprueba **{critical_condition}** y reconstruir la transición desde **{visual_steps[2]}** hasta **{last_step}** sin explicación oral. Registra dos dudas de esa lectura y corrige al menos una. La primera versión, las objeciones y la versión revisada forman parte de la evidencia.

## Ejercicio autónomo

Aplica la secuencia **{sequence}** a otro contexto, escala o grupo de personas. Produce **{specific_evidence}**, una versión inicial y una revisada. Explica qué se mantuvo, qué cambió y por qué los parámetros del caso trabajado no podían copiarse.

**Evidencia mínima:** definición del problema, diagrama específico, producto reproducible, comprobación de la condición crítica y registro de revisión. Guarda el resultado en `evidence/{class_id}/evidencia.md` y enlázalo desde tu portafolio.

## Errores frecuentes y cómo corregirlos

- **Fallo crítico de esta clase:** {critical_condition.capitalize()}. Corrige localizando el paso que falta en la secuencia y vuelve a producir la evidencia.
- **Nombrar sin explicar:** una lista de conceptos no muestra mecanismos. Corrige dibujando relaciones y describiendo causa, consecuencia y límite.
- **Comparar fronteras distintas:** dos alternativas no responden a la misma función. Normaliza primero o declara la diferencia.
- **Confundir precisión con exactitud:** más decimales, polígonos o detalle visual no reparan un dato inadecuado.
- **Forzar lo desconocido a cero:** conserva el estado pendiente y decide cómo se resolverá.
- **Promediar una condición crítica:** seguridad, derechos o cumplimiento no desaparecen dentro de un puntaje total.
- **Citar sin alcance:** identifica documento, versión, sección consultada, función en la clase y límite.
- **Delegar el juicio:** software, IA o una guía apoyan el proceso; la responsabilidad y la validación deben permanecer asignadas.
- **Cerrar sin operación:** incorpora mantenimiento, accesibilidad, actualización y aprendizaje posterior.

## Evaluación y criterios de aceptación

La evidencia se acepta cuando:

1. produce **{specific_evidence}** y responde explícitamente a la pregunta central;
2. diferencia datos, requisitos, hipótesis, preferencias y desconocidos;
3. compara alternativas con función y fronteras equivalentes o justifica la diferencia;
4. permite reconstruir al menos una comprobación, incluidas unidades, versión y fuente;
5. conserva una condición crítica fuera de cualquier promedio compensatorio;
6. identifica responsabilidades y no atribuye al estudiante competencias profesionales reguladas;
7. incluye revisión sustantiva entre dos versiones y explica la consecuencia;
8. demuestra que **{critical_condition}** y enlaza la evidencia con `{following}`.

La rúbrica común complementa estos criterios. Una presentación convincente permanece pendiente si no supera una condición crítica o si la fuente no permite sostener la conclusión.

## Autoevaluación, recuperación y reflexión crítica

Sin mirar el texto, reconstruye la secuencia **{sequence}** y nombra la evidencia que produce cada transición. Explica por qué **{critical_condition}**. Si no puedes localizar esa comprobación en tu entrega, vuelve al diagrama y sustituye una afirmación vaga por una operación observable.

Para recuperar el aprendizaje, repite el ejercicio 24–48 horas después con otra escala o actor. Compara qué elementos del método se transfieren y qué parámetros deben volver a investigarse. Cierra con una reflexión breve: ¿quién recibe el beneficio, quién asume el costo, quién queda fuera de los datos y quién podrá corregir la decisión más adelante?

**Conexión siguiente:** `{following}` reutiliza la matriz, la representación y el registro de cambios. Lleva la evidencia, no las cifras del caso.

## Fuentes y alcance de uso

{source_block(source_ids[0])}

{source_block(source_ids[1])}
"""


def source_block(source_id: str) -> str:
    title, publisher, url, support, limit = SOURCES[source_id]
    return f"""### [[{source_id}]] {title}

{publisher}. [{url}]({url})

**Consulta:** página o documento oficial identificado en el enlace. **Apoyo:** {support} **Límite:** {limit} **Fecha de consulta:** 6 de octubre de 2026."""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Regenerate only the authored Phase III baseline before reapplying pedagogy.",
    )
    args = parser.parse_args()
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    preserved = [item for item in catalog if int(item["id"][4:]) <= 680]
    if len(preserved) != 680:
        raise SystemExit("Expected the preserved ARQ-001..680 baseline")
    additions = []
    number = 681
    for part, part_title, purpose, product, source_ids, titles in PARTS:
        if len(titles) != 10:
            raise SystemExit(f"Part {part} must define ten lessons")
        if len(LESSON_DESIGNS.get(part, [])) != 10:
            raise SystemExit(f"Part {part} must define ten distinct lesson designs")
        folder = ROOT / "classes" / f"parte-{part:02d}"
        folder.mkdir(parents=True, exist_ok=True)
        for title in titles:
            class_id = f"ARQ-{number:03d}"
            relative = f"classes/parte-{part:02d}/{class_id}.md"
            content = lesson_markdown(number, part, part_title, purpose, product, source_ids, title).rstrip() + "\n"
            path = ROOT / relative
            if path.exists():
                current = path.read_text(encoding="utf-8")
                base = re.sub(
                    r"\n?<!-- pedagogia-2026:inicio -->.*?<!-- pedagogia-2026:fin -->\n?",
                    "\n",
                    current,
                    flags=re.DOTALL,
                )
                base = re.sub(r"\n{3,}(## Fuentes y alcance de uso)", r"\n\n\1", base)
                if base.rstrip() != content.rstrip() and not args.refresh:
                    raise SystemExit(f"Refusing to overwrite edited lesson: {relative}")
                if base.rstrip() != content.rstrip() and args.refresh:
                    path.write_text(content, encoding="utf-8", newline="\n")
            else:
                path.write_text(content, encoding="utf-8", newline="\n")
            additions.append({"id": class_id, "title": title, "part": part, "is_new": True, "source": relative})
            number += 1
    if number != 801:
        raise SystemExit("Expansion must end at ARQ-800")
    CATALOG.write_text(json.dumps(preserved + additions, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    update_pedagogy()
    print("Generated 120 Phase III lessons, 2 studios and 21 specialization routes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
