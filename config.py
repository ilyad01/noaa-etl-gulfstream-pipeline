# =========================
# Configuration
# =========================

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

NOAA_URL = "http://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2026.nc"

START_DATE = "2026-08-01"
END_DATE = "2026-08-12"

TARGET_LAT = 40.0
TARGET_LON = -70.0

OUTPUT_FILE = BASE_DIR / "output" / "sst_data.csv"
QUALITY_REPORT_FILE = BASE_DIR / "output" / "quality_report.json"
LOG_DIR = BASE_DIR / "logs"