# NOAA Gulf Stream SST ETL Pipeline
## Project Overview

This project is a simple ETL pipeline built with Python that retrieves daily sea surface temperature (SST) data from NOAA, processes SST data for multiple geographic points along the Gulf Stream, performs basic quality checks, and saves the results to local files.

The project demonstrates a simple end-to-end data engineering workflow:

**Extract → Transform → Validate → Load**
## Data Source

The pipeline uses NOAA's publicly available daily NOAA OISST sea surface temperature dataset.

The dataset contains:

- Date
- Latitude
- Longitude
- Sea Surface Temperature (SST)

SST values are provided in degrees Celsius.

## Pipeline Workflow

### 1. Extract

The pipeline connects to the NOAA dataset and loads it using "xarray".

### 2. Transform

The pipeline generates a series of dates based on the configured date range and frequency.

For each date, SST data is extracted for multiple geographic points along the Gulf Stream using the nearest available grid points.

### 3. Validate

The pipeline performs several validation checks, including:

- Input parameter validation
- Date availability
- Missing SST values
- Data quality checks

A quality report is generated in JSON format.

### 4. Load

The processed result is saved as a CSV file.

The quality report is saved separately as a JSON file.

Pipeline execution details are also written to a log file.

## Project Structure
The project is organized into separate modules for configuration, pipeline logic, output files, and logging.
- config.py — pipeline configuration and parameters
- main.py — main entry point
- etl.py — ETL pipeline logic
- requirements.txt — Python dependencies
- output/ — generated CSV and JSON files
- logs/ — pipeline execution logs
- README.md — project documentation

## Configuration
Pipeline parameters are stored in config.py.

The main configuration parameters are:

- START_DATE — start date of the analysis period
- END_DATE — end date of the analysis period
- DATE_FREQUENCY — frequency used to select dates for analysis
- GULF_STREAM_POINTS — geographic points along the Gulf Stream
- OUTPUT_FILE — output CSV file
- QUALITY_REPORT_FILE — data quality report

## Installation
Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Running the Pipeline
Run the pipeline with:
```bash
python main.py
```
The pipeline will:
1. Validate the configuration parameters.
2. Load the NOAA dataset.
3. Extract the requested SST value.
4. Perform data quality checks.
5. Save the result to CSV.
6. Generate a quality report.
7. Write execution logs.

## Example Output
Example pipeline result:
```text
Date: 2026-08-01
Point: GS-1
Latitude: 32.125
Longitude: -77.875
SST: 28.4 °C
Status: success

Date: 2026-08-01
Point: GS-2
Latitude: 35.125
Longitude: -73.875
SST: 27.1 °C
Status: success
```

## Output Files
- `sst_data.csv` — contains SST data for multiple points along the Gulf Stream across the selected dates.
- `quality_report.json` — contains the results of the data quality checks.
- `pipeline.log` — contains information about pipeline execution, including processing steps and errors.

## Technologies
- Python
- Pandas
- Xarray
- NumPy
- NOAA data
- CSV
- JSON
- Logging

## Key Features
- ETL pipeline structure
- External scientific data source
- Parameter validation
- Data quality checks
- Error handling
- Logging
- Configuration management
- CSV and JSON output
- Modular Python code

## What This Project Demonstrates
- Building a modular ETL pipeline in Python
- Working with external scientific data sources
- Processing time series data for multiple geographic points
- Parameter validation and data quality checks
- Error handling and logging
- Configuration management
- Generating CSV and JSON outputs
- Preparing data for analytical visualization

## Purpose
This project was created as a practical example of a Python-based ETL pipeline for data engineering tasks.
It demonstrates how external data can be extracted, transformed, validated, and loaded into structured output files using Python.
