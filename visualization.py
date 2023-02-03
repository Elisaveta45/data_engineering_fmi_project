import matplotlib.pyplot as plt

import config


def get_list_of_wanted_curves(df, data_type):

    if data_type == "all":
        data_types_list = list(set(df["title"]))
    elif "," in data_type:
        temp_list = [int(data) for data in data_type.split(",")]
        data_types_list = [config.INPUT_DICT[data] for data in temp_list]
    else:
        data_types_list = [config.INPUT_DICT[int(data_type)]]

    return data_types_list


def create_plot(df, data_type):

    data_types_list = get_list_of_wanted_curves(df, data_type)

    g = df.groupby("title").agg(list).reset_index()

    for i, row in g.iterrows():
        if row["title"] in data_types_list:
            plt.plot(row["date"], row["value"], label=row["title"])
            plt.legend()

    plt.gcf()
    plt.xticks(rotation=45)
    plt.show()
