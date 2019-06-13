<h1>Supersense Sequence Labelling</h1>

<h2>About</h2>

There are a lot of models that specialise in NER (Named Entity Recognition) task, 
generally optimizing their results for the CONLL-2003 shared task on NER. 
If we consider SuperSeq (Supersense Sequence) Labelling as an extension of NER, 
the models which achieve 90\%+ F1 score on mentioned data fail to perform on a comparative scale. 
The project attempts to evaluate the NER SOTA models on the SuperSeq Labelling task, 
and investigate on what features need to be captured in addition, so as to extend NER for the problem.

The Project is done under the guidance of Prof. Oier at UPV-EHU, in May-June 2019.

<h2> Data for Training and Evaluation </h2>

TODO: Edit the data here, with links

<h2> Models Investigated </h2>

1. <b>Perceptron Model</b> - This model is considered the Baseline as well as SOTA for SuperSeq Labelling Task.
As mentioned in the paper [1], the authors used a set of hand-refined features to create the perceptron model tagger for the data.
On running the aforementioned tagger, we get an F1 score of 69.46 on the test data.

2. <b>Model 1 (word level bi-LSTM + CRF)</b> - The model as suggested in the paper [2] by Huang and Yu.
The implementation of the model was borrowed from a github repository[<sup>1</sup>](#footnotes), and then tuned upon the data.

3. <b>Model 2 (word level bi-LSTM + character level bi-LSTM + CRF)</b> - The model as suggested in the paper [3] by Lample et al.
The implementation of the model was borrowed from a github repository[<sup>1</sup>](#footnotes), and then tuned upon the data.

4. <b>Model 3 (convNet on characters + word level bi-LSTM + CRF)</b> - The model as suggested in the paper [4] by Ma and Hovy.
The implementation of the model was borrowed from a github repository[<sup>1</sup>](#footnotes), and then tuned upon the data.

<h3>Statistics</h3>

Table 1: Training using train+dev data, tuning and results on test data

| Model Name | Embeddings used | Data Format | F1 Score |
|:-----------|:----------------|:------------|:--------:|
| Perceptron |  -              | IOB | 69.46 |
| Model 1 | glove | IOBES | 67.68 |
| Model 2 | glove | IOBES | 67.48 |
| Model 3 | glove | IOBES | 66.73 |

<h2>Additional Models Evaluation</h2>

TODO: Add links

The following Embeddings were used to tune the models, with the associated hyper-parameters as listed in the next section:

1. ElMO Embeddings
2. Flair Embeddings
3. BERT Embeddings
4. <b>Stack1</b> - ElMO + Flair
5. <b>Stack2</b> - ElMO + BERT
6. <b>Stack3</b> - Flair + BERT
7. <b>Stack4</b> - ElMO + Flair + BERT

For each of the embeddings mentioned above, a model with embedding + character-based embeddings were also tried.

<h3>Hyperparameters Tuned</h3>

Table 2: Hyperparameters tuned per embedding sequences

| Parameter | Search Type | Limits |
|:---------:|:------------:|:------:|
| Hidden Layers | Random Integers | 0 - 400 |
| RNN Layers | Choice | 1, 2 |
| Dropout | Uniform | 0 - 0.5 |
| Learning Rate | Choice | 0.05, 0.10, 0.15, 0.20 |
| Mini Batch Size | Choice | 16, 32 |
| use_CRF | Choice | True, False |

<h3> Statistics </h3>

Table3: Training using train data, tuning on dev data, and results for test data

| Embedding Type | F1 Score | Tuned HyperParameters |
|:--------------:|:---------|:----------------------|
| ElMO | ? | ? |
| Flair | ? | ? |
| BERT | ? | ? |
| Stack1 | ? | ? |
| Stack2 | ? | ? |
| Stack3 | ? | ? |
| Stack4 | ? | ? |

Table4: Training using train data, tuning and results for test data

| Embedding Type | F1 Score | Tuned HyperParameters |
|:--------------:|:---------|:----------------------|
| ElMO | ? | ? |
| Flair | ? | ? |
| BERT  | ? | ? |
| Stack1 | ? | ? |
| Stack2 | ? | ? |
| Stack3 | ? | ? |
| Stack4 | ? | ? |

<h2> References </h2>

[1]: Ciaramita, M., & Altun, Y. (2010). Broad-coverage sense disambiguation and information extraction with a supersense sequence tagger, 594.
https://doi.org/10.3115/1610075.1610158  
[2]: Huang, Z., Xu, W., & Yu, K. (2015). Bidirectional LSTM-CRF Models for Sequence Tagging.
Retrieved from http://arxiv.org/abs/1508.01991  
[3]: Lample, G., Ballesteros, M., Subramanian, S., Kawakami, K., & Dyer, C. (2016). Neural Architectures for Named Entity Recognition.
Retrieved from http://arxiv.org/abs/1603.01360  
[4]: Ma, X., & Hovy, E. (2016). End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF.
Retrieved from http://arxiv.org/abs/1603.01354


<h3>Footnotes</h3>

1. [Github Repository by Guillaume Genthial](https://github.com/guillaumegenthial/tf_ner)
