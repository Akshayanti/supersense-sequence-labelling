from flair.data import Corpus
from flair.embeddings import WordEmbeddings, StackedEmbeddings
from flair.embeddings import BertEmbeddings, FlairEmbeddings, ELMoEmbeddings
from flair.embeddings import BytePairEmbeddings, CharacterEmbeddings
from hyperopt import hp
from flair.hyperparameter.param_selection import SearchSpace, Parameter
from flair.hyperparameter.param_selection import SequenceTaggerParamSelector
from flair.hyperparameter.param_selection import OptimizationValue
from flair.datasets import ColumnCorpus
from flair.models import SequenceTagger

# Set up the Corpus
columns = {0: 'text', 1:'ner'}

data_folder = './data/IOBES'

corpus: Corpus = ColumnCorpus(data_folder, columns, train_file="train.txt", dev_file="dev.txt", test_file="test.txt")
tag_type = 'ner'
tag_dictionary = corpus.make_tag_dictionary(tag_type=tag_type)

# define search_space

search_space = SearchSpace()
search_space.add(Parameter.EMBEDDINGS, hp.choice, options=[
    StackedEmbeddings([ BertEmbeddings('bert-large-cased') ]),
    StackedEmbeddings([ BertEmbeddings('bert-large-cased'), CharacterEmbeddings() ])
])
search_space.add(Parameter.HIDDEN_SIZE, hp.randint, upper=400)
search_space.add(Parameter.RNN_LAYERS, hp.choice, options=[1,2])
search_space.add(Parameter.DROPOUT, hp.uniform, low=0.0, high=0.5)
search_space.add(Parameter.LEARNING_RATE, hp.choice, options=[0.05, 0.1, 0.15, 0.2])
search_space.add(Parameter.MINI_BATCH_SIZE, hp.choice, options=[16, 32])
search_space.add(Parameter.USE_CRF, hp.choice, options=[True, False])


# initialise embeddings

param_selector = SequenceTaggerParamSelector(
    corpus,
    tag_type='ner',
    base_path="Optimisation_evals/BERT/dev",
    training_runs=1, max_epochs=15,
    optimization_value=OptimizationValue.DEV_SCORE
)

# start optimisation
param_selector.optimize(search_space, max_evals=20)


# trainer.train('')
