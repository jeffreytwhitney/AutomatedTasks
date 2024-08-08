import os.path
import shutil
from datetime import datetime

cur_date = datetime.now().strftime("%m_%d_%Y")
db_path = "X:\\Quality Calibration\\Project Management Database\\MPM_be.accdb"
output_path = f"X:\\Quality Calibration\\Work in Progress\\Jeffrey\\Backup\\MPM_be_{cur_date}.accdb"

if not os.path.exists(output_path):
    shutil.copy(db_path, output_path)
