import pandas as pd

import config


def process_data(data):

    times = data["times"]
    df = pd.DataFrame(columns=["key", "value", "date", "title", "units", "valueError"])

    for time in times:

        for value in time["values"]:
            value.update({"date": time["timestamp"]})

        # time_df contains data only for one hour
        time_df = pd.DataFrame(time["values"])

        df = pd.concat([df, time_df], ignore_index=True)

    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%dT%H:%M:%S%z", utc=True)

    df = remove_value_error(df)

    if df.empty:
        return pd.DataFrame()

    df = df.reset_index(drop=True)
    df["title"] = df["key"]
    df["units"] = df["key"]

    legends = data["legend"]
    df_legends = pd.DataFrame(legends)

    df["title"] = df["title"].replace(
        list(df_legends["key"]), list(df_legends["title"])
    )
    df["units"] = df["units"].replace(
        list(df_legends["key"]), list(df_legends["units"])
    )

    df["title"] = [config.DATA_DICT[data] for data in df["title"]]

    return df


def remove_value_error(df):
    df = df.drop("valueError", axis=1)

    return df
