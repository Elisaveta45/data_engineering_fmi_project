import matplotlib.pyplot as plt

import config


def get_list_of_wanted_curves(df, data_type):

    if data_type == "all":
        data_types_list = list(set(df["title"]))
    elif "," in data_type:
        temp_list = [int(data) for data in data_type.split(",")]
        temp_list = list(filter(lambda x: 17 > x > 0, temp_list))
        if temp_list:
            data_types_list = [config.INPUT_DICT[data] for data in temp_list]
        else:
            data_types_list = []
    else:
        if 17 > int(data_type) > 0:
            data_types_list = [config.INPUT_DICT[int(data_type)]]
        else:
            data_types_list = []

    return data_types_list


def create_plot(df, data_type):

    data_types_list = get_list_of_wanted_curves(df, data_type)

    if data_types_list:

        g = df.groupby("title").agg(list).reset_index()

        for i, row in g.iterrows():
            if row["title"] in data_types_list:
                plt.plot(row["date"], row["value"], label=row["title"])
                plt.legend()

        plt.gcf()
        plt.xticks(rotation=45)
        plt.show()

    else:
        raise Exception("Incorrect input parameter for data type.")
