import pandas as pd
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "mantenimiento.csv"
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)
PASSWORD = os.getenv('DB_PASSWORD')

df = pd.read_csv(DATA_PATH)

# Limpieza y renombrado de columnas
df_mantenimiento = df.drop(df.columns[[0, 1]], axis=1)
df_mantenimiento.columns = [
    'Tipo', 'Temp_Aire', 'Temp_Proceso', 'Velocidad',
    'Torque', 'Desgaste', 'Fallo', 'Tipo_Fallo']

# Nuevo índice de esfuerzo mecánico
df_mantenimiento['Indice_Esfuerzo_Mecanico'] = (
    df_mantenimiento['Torque'] * df_mantenimiento['Velocidad'])

engine = create_engine(
    f"mysql+pymysql://root:{PASSWORD}@localhost:3306")

with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS mantenimiento_industrial"))
    conn.commit()


df_mantenimiento.to_sql(
    'monitoreo_maquinas',
    con=engine,
    schema='mantenimiento_industrial',
    if_exists='replace',
    index=False)

print("ÉXITO: Datos cargados correctamente desde cualquier ubicación.")
