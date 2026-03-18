import pandas as pd
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv('DB_PASSWORD')

try:
    df = pd.read_csv('data/mantenimiento.csv')
except FileNotFoundError:
    df = pd.read_csv('mantenimiento.csv')

df_mantenimiento = df.drop(df.columns[[0, 1]], axis=1)
df_mantenimiento.columns = ['Tipo', 'Temp_Aire', 'Temp_Proceso', 'Velocidad', 'Torque', 'Desgaste', 'Fallo', 'Tipo_Fallo']

df_mantenimiento['Consumo_Estimado'] = (df_mantenimiento['Torque'] * df_mantenimiento['Velocidad']) / 1000

engine = create_engine(f'mysql+pymysql://root:{PASSWORD}@localhost:3306')

with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS mantenimiento_industrial"))
    conn.commit()

df_mantenimiento.to_sql('monitoreo_maquinas', con=engine, schema='mantenimiento_industrial', if_exists='replace', index=False)

print("EXITO: Datos en MySQL.")