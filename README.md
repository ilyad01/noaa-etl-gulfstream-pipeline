NOAA Gulf Stream SST ETL Pipeline
Project Overview

This project is a simple ETL pipeline built with Python that retrieves daily sea surface temperature (SST) data from NOAA, processes the data, performs basic quality checks, and saves the results to local files.

The project demonstrates a simple end-to-end data engineering workflow:

Extract → Transform → Validate → Load

Data Source

The pipeline uses NOAA's publicly available sea surface temperature dataset.

The dataset contains:

Date
Latitude
Longitude
Sea Surface Temperature (SST)

SST values are provided in degrees Celsius.

Project Structure
noaa-etl-gulfstream-pipeline/
│
├── config.py
├── main.py
├── pipeline.py
├── requirements.txt
├── README.md
│
├── output/
│   ├── sst_result.csv
│   └── quality_report.json
│
└── logs/
    └── pipeline.log
Pipeline Workflow
1. Extract

The pipeline downloads the NOAA dataset and loads it using xarray.

2. Transform

The required date and geographic coordinates are selected from the dataset.

The pipeline extracts the corresponding SST value for the requested location.

3. Validate

The pipeline performs several validation checks, including:

Input parameter validation
Date availability
Missing SST values
Data quality checks

A quality report is generated in JSON format.

4. Load

The processed result is saved as a CSV file.

The quality report is saved separately as a JSON file.

Pipeline execution details are also written to a log file.

Configuration

Pipeline parameters are stored in config.py.

Example parameters include:

TARGET_LAT = 40.125
TARGET_LON = 290.125


START_DATE = "2026-01-01"
END_DATE = "2026-08-12"


OUTPUT_FILE = "output/sst_result.csv"
QUALITY_REPORT_FILE = "output/quality_report.json"
Installation

Clone the repository and install the required Python packages:

pip install -r requirements.txt
Running the Pipeline

Run the pipeline with:

python main.py

The pipeline will:

Validate the configuration parameters.
Load the NOAA dataset.
Extract the requested SST value.
Perform data quality checks.
Save the result to CSV.
Generate a quality report.
Write execution logs.
Example Output

Example pipeline result:

Date: 2026-08-12T00:00:00
Latitude: 40.125
Longitude: 290.125
SST: 25.09 °C
Output Files
sst_result.csv

Contains the processed SST result for the requested location and date.

quality_report.json

Contains the results of the data quality checks performed during the pipeline execution.

pipeline.log

Contains information about pipeline execution, including processing steps and errors.

Technologies
Python
Pandas
Xarray
NumPy
NOAA data
CSV
JSON
Logging
Key Features
ETL pipeline structure
External scientific data source
Parameter validation
Data quality checks
Error handling
Logging
Configuration management
CSV and JSON output
Modular Python code
Purpose

This project was created as a practical example of a Python-based ETL pipeline for data engineering tasks.

It demonstrates how external data can be extracted, transformed, validated, and loaded into structured output files using Python.
