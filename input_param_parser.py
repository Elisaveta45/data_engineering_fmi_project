from argparse import ArgumentParser
import config
from datetime import datetime


def input_param_parser():
    arg_parser = ArgumentParser()

    arg_parser.add_argument(
        "--from_date", required=False, help=f"From Date: {config.DATE_FORMAT}."
    )

    arg_parser.add_argument(
        "--to_date", required=False, help=f"To Date: {config.DATE_FORMAT}."
    )

    arguments = arg_parser.parse_args()

    config.FROM_DATE = arguments.from_date
    config.TO_DATE = arguments.to_date

    if arguments.from_date is None and arguments.to_date is None:
        config.FROM_DATE = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        config.TO_DATE = datetime.utcnow().replace(hour=23, minute=59, second=59, microsecond=999_999)
    elif arguments.from_date is None or arguments.to_date is None:
        raise ValueError("Please provide a value for both the --from_date and --to_date arguments")
    else:
        config.FROM_DATE = datetime.strptime(config.FROM_DATE, config.DATE_FORMAT)
        config.TO_DATE = datetime.strptime(config.TO_DATE, config.DATE_FORMAT)

    return arguments
