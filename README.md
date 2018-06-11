## Sentiment Classification using LogisticRegression
Text Sentiment Classification. A classic Machine learning classification example.
- ### Dataset used:
  - [Movie reviews Dataset](http://ai.stanford.edu/~amaas/data/sentiment)
  - Contains 25000 positive and 2500 negative reviews
  - Contains at most 30 reviews per movie
- ### Text Processing step:
  - Removing Stop words, Punctuations, etc..
  - Tokenization (TreebankWordTokenizer)
  - Normalization (WordNetLemmatizer)
  - Feature Extraction (TF-IDF)
- ### Classifier used:
  - Logistic Regression
  - F1-Score: 0.88
 
##### Main program: model_train_test.py
