# The Nature of NLP: Analyzing Contributions in NLP Papers

[![Arxiv](https://img.shields.io/badge/Arxiv-2409.19505-red?style=flat&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2409.19505)
[![License](https://img.shields.io/github/license/UKPLab/ukp-project-template)](https://opensource.org/licenses/Apache-2.0)
[![Python Versions](https://img.shields.io/badge/Python-3.9-9cf.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Data](https://img.shields.io/badge/TUdatalib-data-blue.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAYFBMVEX////T57m72pG+3Jbp89252Y7J4qrt9eP8/fuEwBiOxDmMwzSdy1eJwimv1HuSxkKQxT2gzV+Cvg6Lwy+hzWCby1Xn8tnN5LDz+eyYyU7R5ral0Gmp0XD6/Pas03a22IlLnOEsAAAAlklEQVR4AdURAxLEMDBo7OzV+v8vz3aHDdZetMaDCSXFDjNKuXjQSaW1sTtij51/ULoQYtoRGcAEs3lWljuiqqraBKjvtMoYDc2RriC2d8qqwwTKQso9Y6Pb4ftTOHAK74j+hRINMZh6iVLAm7AFxhTaahwfC3pspXho5TqEouj0wxAexpc+DH56XBkjrNrhmRBeoHWeLRrpCZsT6Ny/AAAAAElFTkSuQmCC)](https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/4678)


This repository includes all necessary code and data to reproduce the experiments detailed in the paper [The Nature of NLP: Analyzing Contributions in NLP Papers](https://arxiv.org/pdf/2409.19505). We release the code under an __Apache 2.0__ license and the dataset under a __CC-BY-SA-4.0__ license. 

This repository contains the code for fine-tuning pre-trained models to detect and classify contribution statements in NLP research papers and categorize them by their types (for details on these types, please consult our paper). These trained models can be applied to any NLP research paper to identify its contributions.


Contact person: [Aniket Pramanick](mailto:aniketpramanick26@gmail.com) 

[UKP Lab](https://www.ukp.tu-darmstadt.de/) | [TU Darmstadt](https://www.tu-darmstadt.de/)

The annotated __ACL Events__ dataset from __ACLAnthology__ is available on [TUdatalib](https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/4678).
Additional details about the data are available [here](https://github.com/UKPLab/arxiv-2024-nlp-contributions/blob/main/data/README.md).

Don't hesitate to send us an e-mail or report an issue if something is broken (and it shouldn't be) or if you have further questions.

---

🎉 Now you can find the __project page__ for this work [here](https://ukplab.github.io/acl25-nlp-contributions/).

---

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
@inproceedings{pramanick-etal-2025-nlpcontributions,
    title={The Nature of NLP: Analyzing Contributions in NLP Papers},
    author={Pramanick, Aniket and Hou, Yufang and Mohammad, Saif and Gurevych, Iryna},
    booktitle={The 63rd Annual Meeting of the Association for Computational Linguistics},
    year={2025},
    url={https://arxiv.org/abs/2409.19505}    
}
```

## Disclaimer

> This repository contains experimental software and is published for the sole purpose of giving additional background details on the respective publication. 
