# Practical 8: Mini AI application - Spam text classifier with explainability and ethics
# Name: Anshul Kaustubh
# Enrollment No: 92400118122

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

print("Name: Anshul Kaustubh | Enrollment No: 92400118122")
print("Practical 8 - Spam / Ham Text Classifier")
print("-" * 55)

messages = [
    ("Congratulations you won a free lottery prize, claim now", "spam"),
    ("Win cash now, click this link to claim your reward", "spam"),
    ("Get a free iphone, limited offer, call now", "spam"),
    ("You have been selected for a free gift card", "spam"),
    ("Urgent! your account will be blocked, click link now", "spam"),
    ("Cheap loan offer, apply now and win money", "spam"),
    ("Hey are we meeting for lunch today", "ham"),
    ("Please send me the notes of AI lecture", "ham"),
    ("Can you call me when you reach home", "ham"),
    ("The practical exam is on monday", "ham"),
    ("Happy birthday, have a great day", "ham"),
    ("Let us complete the project report tonight", "ham"),
]

texts = [m[0] for m in messages]
labels = [m[1] for m in messages]

vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

tests = [
    "Claim your free prize now",
    "Are you coming to the AI lab tomorrow",
    "Click the link to win cash",
]
print("Predictions:")
for t in tests:
    p = model.predict(vectorizer.transform([t]))[0]
    prob = model.predict_proba(vectorizer.transform([t]))[0].max()
    print("  ", t.ljust(40), "->", p, "(", round(prob * 100, 1), "% )")

# explainability: words that push the model towards spam
words = vectorizer.get_feature_names_out()
spam_index = list(model.classes_).index("spam")
ham_index = list(model.classes_).index("ham")
score = model.feature_log_prob_[spam_index] - model.feature_log_prob_[ham_index]
top = sorted(zip(score, words), reverse=True)[:6]
print()
print("Explainability - top spam words:", [w for s, w in top])

print()
print("Ethics points:")
print(" 1. Dataset is very small so model can be biased, needs more real data.")
print(" 2. A real mail may be marked spam by mistake (false positive).")
print(" 3. User messages are private data, they must be stored safely.")
print(" 4. Showing the top words helps users understand why a mail is spam.")
