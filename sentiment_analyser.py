positive_words = [
    "good", "great", "excellent", "amazing",
    "happy", "love", "awesome", "wonderful",
    "best", "nice"
]

negative_words = [
    "bad", "worst", "hate", "terrible",
    "sad", "poor", "awful", "boring",
    "disappointed", "horrible"
]


def analyze_sentiment(text):
    text = text.lower()

    words = text.split()

    positive_count = 0
    negative_count = 0

    for word in words:
        if word in positive_words:
            positive_count += 1

        if word in negative_words:
            negative_count += 1

    if positive_count > negative_count:
        return "Positive 😊"

    elif negative_count > positive_count:
        return "Negative 😞"

    else:
        return "Neutral 😐"


print("----- Sentiment Analysis -----")

sentence = input("Enter a sentence: ")

result = analyze_sentiment(sentence)

print("Sentiment:", result)
