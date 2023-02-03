import unittest
from unittest.mock import patch
from datetime import datetime
import config
from input_param_parser import input_param_parser


class TestInputParamParser(unittest.TestCase):
    def test_from_and_to_date(self):
        with patch(
            "sys.argv",
            [
                "input_param_parser",
                "--from_date",
                "2023-01-30",
                "--to_date",
                "2023-01-31",
            ],
        ):
            args = input_param_parser()
            self.assertEqual(
                config.FROM_DATE, datetime.strptime("2023-01-30", config.DATE_FORMAT)
            )
            self.assertEqual(
                config.TO_DATE, datetime.strptime("2023-01-31", config.DATE_FORMAT)
            )
            self.assertEqual(args.from_date, "2023-01-30")
            self.assertEqual(args.to_date, "2023-01-31")

    def test_from_date_only(self):
        with patch("sys.argv", ["input_param_parser", "--from_date", "2023-01-30"]):
            self.assertRaises(ValueError, input_param_parser)

    def test_to_date_only(self):
        with patch("sys.argv", ["input_param_parser", "--to_date", "2023-01-30"]):
            self.assertRaises(ValueError, input_param_parser)

    def test_no_date_provided(self):
        with patch("sys.argv", ["input_param_parser"]):
            args = input_param_parser()
            self.assertEqual(
                config.FROM_DATE,
                datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0),
            )
            self.assertEqual(
                config.TO_DATE,
                datetime.utcnow().replace(
                    hour=23, minute=59, second=59, microsecond=999_999
                ),
            )
            self.assertEqual(args.from_date, None)
            self.assertEqual(args.to_date, None)
