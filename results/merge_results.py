import os
import pandas as pd
import glob


def read(f):
    data = pd.read_csv(f, sep=";")
    data["NAME"] = [f.split("/")[-1]]*len(data)
    return data


def all_to_one_file(files_path, file_name):
    df = pd.concat(map(read, glob.glob(os.path.join(files_path, "*.csv"))))
    df.to_csv(file_name + ".csv")


all_to_one_file('raw_results', 'raw_results')
all_to_one_file('summary_results', 'summary_results')
