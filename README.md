# Análisis de Mantenimiento y Eficiencia Energética

Este proyecto analiza un dataset de mantenimiento industrial para identificar patrones de fallo y optimizar el consumo eléctrico de la maquinaria.

## Fase 1: Preparación y limpieza de datos (Python)

En esta primera etapa, he procesado los datos brutos utilizando Python y la librería Pandas para asegurar su calidad y extraer métricas de valor:

* **Limpieza y normalización:** He eliminado las columnas de identificación que no aportaban valor estadístico y he renombrado las variables para facilitar su manipulación.

* **Ingeniería de variables:** He calculado una estimación de consumo energético (kWh) combinando los datos de Torque y Velocidad.

* **Detección de ineficiencias:** He creado una lógica para identificar automáticamente las máquinas que operan con un gasto superior a la media de la planta.


## Fase 2: Análisis de Datos con SQL

En esta etapa, he migrado los datos limpios a **MySQL** para realizar un análisis de patrones de fallo. Mi objetivo ha sido cruzar la eficiencia energética con la operatividad real para extraer conclusiones accionables:

### Mis conclusiones del análisis:

**1. Distribución de carga y consumo**
He observado que las máquinas **Tipo L (Low)** soportan el mayor peso de la planta, con un consumo acumulado de **359,975 unidades**. Aunque el gasto medio es similar en todas las categorías (~60 unidades), el volumen de estas máquinas las convierte en el punto crítico para cualquier estrategia de ahorro energético.

**2. Relación entre eficiencia y fiabilidad**
Los datos revelan una conexión clara entre el consumo anómalo y las averías:
* He identificado que las máquinas con **Gasto Excesivo** acumulan **268 fallos**, frente a solo **71** registrados en las máquinas eficientes.
* **Resultado:** He determinado que una máquina ineficiente tiene **3.7 veces más probabilidades** de fallar, lo que convierte al sobreconsumo en mi KPI principal para alertas preventivas.

**3. Patrones de temperatura y criticidad por modelo**
He analizado la temperatura en los momentos de fallo, situándose de media en los **310 K**. Al ser un valor tan estable en todos los tipos de máquina, concluyo que el riesgo no es puramente térmico, sino que está ligado a la carga de trabajo:
* Las máquinas **Tipo L** concentran la gran mayoría de las incidencias con **235 fallos**.
* Por el contrario, las máquinas **Tipo H** demuestran ser las más fiables con solo **21 fallos**, confirmando que el diseño térmico es consistente en toda la flota pero el desgaste varía según el modelo.

## Próximas Fases del Proyecto
* **Fase 3:** Visualización avanzada de distribuciones y correlaciones con Python (Seaborn/Matplotlib).
* **Fase 4:** Diseño de un Dashboard interactivo en Power BI conectado a la base de datos SQL.