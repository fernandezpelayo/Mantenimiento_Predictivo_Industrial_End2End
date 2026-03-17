USE mantenimiento_industrial;

-- Verificación inicial de la carga de datos
SELECT * FROM monitoreo_maquinas LIMIT 10;
DESCRIBE monitoreo_maquinas;

-- Análisis de eficiencia energética y costes por categoría de máquina
SELECT 
    Tipo,
    ROUND(SUM(Consumo_Estimado), 2) AS Consumo_Total,
    ROUND(AVG(Consumo_Estimado), 2) AS Consumo_Medio
FROM
    monitoreo_maquinas
GROUP BY Tipo
ORDER BY Consumo_Total DESC;

-- Diagnóstico de fiabilidad: Relación entre fallos, temperatura y consumo anómalo
SELECT 
    Tipo,
    SUM(Fallo) AS Total_Fallos,
    ROUND(AVG(Temp_Proceso), 2) AS Temp_Media_Proceso
FROM
    monitoreo_maquinas
GROUP BY Tipo
ORDER BY Total_Fallos DESC;

SELECT 
    Gasto_Excesivo,
    COUNT(*) AS Cantidad_Maquinas,
    SUM(Fallo) AS Total_Fallos,
    ROUND(AVG(Temp_Proceso), 2) AS Temp_Media
FROM
    monitoreo_maquinas
GROUP BY Gasto_Excesivo;
