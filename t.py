from gensim.models import Word2Vec


sentences = [
    'fazendo um primeiro teste aqui'.split(),
    'fazendo outro teste'.split(),
    'fazendo mais um teste aqui'.split(),
    'novamente fazendo um teste'.split(),
    'outro teste sendo feito'.split(),
    'mais uma vez fazendo um teste'.split(),
    'mais uma vez um experimento sendo feito'.split(),
    'mais uma vez um experimentação sendo feito'.split()
    ]
model = Word2Vec(sentences, min_count=1,size=300)
model.wv.save_word2vec_format('wv_model.txt', binary=False)