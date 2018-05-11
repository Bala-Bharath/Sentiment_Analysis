## Sentiment Classification using LogisticRegression
Text Sentiment Classification.A classic Machine learning classification example.
- <h3>Dataset used:</h3>
 - [Movie reviews Dataset](http://ai.stanford.edu/~amaas/data/sentiment)
 - Contains 25000 positive and 2500 negative reviews
 - Contains at most 30 reviews per moview
- <h3>Text Processing step:</h3>
 - Removing Stop word, Punctuation, etc..
 - Tokenization (TreebankWordTokenizer)
 - Normalization (WordNetLemmatizer)
 - Feature Extraction (TF-IDF)
- <h3>Classifier used:</h3>
 - Logistic Regression
 - F1-Score: 0.88
 
<h5>Main program: model_train_test.py</h5>