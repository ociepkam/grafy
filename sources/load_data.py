import yaml
from os.path import join
import csv
import ast


def load_config():
    try:
        with open("config.yaml") as yaml_file:
            doc = yaml.load(yaml_file, Loader=yaml.FullLoader)
        return doc
    except:
        raise Exception("Can't load config file")


def load_trials(file_name="items.csv"):
    file_path = join("data", file_name)
    try:
        with open(file_path) as f:
            reader = csv.reader(f, delimiter=';')
            header = None
            data_train = []
            data_exp = []
            for row in reader:
                if not header:
                    header = row
                else:
                    data_row = {k: v for k, v in zip(header, row)}
                    for k in ["NR", "FEED", "TRAIN", "NV", "NE"]:
                        data_row[k] = int(data_row[k])
                    for k in ["VA", "VB", "left", "right"]:
                        data_row[k] = [int(elem) for elem in data_row[k].split(",")]
                    for k in ["EA", "EB"]:
                        data_row[k] = ast.literal_eval(data_row[k])
                    if data_row["TRAIN"] == 1:
                        data_train.append(data_row)
                    else:
                        data_exp.append(data_row)
        return data_train, data_exp
    except:
        raise Exception("Can't load file with items: " + file_name)


def replace_polish(text):
    letters = {"Ĺ»": "Ż", "Ã": "Ó", "Ă“": "Ł", "Ä†": "Ć", "Ä": "Ę", "Ĺš": "Ś", "Ä„": "Ą", "Ĺą": "Ź", "Å": "Ń",
               "ĹĽ": "ż", "Ã³": "ó", "Ĺ‚": "ł", "Ä‡": "ć", "Ä™": "ę", "Ĺ›": "ś", "Ä…": "ą", "Ĺş": "ź", "Ĺ„": "ń"}

    for k, v in letters.items():
        text = text.replace(k, v)
    return text