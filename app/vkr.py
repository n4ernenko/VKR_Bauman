import pandas as pd
import numpy as np
import pickle
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sent = str(input('Введите объект закупки(предмет договора): '))
df = pd.read_pickle('ML_data.pkl')

def clean_text(sent):
    sent = re.sub(r'[-,.;:\/\(\)\[\]\n\t]', ' ', sent) #заменяем на пробелы лишние символы
    sent = re.sub(r'[^а-яёА-ЯЁ\s]', '', sent)
    #sent = re.sub(r'^[А-Я]', sent[:1].lower(), sent) # меняем регистр у первой буквы в строке
    #sent = re.sub(r'[А-Я].*$', '', sent) # удаляем  все, после встреченной заглавной буквы в надеже изюавиться от адресов и
    sent=' '.join([w for w in sent.split() if len(w)>3])
    sent = re.sub(r'\s{2,}', ' ', sent)
    sent = sent.lower()
    return sent

MIN_CHARS = 4
MAX_CHARS = 10
def tokenizer(sent, min_chars=MIN_CHARS, max_chars=MAX_CHARS, lemmatize=True):
    if lemmatize:
        stemmer = nltk.stem.SnowballStemmer("russian")
        tokens = [stemmer.stem(w) for w in word_tokenize(sent)]
    else:
        tokens = [w for w in word_tokenize(sent)]
    token = [w for w in tokens if (len(w) > min_chars and len(w) < max_chars)]
    return token

def extract_best_indices(m, topk, mask=None):
    if len(m.shape) > 1:
        cos_sim = np.mean(m, axis=0)
    else:
        cos_sim = m
    index = np.argsort(cos_sim)[::-1]
    if mask is not None:
        assert mask.shape == m.shape
        mask = mask[index]
    else:
        mask = np.ones(len(cos_sim))
    mask = np.logical_or(cos_sim[index] != 0, mask)
    best_index = index[mask][:topk]
    return best_index

vectorizer = pickle.load(open('tfidf_vec.pickle', 'rb'))
#tfidf_mat = pickle.load(open('tfidf_mat.pickle', 'rb'))
tfidf_mat = vectorizer.fit_transform(df['cleaned_subject'].values)
def get_recommendations_tfidf(sent, tfidf_mat):
    clean_sent = clean_text(sent)
    tokens_query = tokenizer(clean_sent)
    embed_query = vectorizer.transform(tokens_query)
    mat = cosine_similarity(embed_query, tfidf_mat)
    best_index = extract_best_indices(mat, topk=3)
    return best_index

best_index = get_recommendations_tfidf(sent, tfidf_mat)

display(df[['OKPD2_code', 'contract_subject']].loc[best_index])