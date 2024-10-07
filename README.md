# The Nature of NLP: Analyzing Contributions in NLP Papers

[![License](https://img.shields.io/github/license/UKPLab/ukp-project-template)](https://opensource.org/licenses/Apache-2.0)
[![Python Versions](https://img.shields.io/badge/Python-3.9-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)

This repository includes all necessary code and data to reproduce the experiments detailed in the paper [The Nature of NLP: Analyzing Contributions in NLP Papers](). We release the code under an __Apache 2.0__ license and the dataset under a __CC-BY-SA-4.0__ license. 

This repository contains the code for fine-tuning pre-trained models to detect and classify contribution statements in NLP research papers and categorize them by their types (for details on these types, please consult our paper). These trained models can be applied to any NLP research paper to identify its contributions.


Contact person: [Aniket Pramanick](mailto:aniket.pramanick@tu-darmstadt.de) 

[UKP Lab](https://www.ukp.tu-darmstadt.de/) | [TU Darmstadt](https://www.tu-darmstadt.de/)

The entire pre-processed __ACL Events__ dataset from __ACLAnthology__ will _soon_ be available on [TUdatalib]().
Additional details about the data are available [here](https://github.com/UKPLab/arxiv-2024-nlp-contributions/blob/main/data/README.md).

Don't hesitate to send us an e-mail or report an issue if something is broken (and it shouldn't be) or if you have further questions.

## Abstract
> Natural Language Processing (NLP) is a dynamic, interdisciplinary field that integrates intellectual traditions from computer science, linguistics, social science, and more. Despite its established presence, the definition of what constitutes NLP research remains debated. In this work, we quantitatively investigate what constitutes NLP by examining research papers. For this purpose, we propose a taxonomy and introduce _NLPContributions_, a dataset of nearly $2k$ research paper abstracts, expertly annotated to identify scientific contributions and classify their types according to this taxonomy. We also propose a novel task to automatically identify these elements, for which we train a strong baseline on our dataset. We present experimental results from this task and apply our model to $\sim29k$ NLP research papers to analyze their contributions, aiding in the understanding of the nature of NLP research. Our findings reveal a rising involvement of machine learning in NLP since the early nineties, alongside a declining focus on adding knowledge about language or people; again, in post-2020, there has been a resurgence of focus on language and people. We hope this work will spark discussions on our community norms and inspire efforts to consciously shape the future.


## Getting Started

Follow the instructions below to create the Python environment for the experiments. 

```
$ conda create -n nlpcontributions pip python=3.9 
$ conda activate nlpcontributions
$ pip install -r requirements.txt
```

## Usage

### Dataset

To use the dataset, download the data from the link above and place it inside the `data` folder. 

### Preprocess

To train the models, you will need to split the data into _train-val-test splits_. Use the following script to preprocess the data. 

```py
python code/finetune_data_preparation.py
```

### Fine-tune and Evaluate

To fine-tune the models and evaluate their performance, use the following script. 

```py
python code/limit_classifier.py --model_name_or_path {local or huggingface model path}.
```

We use the following models: BERT, BiomedBERT, SciBERT, RoBERTa, and Flan-T5. 

### Inference

To run the trained model on _test_ split for inference, use the following script. 

```py
python code/inference_merged_labels.py
```

### Analysis

We have used [Tableau for Students](https://www.tableau.com/academic/students) to analyze the data and create all the plots. However, any other visualization software could be used as well to analyze the data. 


## Cite

Please use the following citation:

```bibtex
@article{pramanick2024nlpcontributions,
  title={The Nature of NLP: Analyzing Contributions in NLP Papers},
  author={Pramanick, Aniket and Hou, Yufang and Mohammad, Saif and Gurevych, Iryna},
  journal={},
  year={2024},
  url={}
}
```

## Disclaimer

> This repository contains experimental software and is published for the sole purpose of giving additional background details on the respective publication. 
