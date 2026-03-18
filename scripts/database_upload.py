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

df_mantenimiento = df.drop(df.columns[[0, 1]], axis=1)
df_mantenimiento.columns = ['Tipo', 'Temp_Aire', 'Temp_Proceso', 'Velocidad', 'Torque', 'Desgaste', 'Fallo', 'Tipo_Fallo']

df_mantenimiento['Consumo_Estimado'] = (df_mantenimiento['Torque'] * df_mantenimiento['Velocidad']) / 1000

engine = create_engine(f'mysql+pymysql://root:{PASSWORD}@localhost:3306')

with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS mantenimiento_industrial"))
    conn.commit()

df_mantenimiento.to_sql('monitoreo_maquinas', con=engine, schema='mantenimiento_industrial', if_exists='replace', index=False)

print("EXITO: Datos cargados correctamente desde cualquier ubicación.")