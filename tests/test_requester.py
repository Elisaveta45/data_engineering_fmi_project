import unittest
import requester
import config
from datetime import datetime


class TestRunRequest(unittest.TestCase):
    def test_run_request(self):
        config.FROM_DATE = datetime.strptime("2023-01-30", config.DATE_FORMAT)
        config.TO_DATE = datetime.strptime("2023-01-31", config.DATE_FORMAT)

        response = requester.run_request()

        self.assertEqual(response.status_code, 200)
