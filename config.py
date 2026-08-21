# =========================
# Configuration
# =========================

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

NOAA_URL = "http://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2026.nc"

START_DATE = "2026-07-01"
END_DATE = "2026-08-12"
DATE_FREQUENCY = "5D"

GULF_STREAM_POINTS = [
    {"name": "GS-1", "lat": 32.0, "lon": -78.0},
    {"name": "GS-2", "lat": 35.0, "lon": -74.0},
    {"name": "GS-3", "lat": 38.0, "lon": -65.0},
    {"name": "GS-4", "lat": 39.5, "lon": -58.0},
    {"name": "GS-5", "lat": 39.5, "lon": -51.0},
]
OUTPUT_FILE = BASE_DIR / "output" / "sst_data.csv"
QUALITY_REPORT_FILE = BASE_DIR / "output" / "quality_report.json"
LOG_DIR = BASE_DIR / "logs"