# FLUTE Extension: Figurative Language Understanding through Textual Explanations

In this repository we propose some extensions to the work of Tuhin Chakrabarty, A. Saakyan, and Debanjan Ghosh on FLUTE project as part of the course Deep Natural Language Processing.

## Actual work

Starting from the FLUTE project, we decided to propose two extensions:

- Model exploration:
  - t5-small
  - t5-base
  - t5-large
  - t5-large with polynomial learning rate 

- Ablation study:
  Two new dataset used for training the model:
  - Fig-QA: it consists of 10256 examples of human-written creative metaphors that are paired as a Winograd schema
  - MNLI: The Multi-Genre Natural Language Inference Corpus is a crowdsourced collection of sentence pairs with textual entailment annotations. Given a premise sentence and a hypothesis sentence, the task is to predict whether the premise entails the hypothesis (entailment), contradicts the hypothesis (contradiction), or neither (neutral)


## Previous work

Code and Data for EMNLP 2022 paper <a target="FLUTE: Figurative Language Understanding through Textual Explanations" href="https://arxiv.org/pdf/2205.12404.pdf">FLUTE: Figurative Language Understanding through Textual Explanations</a><br>
Email : tuhin.chakr@cs.columbia.edu ( For enquiries)

You can explore our data at https://huggingface.co/datasets/ColumbiaNLP/FLUTE with dataset explorer<br>
Our train, val and test data can be accessed from files FLUTEfinaltrain.json, FLUTEfinalval.json, FLUTEfinaltest.json
The test labels and explanations for the entire test set are intentionally hidden for now. We will release it in time. Please email us for gold label and explanations for test set

                @inproceedings{Chakrabarty2022FLUTEFL,
                                  title={FLUTE: Figurative Language Understanding through Textual Explanations},
                                  author={Tuhin Chakrabarty and A. Saakyan and Debanjan Ghosh and Smaranda Muresan},
                                  year={2022}
                                }

# Authors
- Alexandre Casarin
- Federica Lupo


                                
