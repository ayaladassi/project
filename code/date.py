import gensim

model = gensim.models.KeyedVectors.load_word2vec_format(
    r'C:\Users\1\Documents\project\project\GoogleNews-vectors-negative300.bin.gz', binary=True, limit=200000
)
print(model['king'])

result = model.most_similar(positive=['king','woman'], negative=[ 'man'], topn=1)
print(result)

