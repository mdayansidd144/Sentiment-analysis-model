from torch import dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,conv1D,GlobalMaxPooling1D,Dense
def build_model():
    model =Sequential([
        Embedding(10000,100,input_length=150),
        conv1D(128,5,activation='relu'),
        GlobalMaxPooling1D(),
        Dense(64,activation='relu'),
        dropout(0.5),
        Dense(1,activation='sigmoid')
    ])
    model.compile(
        optimizer='adam',
        loss ='binary_crossentropy',
        metrics=['accuracy']
    ) 
    return model
