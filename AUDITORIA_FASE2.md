# Auditoría e integración — Fase 2

## Punto de partida auditado

Se tomó `ruta_tutor_adaptativo_fase1.py`, no una reconstrucción. Conservaba: servidor Python local, mapa inicial, cobertura persistente, diagnóstico, lecciones con explicación/ejemplo/prácticas, evaluación por Gemini, repaso, respaldo local y pila recursiva de contextos. La Fase 1 ya registraba `nextIntervention()`, pero no ejecutaba consistentemente esa decisión; su cobertura podía marcar dominio con un solo acierto; y el microcontexto se cerraba tras un único resultado correcto.

## Cambios implementados

1. **Motor conectado al flujo real.** Los fallos no correctos de fases principales pasan por `openIntervention()`, que usa `nextIntervention()` y guarda `decision`, fase original, pregunta padre y error. La decisión visible acompaña la microtutoría.
2. **Suficiencia de evidencia.** La evidencia incluye fase, ayuda, independencia y variación. Una dimensión de aplicación/procedimiento requiere un acierto independiente. Transferencia requiere tarea independiente y variada. Memoria exige repaso. Esto evita marcar dominio solo por una respuesta guiada.
3. **Microtutoría escalonada.** Cada intervención tiene CHECK, GUIDED e INDEPENDENT. CHECK muestra explicación y ejemplo; GUIDED permite pista; INDEPENDENT exige aplicación sin contar la ayuda anterior como independencia. Solo entonces vuelve al problema original. Esto usa la pila existente, no una nueva arquitectura.
4. **Causa a intervención.** Errores de álgebra, aritmética, unidades, selección de fórmula o variables se etiquetan como intervención dirigida; conceptual pide explicación antes de práctica; memoria pide reparación de recuperación; aplicación/transferencia pide práctica contextual. La generación del microcontexto aún usa una llamada.
5. **Cobertura honesta.** Actualiza dimensiones solo si existen y la actividad pudo aportar la clase de evidencia correspondiente. Un tipo de error no degrada automáticamente todo el componente.

## Lo que sigue parcial

- `nextIntervention` selecciona familias de intervención, pero aún no genera por separado un diagrama, analogía, comparación, actividad de clasificación o ejemplo parcialmente completado.
- La causa sigue siendo la hipótesis de Gemini; no existe verificador simbólico de unidades/álgebra.
- La actividad independiente reutiliza la pregunta micro existente; una Fase 3 debe generar una variante solo cuando se requiera evidencia de transferencia, sin llamar más de lo necesario.
- Confianza declarada, interleaving, revisión de estabilidad personalizada, modo enseñar y proyectos no se implementaron; son fases posteriores.
- MAP UPDATE registra la razón, pero aún no inserta automáticamente nodos generados; requiere revisión para no contaminar el grafo.

## Riesgos

La misma clave local de navegador carga metas antiguas. Los campos nuevos son defensivos, pero una meta antigua no tendrá coverage rico: crea una nueva para prueba. Múltiples pestañas pueden sobrescribir estado. No se verificó una sesión real con Gemini, cuota o latencia.

## Pruebas ejecutadas

- Autotest de la aplicación: OK.
- `test_fase2.py`: mapa, dimensiones, MAP UPDATE y respuesta «No sé» local: OK.
- Sintaxis JavaScript: OK.
- Pruebas sin Gemini; no prueban calidad de generación ni aprendizaje real.

## Escenario esperado

Meta: resolver F=ma. Si el alumno conoce la ley pero falla despeje, se registra `TARGETED_MICRO`; la intervención explica el despeje, ofrece ejemplo, comprobación, guiada e independiente. Al superar independiente, regresa al problema padre. El conocimiento conceptual de F=ma no se vuelve desconocido por un fallo de álgebra. Si el alumno falla identificación de fuerzas, se abre otra intervención dirigida, no una repetición de F=ma.
