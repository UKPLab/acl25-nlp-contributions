# The Nature of NLP: Analyzing Contributions in NLP Papers

[![Arxiv](https://img.shields.io/badge/Arxiv-YYMM.NNNNN-red?style=flat&logo=arxiv&logoColor=white)](https://put-here-your-paper.com)
[![License](https://img.shields.io/github/license/UKPLab/ukp-project-template)](https://opensource.org/licenses/Apache-2.0)
[![Python Versions](https://img.shields.io/badge/Python-3.9-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)

This repository includes all necessary code and data to reproduce the experiments detailed in the paper [The Nature of NLP: Analyzing Contributions in NLP Papers](). We release the code under an __Apache 2.0__ license and the dataset under a __CC-BY-SA-4.0__ license. 

Contact person: [Aniket Pramanick](mailto:aniket.pramanick@tu-darmstadt.de) 

[UKP Lab](https://www.ukp.tu-darmstadt.de/) | [TU Darmstadt](https://www.tu-darmstadt.de/)

The entire pre-processed __ACL Events__ dataset from __ACLAnthology__ will _soon_ be available on [TUdatalib]().

Don't hesitate to send us an e-mail or report an issue if something is broken (and it shouldn't be) or if you have further questions.

## Abstract
> Natural Language Processing (NLP) is a dynamic, interdisciplinary field that integrates intellectual traditions from computer science, linguistics, social science, and more. Despite its established presence, the definition of what constitutes NLP research remains debated. In this work, we quantitatively investigate what constitutes NLP by examining research papers. For this purpose, we propose a taxonomy and introduce _NLPContributions_, a dataset of nearly $2k$ research paper abstracts, expertly annotated to identify scientific contributions and classify their types according to this taxonomy. We also propose a novel task to automatically identify these elements, for which we train a strong baseline on our dataset. We present experimental results from this task and apply our model to $\sim29k$ NLP research papers to analyze their contributions, aiding in the understanding of the nature of NLP research. Our findings reveal a rising involvement of machine learning in NLP since the early nineties, alongside a declining focus on adding knowledge about language or people; again, in post-2020, there has been a resurgence of focus on language and people. We hope this work will spark discussions on our community norms and inspire efforts to consciously shape the future.


## Getting Started

> **DO NOT CLONE OR FORK**

If you want to set up this template:

1. Request a repository on UKP Lab's GitHub by following the standard procedure on the wiki. It will install the template directly. Alternatively, set it up in your personal GitHub account by clicking **[Use this template](https://github.com/rochacbruno/python-project-template/generate)**.
2. Wait until the first run of CI finishes. Github Actions will commit to your new repo with a "✅ Ready to clone and code" message.
3. Delete optional files: 
    - If you don't need automatic documentation generation, you can delete folder `docs`, file `.github\workflows\docs.yml` and `mkdocs.yml`
    - If you don't want automatic testing, you can delete folder `tests` and file `.github\workflows\tests.yml`
4. Prepare a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
pip install .
pip install -r requirements-dev.txt # Only needed for development
```
5. Adapt anything else (for example this file) to your project. 

6. Read the file [ABOUT_THIS_TEMPLATE.md](ABOUT_THIS_TEMPLATE.md)  for more information about development.

## Usage

### Using the classes

To import classes/methods of `arxiv_2024_nlp_contributions` from inside the package itself you can use relative imports: 

```py
from .base import BaseClass # Notice how I omit the package name

BaseClass().something()
```

To import classes/methods from outside the package (e.g. when you want to use the package in some other project) you can instead refer to the package name:

```py
from arxiv_2024_nlp_contributions import BaseClass # Notice how I omit the file name
from arxiv_2024_nlp_contributions.subpackage import SubPackageClass # Here it's necessary because it's a subpackage

BaseClass().something()
SubPackageClass().something()
```

### Using scripts

This is how you can use `arxiv_2024_nlp_contributions` from command line:

```bash
$ python -m arxiv_2024_nlp_contributions
```

### Expected results

After running the experiments, you should expect the following results:

(Feel free to describe your expected results here...)

### Parameter description

* `x, --xxxx`: This parameter does something nice

* ...

* `z, --zzzz`: This parameter does something even nicer

## Development

Read the FAQs in [ABOUT_THIS_TEMPLATE.md](ABOUT_THIS_TEMPLATE.md) to learn more about how this template works and where you should put your classes & methods. Make sure you've correctly installed `requirements-dev.txt` dependencies

## Cite

Please use the following citation:

```
@InProceedings{smith:20xx:CONFERENCE_TITLE,
  author    = {Smith, John},
  title     = {My Paper Title},
  booktitle = {Proceedings of the 20XX Conference on XXXX},
  month     = mmm,
  year      = {20xx},
  address   = {Gotham City, USA},
  publisher = {Association for XXX},
  pages     = {XXXX--XXXX},
  url       = {http://xxxx.xxx}
}
```

## Disclaimer

> This repository contains experimental software and is published for the sole purpose of giving additional background details on the respective publication. 
