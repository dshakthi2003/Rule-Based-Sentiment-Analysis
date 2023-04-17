import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")
sia= SentimentIntensityAnalyzer()
text=input("Enter the text:")
sentiment_scores=sia.polarity_scores(text)
print(sentiment_scores)
if(sentiment_scores["compound"]>0):
  print("Positive Text")
elif(sentiment_scores['compound']<0):
  print("Negative Text")
else:
   print("Neutral Text")
