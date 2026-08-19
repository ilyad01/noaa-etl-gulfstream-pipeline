import logging
import json

import xarray as xr

from config import (
    LOG_DIR,
    NOAA_URL,
    START_DATE,
    END_DATE,
    TARGET_LAT,
    TARGET_LON,
    OUTPUT_FILE,
    QUALITY_REPORT_FILE
)

from etl import (
    validate_parameters,
    run_pipeline
)

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "pipeline.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

def main():

    validate_parameters(
        START_DATE,
        END_DATE,
        TARGET_LAT,
        TARGET_LON
    )


    # Open NOAA dataset
    try:

        logger.info("Opening NOAA dataset...")
        with xr.open_dataset(NOAA_URL) as ds:
            logger.info("NOAA dataset opened successfully.")

            # Run pipeline
            df, quality_report = run_pipeline(
                ds,
                START_DATE,
                END_DATE,
                TARGET_LAT,
                TARGET_LON
            )

    except Exception as e:

        logger.error(f"Pipeline failed: {e}")
        raise

    # Save results to CSV
    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    logger.info(f"Data saved to {OUTPUT_FILE}")

    with open(QUALITY_REPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(
            quality_report,
            file,
            indent=4
        )

    logger.info(f"Quality report saved to {QUALITY_REPORT_FILE}")


if __name__ == "__main__":
    main()
