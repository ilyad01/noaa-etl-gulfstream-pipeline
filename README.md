# NOAA Sea Surface Temperature ETL Pipeline

## Project Overview

This project is a Python-based ETL pipeline for extracting, transforming,
validating, and storing daily Sea Surface Temperature (SST) data from NOAA.

The pipeline retrieves SST data for a specified geographic location and date
range, performs basic data quality checks, and saves the processed data to CSV.

## Architecture

The project follows a simple ETL architecture:

NOAA NetCDF Dataset
        |
        v
   Data Extraction
        |
        v
   Data Transformation
        |
        v
   Data Quality Checks
        |
        +----> CSV output
        |
        +----> Quality report
        |
        +----> Pipeline log

The project separates configuration, ETL logic, and pipeline orchestration
into dedicated modules.

- `config.py` — configuration parameters and file paths
- `etl.py` — data validation, extraction, transformation and quality checks
- `main.py` — pipeline orchestration and output management

## Data Source

The project uses the NOAA High-resolution Blended Analysis dataset.

The dataset provides daily Sea Surface Temperature data on a 0.25° spatial grid.

## Technologies

- Python
- Pandas
- NumPy
- Xarray
- NetCDF4
- NOAA NetCDF data

## Pipeline

The pipeline consists of the following steps:

1. Validate input parameters
2. Open the NOAA dataset
3. Select the requested date
4. Find the nearest available grid point
5. Extract Sea Surface Temperature
6. Handle missing values
7. Generate a data quality report
8. Save the processed data to CSV

## Project Structure

etl_gulfstream/
├── main.py
├── config.py
├── etl.py
├── requirements.txt
├── README.md
├── .gitignore
└── output/
    └── sst_data.csv

Configuration

The main parameters are defined in config.py:

Start date
End date
Latitude
Longitude
NOAA dataset URL
Output file

Example:

START_DATE = "2026-08-01"
END_DATE = "2026-08-12"

TARGET_LAT = 40.0
TARGET_LON = -70.0

Output

The pipeline produces a CSV file containing:

Date
Requested latitude
Requested longitude
Actual grid latitude
Actual grid longitude
SST
Status

Example:

date,requested_lat,requested_lon,actual_lat,actual_lon,sst,status
2026-08-12,40.0,-70.0,40.125,-69.875,25.09,success

Data Quality

The pipeline identifies several possible statuses:

success — SST value successfully retrieved
sst_missing — SST value is missing
date_not_available — requested date is not available

A quality report provides the number of records processed and the number
of successful and unsuccessful records.

Installation

Create a virtual environment:

python -m venv .venv

Activate the environment and install dependencies:

pip install -r requirements.txt
```

Usage

Run the pipeline with:

python main.py

The processed data will be saved to the configured output file.

                 NOAA NetCDF
                      │
                      ▼
               ┌─────────────┐
               │   main.py   │
               │ Orchestration│
               └──────┬──────┘
                      │
                      ▼
               ┌─────────────┐
               │    etl.py   │
               │             │
               │ Validation  │
               │ Extraction  │
               │ Transform   │
               │ Data Quality│
               └──────┬──────┘
                      │
                      ▼
                pandas DataFrame
                      │
             ┌────────┴────────┐
             ▼                 ▼
          CSV output      Quality report