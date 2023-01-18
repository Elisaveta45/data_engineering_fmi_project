import logging

import pandas as pd
import matplotlib.pyplot as plt

import config


logger = logging.getLogger(__name__)


def work(data):
    times = data["times"]
    df = pd.DataFrame(columns=['key', 'value', 'date', 'title', 'units', 'valueError'])

    for time in times:
        for value in time["values"]:
            value.update({"date": time["timestamp"]})

        time_df = pd.DataFrame(time["values"])
        df = pd.concat([df, time_df], ignore_index=True)

    df["date"] = pd.to_datetime(
        df["date"], format="%Y-%m-%dT%H:%M:%S%z", utc=True
    )

    df = remove_value_error(df)
    if df.empty:
        logger.info(
            f"No new data found for {config.TS_NAME}")
        return

    if df is None or df.empty is True:
        logger.info(
            f"No new data found for {config.TS_NAME}")
        return

    df = df.reset_index(drop=True)
    df["title"] = df["key"]
    df["units"] = df["key"]

    legends = data["legend"]
    df_legends = pd.DataFrame(legends)

    df["title"] = df["title"].replace(list(df_legends["key"]), list(df_legends["title"]))
    df["units"] = df["units"].replace(list(df_legends["key"]), list(df_legends["units"]))

    g = df.groupby('title').agg(list).reset_index()
    for i, row in g.iterrows():
        plt.plot(row['date'], row['value'], label=row['title'])
        plt.legend()

    plt.gcf().autofmt_xdate()
    plt.show()
    return df


def remove_value_error(df):
    df = df.drop("valueError", axis=1)

    return df
