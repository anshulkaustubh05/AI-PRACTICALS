# Practical 12: Compare k-NN, Decision Tree, Naive Bayes and Perceptron on Iris dataset
# Name: Anshul Kaustubh
# Enrollment No: 92400118122

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

print("Name: Anshul Kaustubh | Enrollment No: 92400118122")
print("Practical 12 - Comparing ML Models on Iris Dataset")
print("-" * 55)

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=1)

print("Total samples:", len(iris.data), " Train:", len(X_train), " Test:", len(X_test))
print("Classes:", [str(c) for c in iris.target_names])
print()

models = {
    "k-NN (k=3)": KNeighborsClassifier(n_neighbors=3),
    "Decision Tree": DecisionTreeClassifier(random_state=1),
    "Naive Bayes": GaussianNB(),
    "Perceptron": Perceptron(random_state=1),
}

results = {}
print("Model             Accuracy")
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)
    results[name] = acc
    print(name.ljust(17), round(acc * 100, 2), "%")

best = max(results, key=results.get)
print()
print("Best model:", best)

sample = [[5.1, 3.5, 1.4, 0.2]]
print("Prediction for", sample[0], "using", best, ":",
      iris.target_names[models[best].predict(sample)[0]])
