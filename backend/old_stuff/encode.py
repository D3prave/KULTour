from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('original_data.csv', encoding='UTF-16')
    
columns_to_keep = ['eventName (actionDetails 1)', 'visitorType', 'visitCount', 'continent', 'country', 'visitorId']
data = data.loc[:, columns_to_keep]

data['is_user_new'] = data['visitorType'].map({"new": 1, "returning": 0})

data.drop(['visitorType', 'visitorId'], inplace=True, axis=1)

Xs, Ys = data.drop(columns=['eventName (actionDetails 1)']), data['eventName (actionDetails 1)']

X_train, X_test, y_train, y_test = train_test_split(Xs, Ys, shuffle=True, train_size=0.8, random_state=42)

preprocessor = ColumnTransformer(
    transformers=[
        ('onehot', OneHotEncoder(sparse_output=False, handle_unknown='ignore'), ['continent', 'country'])
    ],
    remainder='passthrough'
)

X_train_encoded = preprocessor.fit_transform(X_train)
X_test_encoded = preprocessor.transform(X_test)

X_train_encoded = pd.DataFrame(X_train_encoded, columns=preprocessor.get_feature_names_out())
X_test_encoded = pd.DataFrame(X_test_encoded, columns=preprocessor.get_feature_names_out())

label_encoder = LabelEncoder()

label_encoder.fit(pd.concat([y_train, y_test], axis=0))

y_train_encoded = label_encoder.transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

print("X_train_encoded:")
print(X_train_encoded.head())
print("\nY_train_encoded:", y_train_encoded[:5])