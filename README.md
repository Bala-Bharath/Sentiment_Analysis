Sentiment Classification using LogisticRegression
-------------------------------------------------
A classic machine learning example for text classification.

Dataset used:
	IMDB Movie reviews
	- contains 25000 positive and 2500 negative reviews
	- contains at most 30 reviews per moview

Text Processing step:
	- Removing Stop word, Punctuation, etc..
	- Tokenization (TreebankWordTokenizer)
	- Normalization (WordNetLemmatizer)
	- Feature Extraction (TF-IDF)

Classifier used:
	- Logistic Regression

F1-Score: 0.88
Main program: model_train_test.py
