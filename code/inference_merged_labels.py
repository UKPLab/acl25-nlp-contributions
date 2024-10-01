# from transformers import pipeline
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import pathlib
import json
import os
import numpy as np
import pandas as pd
from nltk import sent_tokenize
from tqdm import tqdm
from transformers.trainer_callback import TrainerState

os.environ["WANDB_DISABLED"] = "true"

import nltk.data
nltk_tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')

def get_knowledge_merge_labels_inference(model_dir, dest_dir, load_smaller=False):
    print(f"Starting Inference with model_dir: {str(model_dir)} and dest_dir: {str(dest_dir)}!")
    
    model_save_dir = pathlib.Path(model_dir)

    if not load_smaller:
        tokenizer = AutoTokenizer.from_pretrained(model_save_dir)
        model = AutoModelForSequenceClassification.from_pretrained(model_save_dir)
        knowledge_inference_instance = pipeline(task="text-classification", model=model, tokenizer=tokenizer, batch_size=8)
    
    elif load_smaller:
        print("Loading Smaller Model!")
        tokenizer = AutoTokenizer.from_pretrained(model_save_dir)
        model = AutoModelForSequenceClassification.from_pretrained(model_save_dir, device_map="auto", load_in_8bit=True)
        knowledge_inference_instance = pipeline(task="text-classification", model=model, tokenizer=tokenizer, batch_size=8)

    dest_dir = pathlib.Path(dest_dir)

    if not dest_dir.exists():
        dest_dir.mkdir(parents=True, exist_ok=True)

    
    data_dir = "data/cl_papers_united"
    data_dir = pathlib.Path(data_dir)

    conf_list = os.listdir(data_dir)

    for conf in tqdm(conf_list):
        conf_path = pathlib.Path(f"{data_dir}/{conf}")
        year_list = os.listdir(conf_path)

        for year in year_list:
            conf_year_path = pathlib.Path(f"{conf_path}/{year}")
            paper_list = os.listdir(conf_year_path)

            for paper in paper_list:
                paper_path = pathlib.Path(f"{conf_year_path}/{paper}")

                with open(paper_path, "r") as f_in:
                    paper_data = json.load(f_in)
                    paper_abstract = paper_data["abstract"]
                    # tokenized_abstract = sent_tokenize(paper_abstract)
                    tokenized_abstract = nltk_tokenizer.tokenize(paper_abstract)

                    dest_file_path = f"{dest_dir}/{conf}/{year}/{paper}"
                    dest_file_path = pathlib.Path(dest_file_path)

                    if not dest_file_path.parent.exists():
                        dest_file_path.parent.mkdir(parents=True, exist_ok=True)

                    if not dest_file_path.exists():
                        try:
                            abstract_labels = knowledge_inference_instance(tokenized_abstract)
                            paper_data["abstract_labels"] = [{"text":sent_data, "label":label_data["label"]} for sent_data, label_data in zip(tokenized_abstract, abstract_labels)]

                            with open(dest_file_path, "w") as f_out:
                                json.dump(paper_data, f_out, indent=6)
                        except:
                            print(f"Error in processing {paper_path}")
                            continue
                    
                    else:
                        print(f"Skipping {dest_file_path} because it already exists!")
        
        print(f"Knowledge Inference Labels Generation Completed for {conf}!")

    print("Knowledge Inference Labels Generation Completed!")


if __name__ == '__main__':
    model_dir = "model/scibert"
    model_dir = pathlib.Path(model_dir)

    dest_dir = "data/knowledge_inference_merged"
    dest_dir = pathlib.Path(dest_dir)

    get_knowledge_merge_labels_inference(model_dir, dest_dir)
    
