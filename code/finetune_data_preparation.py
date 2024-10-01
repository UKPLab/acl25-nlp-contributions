import json
import os
import pathlib
from pprint import pprint
import random
import tqdm

import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
import numpy as np
import nltk

# font = {"size": 30}
# plt.rc("font", **font)

from sklearn.model_selection import train_test_split

RANDOM_SEED = 123

random.seed(RANDOM_SEED)

def create_splits():
    src_path = "data/contrib_data/"
    src_path = pathlib.Path(src_path)

    dest_path = "data/finetune_data/"
    dest_path = pathlib.Path(dest_path)

    label_list = []

    for dir_path in src_path.iterdir():
        dir_name = dir_path.name

        if "acl" in dir_name:
            _, typ, cat = dir_name.split("_")
        
            label = f"{typ}_{cat}"
            label_list.append(label)

            pos_samples = []
            neg_samples = []

            for conf in dir_path.iterdir():
                for yr in conf.iterdir():
                    for paper in yr.iterdir():
                        if str(paper.name).endswith(".json"):
                            with open(paper, 'r') as f_in:
                                paper_data = json.load(f_in)
                                annotations = paper_data["llm_annotations"]

                                for row in annotations:
                                    if row["label"].lower()=="yes":
                                        pos_samples.append(row["text"])
                                    elif row["label"].lower()=="no":
                                        neg_samples.append(row["text"])


            try:
                sub_neg_samples = random.sample(neg_samples, len(pos_samples)*2)
            
            except:
                sub_neg_samples = list(neg_samples)

            
            pos_data = [[txt, "pos"] for txt in pos_samples]
            neg_data = [[txt, "neg"] for txt in sub_neg_samples]

            combined_data = list(pos_data) + list(neg_data)
            random.shuffle(combined_data)

            train_samples, rest_samples = train_test_split(combined_data, test_size=0.3, random_state=RANDOM_SEED)
            val_samples, test_samples = train_test_split(rest_samples, test_size=0.5, random_state=RANDOM_SEED)

            train_df = pd.DataFrame(train_samples, columns=["text", "label"])
            val_df = pd.DataFrame(val_samples, columns=["text", "label"])
            test_df = pd.DataFrame(test_samples, columns=["text", "label"])

            # dest_folder = f"{dest_path}/{dir_name}"
            dest_folder = f"{dest_path}/{typ}_{cat}"
            dest_folder = pathlib.Path(dest_folder)

            if not dest_folder.exists():
                dest_folder.mkdir(parents=True, exist_ok=True)
            
            train_df.to_csv(f"{dest_folder}/train.csv", index=False)
            val_df.to_csv(f"{dest_folder}/val.csv", index=False)
            test_df.to_csv(f"{dest_folder}/test.csv", index=False)
        
        else:
            print("Error: unknown directory name")
            exit(1)


if __name__ == "__main__":
    create_splits()
