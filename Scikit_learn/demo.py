import pandas as pd
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# data_dist = {
#     'Weight_gram': [140, 130, 150, 170, 155, 160, 145, 165,170,167],
#     'Texture_Score': [7, 8, 7, 2, 3, 2, 8, 3,5,6] # ১-১০ স্কেলে মসৃণতা
# }
# y_dist = ['Apple', 'Apple', 'Apple', 'Avogado', 'Orange', 'Orange', 'Apple', 'Orange','Avogado','Orange']

data_dist = {
    'Weight_gram': [
        140, 130, 145, 135, 142, 148, 138, 141, 146, 132, # Apples
        160, 165, 170, 155, 158, 162, 168, 157, 159, 164, # Oranges
        180, 190, 185, 175, 195, 182, 188, 178, 192, 184  # Avocados
    ],
    'Texture_Score': [
        7, 8, 8, 7, 9, 7, 8, 7, 8, 9, # Apples (High score)
        3, 2, 4, 3, 2, 5, 3, 4, 2, 3, # Oranges (Low score)
        5, 6, 5, 7, 6, 5, 6, 7, 5, 6  # Avocados (Medium score)
    ]
}

y_dist = (['Apple'] * 10) + (['Orange'] * 10) + (['Avogado'] * 10)
df2 = pd.DataFrame(data_dist)

scaler=OrdinalEncoder()
X=scaler.fit_transform(df2[['Weight_gram','Texture_Score']])

encoder=LabelEncoder()
y=encoder.fit_transform(y_dist)

X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.75,random_state=42)

model=KNeighborsClassifier(n_neighbors=1)
model.fit(X_train,y_train)

predicValue=model.predict(X_test)
value=encoder.inverse_transform(predicValue)
print(value)

pf1=pd.DataFrame({'Weight_gram':[180],'Texture_Score':[6]})
x1=scaler.transform(pf1)

pred=model.predict(x1)

print("Pridic fruit:",encoder.inverse_transform(pred)[0])
print("accurecy:",accuracy_score(y_test,predicValue)*100)


