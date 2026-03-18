import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")
PASSWORD = os.getenv('DB_PASSWORD')

DB_URL = f'mysql+pymysql://root:{PASSWORD}@localhost:3306/mantenimiento_industrial'
engine = create_engine(DB_URL)

df = pd.read_sql("SELECT * FROM monitoreo_maquinas", con=engine)

# Filtrar máquinas en riesgo
critico = df[(df['Desgaste'] > 180) | (df['Torque'] > 60)]

critico.to_csv(BASE_DIR / 'reporte_mantenimiento_critico.csv', index=False)

print(f"Reporte generado: {len(critico)} máquinas requieren revisión.")