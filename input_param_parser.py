import logging

from argparse import ArgumentParser
import config

logger = logging.getLogger(__name__)


def input_param_parser():
    arg_parser = ArgumentParser()

    arg_parser.add_argument(
        "--from_date", required=False, help=f"From Date: {config.DATE_FORMAT}."
    )

    arg_parser.add_argument(
        "--end_date", required=False, help=f"To Date: {config.DATE_FORMAT}."
    )

    arguments = arg_parser.parse_args()

    config.FROM_DATE = arguments.from_date
    config.END_DATE = arguments.end_date

    logger.info('  <<<Input parameters>>>')
    logger.info(f'[OPT] -Start date:                   {config.FROM_DATE}')
    logger.info(f'[OPT] -End date:                     {config.END_DATE}')
    logger.info('  <<<Input parameters>>>\n')

    return arguments
