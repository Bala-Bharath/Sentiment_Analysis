from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

import text_processing as tp

# training data
x_train = tp.get_train_tfidf_data()
y_train = tp.get_train_classes()

# training the model
logmodel = LogisticRegression()
logmodel.fit(x_train,y_train)

# testing data
x_test = tp.get_test_tfidf_data()
y_test = tp.get_test_classes()

# prediction
y_pred = logmodel.predict(x_test)
print(classification_report(y_pred, y_test))
