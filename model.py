import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

dataset=pd.read_csv('hiring.csv')

dataset['experience'].fillna(0,inplace=True)

dataset['test_score'].fillna(dataset['test_score'].mean(),inplace=True)

X=dataset.iloc[:,:3]

#Converting words to integer values
def convert_to_int(word):
    word_dict={'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
    return word_dict[word]

X['experience']=X['experience'].apply(lambda x: convert_to_int(x))

y=dataset.iloc[:,-1]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(X,y)

pickle.dump(regressor,open('model.pkl','wb'))

model=pickle.load(open('model.pkl','rb'))
print(model.predict([[2,9,6]]))
