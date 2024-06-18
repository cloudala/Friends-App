import pandas as pd
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist

# Ensure you have the necessary NLTK data files
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

# Collecting stop words for the English language in a set
stop_words = set(stopwords.words('english'))
additional_stopwords = ['\'s', '\'d', 'say', 'said', 'one', '...', 'n\'t', '\'m', 'oh', '\'re', 'ok', 'yeah', 'm', 'hey', 'y\'know', 'well', 'na', 'gon', 'okay', 'right', 'uh', '....', 'um', 'ow', '\'ve', 'alright', '\'ll', 'ah', 'really', 'ca', 'umm', '..', '``', '"', 'know', 'like', 'get', 'go', 'ok.', 'look', 'hi', 'tell', 'mean', 'come', 'want', 'thing', 'think', '\'\'', 'c\'mon', 'yes', 'god', 'ya', 'would', 'guy', 'uh-', 'see', 'ooh', 'sorry', 'c\'mere', '-', '--', 'u', 'huh', 'woah', 'wan', 'good', 'great', 'bye', 'whoa', 'ree', 'something', 'could', 'still', 'la', 'blah', 'thanks', 'thank', 'san', 'ha', 'uhh', '\'cause', 'i-i', 'ohh', 'ahh', 'ta', 'ew', 'im', 'thats', 'dont', 'cant', 'youre', 'uhm']
stop_words.update(additional_stopwords)

# Load the CSV file with concatenated episode quotes
df = pd.read_csv('emotion_analysis_results.csv')

# Processing each episode
lemmatizer = WordNetLemmatizer()
processed_data = []

for index, row in df.iterrows():
    season = row['season']
    episode_number = row['episode_number']
    episode_title = row['episode_title']
    processed_text = row['processed_text']
    anger = row['anger']
    disgust = row['disgust']
    fear = row['fear']
    joy = row['joy']
    neutral = row['neutral']
    sadness = row['sadness']
    surprise = row['surprise']
    
    tokens = processed_text.split()
    
    # Frequency distribution
    fd = FreqDist(tokens)
    
    # Plotting the 10 most common words
    most_common_words = fd.most_common(10)
    tags, counts = zip(*most_common_words)
    tags = list(tags)

    processed_data.append([season, episode_number, episode_title, processed_text, tags, anger, disgust, fear, joy, neutral, sadness, surprise])

# Save processed data to a CSV file
processed_df = pd.DataFrame(processed_data, columns=['season', 'episode_number', 'episode_title', 'processed_text', 'tags', 'anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise'])
processed_df.to_csv('friends_episodes_final.csv', index=False)

print("Analysis complete. Processed text data saved to 'friends_episodes_final.csv'.")