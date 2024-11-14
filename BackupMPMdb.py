import os
import shutil
from datetime import datetime

cur_date = datetime.now().strftime("%m_%d_%Y_%H-%M-%S")
db_path = "X:\\Quality Calibration\\Project Management Database\\MPM_be.accdb"
output_path = f"X:\\Quality Calibration\\Project Management Database\\Database Backup\\MPM_be_{cur_date}.accdb"

for filename in sorted(os.scandir("X:\\Quality Calibration\\Project Management Database\\Database Backup\\"),
                       key=lambda x: x.stat().st_mtime, reverse=True)[9:]:
    filename_relPath = os.path.join("X:\\Quality Calibration\\Project Management Database\\Database Backup\\", filename)
    os.remove(filename_relPath)

if not os.path.exists(output_path):
    shutil.copy(db_path, output_path)
