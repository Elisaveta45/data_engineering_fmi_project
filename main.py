import unittest

import worker
import config
from input_param_parser import input_param_parser
from requester import run_request
from visualization import create_plot
from tests.test_worker import TestProscessData
from tests.test_requester import TestRunRequest
from tests.test_input_parameter_data_type import TestGetListOfWantedCurves
from tests.test_input_param_parser import TestInputParamParser


def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestProscessData("test_remove_value_error"))
    suite.addTest(TestProscessData("test_process_data"))

    suite.addTest(TestRunRequest("test_run_request"))

    suite.addTest(TestInputParamParser("test_from_and_to_date"))
    suite.addTest(TestInputParamParser("test_from_date_only"))
    suite.addTest(TestInputParamParser("test_to_date_only"))
    suite.addTest(TestInputParamParser("test_no_date_provided"))

    suite.addTest(TestGetListOfWantedCurves("test_all_parameter"))
    suite.addTest(TestGetListOfWantedCurves("test_multiple_parameters"))
    suite.addTest(TestGetListOfWantedCurves("test_single_parameter"))

    return suite


def input_data_type():
    input_param = input(
        "Enter type of data that you want to show:\n"
        "Can be single value(ex: 3 - this mean you want data Biogas) or multiple values(ex: 1,2,3)\n"
        "Mapping of values:\n"
        "Cogeneration plant -> 1\n"
        "VEKS -> 2\n"
        "Biogas -> 3\n"
        "Geothermal -> 4\n"
        "Industrial waste heat -> 5\n"
        "Peak load gas -> 6\n"
        "Local production -> 7\n"
        "Solar heating -> 8\n"
        "Peak load el -> 9\n"
        "Heat pumps -> 10\n"
        "CTR -> 11\n"
        "Peak load wood pellets -> 12\n"
        "Waste energy plant -> 13\n"
        "Total production -> 14\n"
        "Peak load oil -> 15\n"
        "CO2 - Emission -> 16\n"
        "For all data -> all\n"
        "Data type(from the above list) that you want:"
    )

    return input_param


def main():

    try:
        response = run_request()

        print(f"Status code: {response.status_code}")
    except Exception as ex:
        raise Exception(ex)

    data = response.json()

    try:
        df = worker.process_data(data)
    except Exception as ex:
        raise Exception(ex)

    if df.empty:
        print(f"No data found in varmelast.dk for the given period")
        return
    else:
        data_type = input_data_type()

        try:
            create_plot(df, data_type)
        except Exception as ex:
            raise Exception(ex)


if __name__ == "__main__":
    args = input_param_parser()

    print("<<<Input parameters>>>")
    print(f"[OPT] --From date: {config.FROM_DATE}")
    print(f"[OPT] --To date:   {config.TO_DATE}")
    print("<<<Input parameters>>>\n")

    main()
    runner = unittest.TextTestRunner()
    runner.run(suite())
