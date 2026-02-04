from torch import dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding,Conv1D,GlobalMaxPooling1D,Dense,Dropout
def build_model():
    model =Sequential([
        Embedding(10000,output_dim=100,input_length=150),
        Conv1D(128,5,activation='relu'),
        GlobalMaxPooling1D(),
        Dense(64,activation='relu'),
        Dropout(0.5),
        Dense(1,activation='sigmoid')
    ])
    model.compile(
        optimizer='adam',
        loss ='binary_crossentropy',
        metrics=['accuracy']
    ) 
    return model
# this is ai ml project