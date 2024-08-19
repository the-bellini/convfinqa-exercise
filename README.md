# Convfinqa LLM MVP

## Overview

This repo is an LLM-based exploratory solution to the Convfinqa dataset. The LLM of choice was GPT-4o.

Run `poetry install` to install dependencies.

Please see notebook.ipynb for a working pipeline of the solution.

## Data Pipeline

#### Document preprocessing

1. Documents are split into pre and post texts and table.

2. A summary is generated per document.

3. The document is split into chunks semantically and entities identified in each chunk. Entities are recognised using GliNER to avoid overusing API calls to ChatGPT.

#### Query preprocessing

Entities are recognised in the user prompt, and the LLM is shown the summary and the chunks with the same type of entity as in the query. It is always shown the full table. 

Filtering "nodes" by entity is a similar approach used in Microsoft's GraphRAG. I also wanted to avoid a vector database as I wanted the higher degree of certainty the returned chunks would be relevant.

User queries go through a series of prompts:

1. The first prompt generates a list of follow-up questions to help with the LLM's train of thought.

2. The next prompt double-checks generated questions for inaccuracies.

3. The final prompt generates a calculation based off the generated questions.

#### Calculations

Generated calculations are passed to the calculation module as LLM's calculation abilities can be weak.

## Metrics

The pipeline was run on 50 documents to get a decent estimation of accuracy. Please see notebook.ipynb for a view of how the metrics were calculated.

Percentage of correct estimates:

 - Exact = 30%

 - Out by a factor of 10 = 34%

Accuracy is clearly lower than we would want, however, with more time factoral issues can be remedied more easily than incorrect calculations.

See other potential accuracy improvements below...

## With more time I would improve on

1. Greater control of false positives being generated as accuracy of data points extracted from financial documents is highly important.

2. More checks on formatting calculations to the correct decimal place etc.

3. Finetuning of prompts and more steps to check outputs. In particular, I would focus on the follow-up questions being generated as often they do not accurately answer the user question.

4. Given the large dataset, a smaller LLM could be finetuned to generate more accurate follow-up questions.

5. More entities to recognise in GliNER / possibly swapped out for API calls to an LLM.

6. General optimisations such as parallising tasks 

7. Move solution from notebook.ipynb to an orchestrator / deploy NER model 