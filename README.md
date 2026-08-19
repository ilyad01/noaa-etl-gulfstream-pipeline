# NOAA Gulf Stream SST ETL Pipeline
## Project Overview

This project is a simple ETL pipeline built with Python that retrieves daily sea surface temperature (SST) data from NOAA, processes the data, performs basic quality checks, and saves the results to local files.

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

The required date and geographic coordinates are selected from the dataset.

The pipeline extracts the corresponding SST value for the requested location.

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

- TARGET_LAT — target latitude
- TARGET_LON — target longitude
- START_DATE — start date of the dataset
- END_DATE — end date of the dataset
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
Date: 2026-08-12T00:00:00
Latitude: 40.125
Longitude: -69.875
SST: 25.09 °C
```

## Output Files
sst_data.csv — contains the processed SST result for the requested location and date.
quality_report.json — contains the results of the data quality checks.
pipeline.log — contains information about pipeline execution, including processing steps and errors.

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

## Purpose
This project was created as a practical example of a Python-based ETL pipeline for data engineering tasks.
It demonstrates how external data can be extracted, transformed, validated, and loaded into structured output files using Python.
