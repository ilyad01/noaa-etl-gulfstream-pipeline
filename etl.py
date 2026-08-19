import logging

import numpy as np
import pandas as pd

# =========================
# Functions
# =========================

logger = logging.getLogger(__name__)


def validate_parameters(start_date, end_date, target_lat, target_lon):

    # Validate dates
    try:
        start_date = pd.Timestamp(start_date)
        end_date = pd.Timestamp(end_date)
    except Exception:
        raise ValueError("Invalid date format.")

    if start_date > end_date:
        raise ValueError("START_DATE cannot be later than END_DATE.")

    # Validate latitude
    if not -90 <= target_lat <= 90:
        raise ValueError("Latitude must be between -90 and 90.")

    # Validate longitude
    if not -180 <= target_lon <= 180:
        raise ValueError("Longitude must be between -180 and 180.")

    logger.info("Input parameters validated successfully.")


def get_sst(ds, target_date, target_lat, target_lon):

    target_date = pd.Timestamp(target_date)

    # Save requested coordinates
    requested_lat = target_lat
    requested_lon = target_lon

    # NOAA uses longitude values from 0 to 360.
    # Convert user input from -180...180 to NOAA format.
    if target_lon < 0:
        target_lon = target_lon + 360

    # Check date
    if target_date not in ds.time.values:

        logger.warning(
            f"Date {target_date.date()} is not available in the dataset."
        )

        return {
            "date": target_date,
            "requested_lat": requested_lat,
            "requested_lon": requested_lon,
            "actual_lat": np.nan,
            "actual_lon": np.nan,
            "sst": np.nan,
            "status": "date_not_available"
    }

    # Select nearest grid point
    point = ds["sst"].sel(
        time=target_date,
        lat=target_lat,
        lon=target_lon,
        method="nearest"
    )

    # Get actual coordinates selected by NOAA
    actual_lat = point.lat.values.item()
    actual_lon = point.lon.values.item()

    # Get SST value
    sst_value = point.values.item()

    # Check missing value
    if np.isnan(sst_value):

        logger.warning(
            f"SST data missing for date {target_date.date()} "
            f"at location {requested_lat}, {requested_lon}"
        )

        return {
            "date": target_date,
            "requested_lat": requested_lat,
            "requested_lon": requested_lon,
            "actual_lat": actual_lat,
            "actual_lon": actual_lon,
            "sst": np.nan,
            "status": "sst_missing"
        }

    # Convert selected NOAA longitude back to -180...180
    # for the output.
    if actual_lon > 180:
        actual_lon = actual_lon - 360

    return {
        "date": point.time.values,
        "requested_lat": requested_lat,
        "requested_lon": requested_lon,
        "actual_lat": actual_lat,
        "actual_lon": actual_lon,
        "sst": sst_value,
        "status": "success"
    }


def get_sst_timeseries(ds, dates, target_lat, target_lon):

    results = []

    for date in dates:

        result = get_sst(
            ds,
            date,
            target_lat,
            target_lon
        )

        results.append(result)

    return results


def run_pipeline(ds, start_date, end_date, target_lat, target_lon):

    logger.info(
        f"Starting pipeline for {start_date} to {end_date}, "
        f"location: {target_lat}, {target_lon}"
    )

    dates = pd.date_range(
        start=start_date,
        end=end_date,
        freq="D"
    )

    results = get_sst_timeseries(
        ds,
        dates,
        target_lat,
        target_lon
    )

    df = pd.DataFrame(results)

    df["date"] = pd.to_datetime(df["date"]).dt.date

    # Data quality check
    quality_report = generate_quality_report(df)

    logger.info(f"Pipeline completed. Records processed: {len(df)}")

    logger.info(f"Status summary:\n{df['status'].value_counts().to_string()}")

    return df, quality_report


def generate_quality_report(df):

    total_records = len(df)
    successful_records = (df["status"] == "success").sum()
    missing_records = (df["status"] == "sst_missing").sum()
    unavailable_dates = (df["status"] == "date_not_available").sum()

    logger.info(f"Total records: {total_records}")
    logger.info(f"Successful records: {successful_records}")
    logger.info(f"Missing SST: {missing_records}")
    logger.info(f"Unavailable dates: {unavailable_dates}")

    return {
        "total_records": int(total_records),
        "successful_records": int(successful_records),
        "missing_sst": int(missing_records),
        "unavailable_dates": int(unavailable_dates)
    }
