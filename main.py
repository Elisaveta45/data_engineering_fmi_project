import logging

import pandas as pd
import requests

import config
from input_param_parser import input_param_parser

import worker


def main():
    start_date: pd.Timestamp = pd.to_datetime(config.FROM_DATE, format=config.DATE_FORMAT)
    end_date: pd.Timestamp = pd.to_datetime(config.END_DATE, format=config.DATE_FORMAT)

    if start_date is None and end_date is None:
        start_date = pd.Timestamp.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = pd.Timestamp.utcnow().replace(hour=23, minute=59, second=59, microsecond=999_999)
    elif start_date is None or end_date is None:
        raise ValueError("Please provide a value for both the -fd and -td arguments")

    logger.info(f"Running for date range start={start_date} -- end={end_date}")

    url = "/".join(
        ["http://www.varmelast.dk", "api", "v1", "heatdata", "historical", ]

    )

    r = requests.get(
        url,
        params={
            "from": start_date.strftime(config.DATE_FORMAT),
            "to": end_date.strftime(config.DATE_FORMAT),
            "intervalMinutes": 60,
            "contextSite": "varmelast_dk",
        },
    )

    data = r.json()
    df = worker.work(data)


if __name__ == "__main__":
    # handler = logging.StreamHandler()
    # handler.setFormatter(logging.Formatter(fmt=config.LOG_FORMAT_STRING))
    # logging.basicConfig(level=config.LOG_LEVEL, handlers=[handler])
    logger = logging.getLogger(__name__)

    args = input_param_parser()
    main()
