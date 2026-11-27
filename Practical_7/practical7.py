# Practical 7: Probabilistic classifier (Naive Bayes) for prediction using scikit-learn
# Name: Anshul Kaustubh
# Enrollment No: 92400118122

from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

print("Name: Anshul Kaustubh | Enrollment No: 92400118122")
print("Practical 7 - Naive Bayes Classifier (Play Tennis)")
print("-" * 55)

# Outlook, Temperature, Humidity, Wind -> Play
data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"],
    ["Overcast", "Cool", "Normal", "Strong", "Yes"],
    ["Sunny", "Mild", "High", "Weak", "No"],
    ["Sunny", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "Normal", "Weak", "Yes"],
    ["Sunny", "Mild", "Normal", "Strong", "Yes"],
    ["Overcast", "Mild", "High", "Strong", "Yes"],
    ["Overcast", "Hot", "Normal", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Strong", "No"],
]

X = [row[:4] for row in data]
y = [row[4] for row in data]

enc = OrdinalEncoder()
X_enc = enc.fit_transform(X)

model = CategoricalNB()
model.fit(X_enc, y)

print("Training records:", len(data))
print("Classes:", [str(c) for c in model.classes_])
print("P(Play=No) =", round(y.count("No") / len(y), 3), " P(Play=Yes) =", round(y.count("Yes") / len(y), 3))
print()

tests = [
    ["Sunny", "Cool", "High", "Strong"],
    ["Overcast", "Mild", "Normal", "Weak"],
    ["Rain", "Hot", "High", "Weak"],
]

for t in tests:
    t_enc = enc.transform([t])
    pred = model.predict(t_enc)[0]
    prob = model.predict_proba(t_enc)[0]
    print("Input:", t)
    print("   P(No) =", round(prob[0], 3), " P(Yes) =", round(prob[1], 3), " => Play Tennis:", pred)
