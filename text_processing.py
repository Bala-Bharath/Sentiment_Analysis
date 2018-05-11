from nltk.tokenize import TreebankWordTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer

import train_test_data as ttd

# train and test data
train_data = ttd.get_train_data()
test_data = ttd.get_test_data()

tfidf = TfidfVectorizer(min_df=2,max_df=0.7,ngram_range=[1,3])

# text processing steps
def token_normalization(text):
    tokenizer = TreebankWordTokenizer()
    normalizer = WordNetLemmatizer()
    stopwds = stopwords.words('English')
    text = ''.join([c for c in text if c not in punctuation])
    tokens = tokenizer.tokenize(text)
    tokens = [token for token in tokens if token not in stopwds]
    tokens = [normalizer.lemmatize(token) for token in tokens]
    tokens = ' '.join([token for token in tokens if token.isalpha()])
    return tokens

# returns labels of training data
def get_train_classes():
    return train_data['class']

# returns labels of testing data
def get_test_classes():
    return test_data['class']
    
# returns tfidf matrix for training data
def get_train_tfidf_data():
    tokens = train_data['review'].apply(token_normalization)
    tfidf_data = tfidf.fit_transform(tokens)
    return tfidf_data

# returns tfidf matrix for testing data
def get_test_tfidf_data():
    tokens = test_data['review'].apply(token_normalization)
    tfidf_data = tfidf.transform(tokens)
    return tfidf_data
    

    
    

    
    
    
    
    
    
    
    
    
    
    
    