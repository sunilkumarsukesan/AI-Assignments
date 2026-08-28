


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

le.fit(["Apple","Mango","Orange","Pineapple"])
encoded_lables=le.transform(["Apple","Mango","Orange","Pineapple"])
print(encoded_lables)

original_lables=le.inverse_transform([0,1,2,3])
print(original_lables)