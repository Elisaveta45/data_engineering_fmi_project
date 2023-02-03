import unittest

import pandas as pd

import config
from visualization import get_list_of_wanted_curves


class TestGetListOfWantedCurves(unittest.TestCase):
    def test_all_parameter(self):
        df = pd.DataFrame()
        df["key"] = [
            "BE-EO-CTR-EFF",
            "BE-VL-AFFALD-EF",
            "BE-VL-BIO-EF",
            "BE-VL-EVO-EF",
            "BE-VL-KRAFTV-EF",
            "BE-VL-SPIDS-GAS-EF",
            "BE-VL-SPIDS-OLIE-EF",
            "BE-VL-TOTAL-FAK",
            "BIOGAS",
            "DAP-VEKS-FORBRUG-EFF",
            "GEOTERM",
            "IND_OVS",
            "LOCAL",
            "PUMP",
            "SOL",
            "TOTAL",
            "BE-EO-CTR-EFF",
            "BE-VL-AFFALD-EF",
            "BE-VL-BIO-EF",
            "BE-VL-EVO-EF",
        ]
        df["value"] = [
            1138.0501505534166,
            230.22643534333332,
            0.0,
            19.734650135083335,
            1425.8605346680833,
            12.312466502083334,
            6.003405849333333,
            4.401887774583333,
            3.0,
            411.19787343366664,
            0.0,
            11.0,
            31.0,
            17.0,
            0.0,
            1694.1374924979166,
            1100.819905599,
            210.735903422,
            0.0,
            1.6189741294166666,
        ]
        df["date"] = [
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-01-31 23:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-02-01 00:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-02-01 00:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-02-01 00:00:00+0000", tz="UTC"),
            pd.Timestamp("2023-02-01 00:00:00+0000", tz="UTC"),
        ]
        df["title"] = [
            "CTR",
            "Waste energy plant",
            "Peak load wood pellets",
            "Peak load el",
            "Cogeneration plant",
            "Peak load gas",
            "Peak load oil",
            "CO2 - Emission",
            "Biogas",
            "VEKS",
            "Geothermal",
            "Industrial waste heat",
            "Local production",
            "Heat pumps",
            "Solar heating",
            "Total production",
            "CTR",
            "Waste energy plant",
            "Peak load wood pellets",
            "Peak load el",
        ]
        df["units"] = [
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "Kg/GJ",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
            "MJ/s",
        ]

        data_type = "all"
        expected = list(set(df["title"]))
        result = get_list_of_wanted_curves(df, data_type)
        self.assertEqual(result, expected)

    def test_multiple_parameters(self):
        df = pd.DataFrame()

        data_type = "1,2,3"
        expected = [config.INPUT_DICT[data] for data in [1, 2, 3]]
        result = get_list_of_wanted_curves(df, data_type)
        self.assertEqual(result, expected)

    def test_single_parameter(self):
        df = pd.DataFrame()
        data_type = "1"
        expected = [config.INPUT_DICT[1]]
        result = get_list_of_wanted_curves(df, data_type)
        self.assertEqual(result, expected)
