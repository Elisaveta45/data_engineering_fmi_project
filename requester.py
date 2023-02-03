import requests
from retrying import retry

import config


def check_response(response):

    return response.status_code != 200


@retry(retry_on_result=check_response, stop_max_attempt_number=3, wait_fixed=2000)
def run_request():

    response = requests.get(
        config.URL,
        params={
            "from": config.FROM_DATE.strftime(config.DATE_FORMAT),
            "to": config.TO_DATE.strftime(config.DATE_FORMAT),
            "intervalMinutes": 60,
            "contextSite": "varmelast_dk",
        },
    )

    return response
