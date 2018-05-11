from os import listdir
from os.path import isfile, join
from pandas import DataFrame

basedir = 'C:/Users/BA388496/Documents/Learning/Technologies/Datasets/aclImdb'

# getting all file under the given path
def get_files(path):
    files = [(path + f) for f in listdir(path) if isfile(join(path, f))]
    return files

# getting train data
def get_train_data():
    train_neg = basedir + '/train/neg/'
    train_pos = basedir + '/train/pos/'
    
    train_data = []
    for file in get_files(train_neg):
        f = open(file,encoding='utf8')
        train_data.append([f.readlines()[0],0])
        
    for file in get_files(train_pos):
        f = open(file,encoding='utf8')
        train_data.append([f.readlines()[0],1])
        
    return DataFrame(train_data, columns=['review','class'])
    
# getting test data
def get_test_data():
    test_neg = basedir + '/test/neg/'
    test_pos = basedir + '/test/pos/'
    
    test_data = []
    for file in get_files(test_neg):
        f = open(file,encoding='utf8')
        test_data.append([f.readlines()[0],0])
        
    for file in get_files(test_pos):
        f = open(file,encoding='utf8')
        test_data.append([f.readlines()[0],1])
        
    return DataFrame(test_data, columns=['review','class']) 



    
