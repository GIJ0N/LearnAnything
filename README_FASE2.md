# Ruta adaptativo — Fase 2

Esta versión se construyó sobre `ruta_tutor_adaptativo_fase1.py`; no reemplaza ni borra tu archivo original. Corrige la integración del motor de decisión y la progresión de microtutoría.

## Instalar sin riesgo

Crea una carpeta nueva, por ejemplo:

```text
C:\Users\aris\Downloads\LearnAnythingV10_Fase2
```

Copia allí:

- `ruta_tutor_adaptativo_fase2.py`
- `test_fase2.py`
- `AUDITORIA_FASE2.md`
- `README_FASE2.md`

Detén cualquier servidor anterior con Ctrl+C. Ejecuta una línea por vez:

```powershell
python ruta_tutor_adaptativo_fase2.py --self-test
python test_fase2.py
python ruta_tutor_adaptativo_fase2.py
```

Abre `http://127.0.0.1:8765` en una sola pestaña. Exporta un respaldo antes de probar. Para verificar la nueva cobertura de forma limpia, crea una meta nueva.

## Cambio visible

Al fallar una pregunta del flujo principal, el sistema abre una intervención con causa registrada. Una microtutoría ya no se cierra después de un único acierto: pasa por **comprobación → práctica guiada → práctica independiente → regreso al problema original**. Usa una pista solo cuando hace falta; los aciertos guiados no cuentan como aplicación independiente.

Los tests no consumen Gemini. La calidad pedagógica real y la clasificación de Gemini aún requieren prueba con una meta no confidencial.
