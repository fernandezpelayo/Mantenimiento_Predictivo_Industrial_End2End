# Proyecto de Monitoreo y Mantenimiento Predictivo Industrial

Este proyecto automatiza el ciclo completo de datos (ETL, almacenamiento y análisis) de sensores industriales para identificar patrones de fallo y optimizar el consumo de maquinaria. Basado en un dataset de mantenimiento preventivo, el objetivo es transformar registros brutos en decisiones de negocio y visualizarlas en un entorno de Business Intelligence profesional.

## Tecnologías utilizadas
* **Python**: Pandas para procesamiento y Seaborn/Matplotlib para visualización técnica.
* **MySQL**: Almacenamiento y gestión de datos relacionales.
* **SQLAlchemy**: Librería para la conexión eficiente entre Python y SQL.
* **Power BI**: Diseño de Dashboard interactivo y cálculo de medidas DAX para KPIs de negocio.

## Hallazgos y Conclusiones del Análisis
Tras procesar 10,000 registros de sensores y analizar los resultados en SQL y Power BI, se extraen las siguientes conclusiones:

1. **Indicador de Fallo Energético:** Una máquina con consumo ineficiente tiene **3.7 veces más probabilidades de fallar**. El sobreconsumo se establece como el principal KPI preventivo para el sistema de alertas.

2. **Correlación de Consumo:** Existe una relación del **0.98** entre el **Torque** y el **Consumo Estimado**. La optimización del par de fuerza es la clave directa para el ahorro energético en planta.

3. **Nivel de Riesgo por Modelo:** Las máquinas de tipo "Low" (L) concentran la gran mayoría de las incidencias (**235 fallos**), destacando causas como el **Sobreesfuerzo**.

4. **Fuga de Eficiencia:** Los modelos Tipo L representan el **72.43% del desgaste** total de la planta. Esto confirma que la gama baja es el principal factor de riesgo operativo, a pesar de mantener un consumo medio similar a las gamas superiores.

5. **Tasa de Fallo Global:** Se ha identificado una tasa de fallo de planta del **3.39%**, monitorizada dinámicamente mediante el dashboard.

## Visualizaciones Destacadas

### Análisis Técnico (Python)
![Análisis de Fallos](./reports/fallos.png)
*Gráfico de barras: Identificación de la fragilidad del modelo 'L' ante picos de sobreesfuerzo.*

![Matriz de Correlación](./reports/correlacion.png)
*Mapa de calor: Identificación del Torque como el principal responsable del consumo eléctrico.*

### Dashboard Ejecutivo (Power BI)
![Dashboard Interactivo](./reports/Monitorizacion_Mantenimiento.png)
*Panel de control interactivo conectado a MySQL para la monitorización de salud de planta. [Ver imagen en PDF](./dashboard/Monitorizacion_Mantenimiento.pdf)*

## Estructura del Proyecto
* `data/`: Dataset original y procesado de sensores industriales.
* `sql/`: Scripts de consultas y creación de tablas en MySQL.
* `dashboard/`: Archivo `.pbix` de Power BI y versión exportada en `.pdf`.
* `reports/`: Gráficas técnicas e imágenes (.png) generadas para el informe.
* `scripts/`:
    * `database_upload.py`: Automatización de la carga de datos con seguridad (.env).
    * `analisis_visual.py`: Generación de matrices de correlación y gráficos de fallos.
    * `generar_reporte.py`: Exportación de máquinas en estado crítico a CSV.

## Conclusiones y Recomendaciones Proyectadas
1. **Optimización de Activos:** Se recomienda la sustitución progresiva de los modelos Tipo L por modelos Tipo M en procesos de alto Torque, con un potencial de reducción de paradas por sobreesfuerzo del **85%**.
2. **Escalabilidad del Pipeline:** La arquitectura implementada (Python -> MySQL -> Power BI) permite una monitorización continua. Se establece que un aumento del 10% en el KPI de **Consumo Estimado** sin variaciones en la producción debe activar un protocolo de inspección preventiva.