from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

def load_data(max_words=10000,max_len=150):
  (x_train,y_train),(x_test,y_test)=imdb.load_data(num_words=max_words)
  x_train = pad_sequences(x_train,maxlen=max_len)
  x_test =  pad_sequences(x_test,maxlen=max_len)
  return x_train,x_test,y_train,y_test
