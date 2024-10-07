# NLPContributions Dataset

The __NLPContributions__ dataset is composed of abstracts from 1,995 research papers selected from the [ACL Anthology](https://aclanthology.org/), each manually annotated with types of contributions and corresponding statements. We ensured a random yet representative selection, including a minimum of five papers from every year spanning 1974 to February 2024. All selected papers are from journals and conferences associated with “ACL Events.”

Furthermore, our dataset contains abstracts from 28,937 research papers from the ACL Anthology, which have been categorized based on the taxonomy outlined in our paper using a fine-tuned SciBERT model.


## Dataset Sample

```json
	{
      "id": "P03-2011",
      "title": "Semantic Classification of {C}hinese Unknown Words",
      "abstract": "This paper describes a classifier that assigns semantic thesaurus categories to unknown Chinese words (words not already in the CiLin thesaurus and the Chinese Electronic Dictionary, but in the Sinica Corpus). The focus of the paper differs in two ways from previous research in this particular area.Prior research in Chinese unknown words mostly focused on proper nouns (Lee 1993, Lee, Lee and Chen 1994, Huang, Hong and Chen 1994, Chen and Chen 2000). This paper does not address proper nouns, focusing rather on common nouns, adjectives, and verbs. My analysis of the Sinica Corpus shows that contrary to expectation, most of unknown words in Chinese are common nouns, adjectives, and verbs rather than proper nouns. Other previous research has focused on features related to unknown word contexts (Caraballo 1999; Roark and Charniak 1998). While context is clearly an important feature, this paper focuses on non-contextual features, which may play a key role for unknown words that occur only once and hence have limited context. The feature I focus on, following Ciaramita (2002), is morphological similarity to words whose semantic category is known. My nearest neighbor approach to lexical acquisition computes the distance between an unknown word and examples from the CiLin thesaurus based upon its morphological structure. The classifier improves on baseline semantic categorization performance for adjectives and verbs, but not for nouns.",
      "url": "https://aclanthology.org/P03-2011",
      "year": "2003",
      "venue": "The Companion Volume to the Proceedings of 41st Annual Meeting of the Association for Computational Linguistics",
      "authors": [
            "Tseng, Huihsin"
      ],
      "annotations": {
            "artifact_task": [],
            "artifact_method": [
                  "This paper describes a classifier that assigns semantic thesaurus categories to unknown Chinese words (words not already in the CiLin thesaurus and the Chinese Electronic Dictionary, but in the Sinica Corpus)."
            ],
            "knowledge_people": [],
            "knowledge_dataset": [
                  "My analysis of the Sinica Corpus shows that contrary to expectation, most of unknown words in Chinese are common nouns, adjectives, and verbs rather than proper nouns."
            ],
            "knowledge_language": [],
            "artifact_dataset": [],
            "knowledge_task": [],
            "knowledge_method": [
                  "While context is clearly an important feature, this paper focuses on non-contextual features, which may play a key role for unknown words that occur only once and hence have limited context.",
                  "The classifier improves on baseline semantic categorization performance for adjectives and verbs, but not for nouns."
            ]
      }
}

```

## Taxonomy Overview

Below, we provide a concise overview of the taxonomy used to categorize the contribution statements. For details, please refer to the paper. 

| Category | Description |
| --- | --- |
| `knowledge-dataset` | Describes new knowledge about datasets, such as their new properties or characteristics. |
| `knowledge-language` | Presents new knowledge about language, such as a new property or characteristic of language. |
| `knowledge-method` | Describes new knowledge or analysis about NLP models or methods (which predominantly draw from Machine Learning). |
| `knowledge-people` | Presents new knowledge about people, humankind, society, or human civilization. |
| `knowledge-task` | Describes new knowledge about NLP tasks. |
| `artifact-dataset` | Introduces a new NLP dataset (i.e., textual resources such as corpora or lexicon). |
| `artifact-method` | Introduces or proposes a new or novel NLP method or model (primarily to solve NLP task(s)). |
| `artifact-task` | Introduces or proposes a new or novel NLP task (i.e., well-defined NLP problem). |
