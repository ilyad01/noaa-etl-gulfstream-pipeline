# NOAA Gulf Stream SST ETL Pipeline

A Python-based ETL pipeline for extracting and processing Sea Surface Temperature (SST) data from NOAA.

The project demonstrates an end-to-end data processing workflow including data extraction, parameter validation, transformation, data quality checks, logging, and output generation.

## Project Overview

The pipeline retrieves daily Sea Surface Temperature data for a specified date and geographic location.

### ETL Workflow

1. **Extract** – retrieve SST data from NOAA
2. **Validate** – validate input parameters and data availability
3. **Transform** – select and process data for the requested coordinates and date
4. **Quality Check** – validate the processed data and generate a quality report
5. **Load** – save the processed result to the output directory
6. **Logging** – record pipeline execution and errors

## Technologies

- **Python 3**
- **Xarray** – processing multidimensional scientific datasets
- **Pandas** – data processing and transformation
- **NumPy** – numerical operations
- **JSON** – quality reporting
- **Python Logging** – execution monitoring
- **NOAA** – external data source

## Data Source

The project uses NOAA Sea Surface Temperature data.

The dataset contains daily SST measurements with the following main dimensions:

- `time`
- `latitude`
- `longitude`

SST values are provided in degrees Celsius.

## Project Structure

```text
noaa-etl-gulfstream-pipeline/
│
├── output/           # Processed data and quality reports
│
├── .gitignore
├── README.md
├── config.py         # Pipeline configuration
├── etl.py            # ETL and data processing logic
├── main.py           # Pipeline entry point
└── requirements.txt  # Python dependencies

Configuration

Pipeline parameters are defined in config.py.

Example parameters include:

START_DATE = ...
END_DATE = ...


TARGET_LAT = ...
TARGET_LON = ...


OUTPUT_FILE = ...
QUALITY_REPORT_FILE = ...

This allows the pipeline to be executed with different dates and geographic coordinates without changing the core ETL logic.

Data Validation

The pipeline performs validation checks for:

required parameters
date availability in the source dataset
geographic coordinates
missing SST values
invalid or missing source data
output data consistency

If the requested date is not available in the source dataset, the pipeline returns an appropriate status instead of failing unexpectedly.

Data Quality Report

After processing, the pipeline generates a JSON quality report in the output directory.

The report contains information about the pipeline execution and validation results.

Example:

{
    "status": "success",
    "records_processed": 1,
    "quality_checks": "passed"
}
Logging

The pipeline uses Python's built-in logging module to record execution details.

The logs provide information about:

pipeline start and completion
validation results
data processing steps
errors and exceptions
output file generation

This makes the pipeline easier to monitor and troubleshoot.

Example Output

For a requested date and geographic location, the pipeline can produce an SST result similar to:

Date: 2026-08-12T00:00:00
Latitude: 40.125
Longitude: 290.125
SST: 25.09 °C
How to Run

Install the required dependencies:

pip install -r requirements.txt

Configure the required parameters in config.py.

Run the pipeline:

python main.py

The processed data and quality report will be generated in the output directory.

Key Skills Demonstrated
Python ETL development
External data ingestion
Multidimensional data processing
Data validation
Data quality monitoring
Error handling
Logging
Configuration management
JSON-based reporting
Modular pipeline design
Future Improvements

Possible extensions of the project include:

scheduled pipeline execution
storing processed data in a database
unit and integration tests
Docker containerization
CI/CD with GitHub Actions
processing multiple geographic locations
adding data visualization

Author

Ilya Davidovich

Data Engineer / Data Analyst