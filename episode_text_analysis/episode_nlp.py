import pandas as pd
import os
import string
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.probability import FreqDist
from wordcloud import WordCloud
import nltk

# Function for tag notation conversion
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

# Function defining Friends-themed color palette
def friends_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    colors = ["#FF4238", "#FFDC00", "#42A2D6", "#9A0006", "#FFF480", "#00009E"]
    return np.random.choice(colors)

# 1) Downloading necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# 2) Collecting stop words for the English language in a set
stop_words = set(stopwords.words('english'))

# 3) Extending stop words list with additional words
additional_stopwords = ['\'s', '\'d', 'say', 'said', 'one', '...', 'n\'t', '\'m', 'oh', '\'re', 'ok', 'yeah', 'm', 'hey', 'y\'know', 'well', 'na', 'gon', 'okay', 'right', 'uh', '....', 'um', 'ow', '\'ve', 'alright', '\'ll', 'ah', 'really', 'ca', 'umm', '..', '``', '"', 'know', 'like', 'get', 'go', 'ok.', 'look', 'hi', 'tell', 'mean', 'come', 'want', 'thing', 'think', '\'\'', 'c\'mon', 'yes', 'god', 'ya', 'would', 'guy', 'uh-', 'see', 'ooh', 'sorry', 'c\'mere', '-', '--', 'u', 'huh', 'woah', 'wan', 'good', 'great', 'bye', 'whoa', 'ree', 'something', 'could', 'still', 'la', 'blah', 'thanks', 'thank', 'san', 'ha', 'uhh', '\'cause', 'i-i', 'ohh', 'ahh', 'ta', 'ew', 'im', 'thats', 'dont', 'cant', 'youre', 'uhm']
stop_words.update(additional_stopwords)

# 4) Loading the CSV file with concatenated episode quotes
df = pd.read_csv('episode_csv/friends_episodes.csv')

# 5) Ensuring the output directory exists
output_dir = 'episode_analysis'
os.makedirs(output_dir, exist_ok=True)

# 6) Loading the mask image
mask_image_path = 'friends_couch.png'
mask_image = np.array(Image.open(mask_image_path))

# 7) Loading the Friends font
font_path = 'font/FRIENDS_.TTF'

# 8) Processing each episode text
# Creating a lemmatizer
lemmatizer = WordNetLemmatizer()
processed_data = []

for index, row in df.iterrows():
    season = row['season']
    episode_number = row['episode_number']
    episode_title = row['episode_title']
    text = row['text']
    
    # Tokenizing the episode text
    tokens = word_tokenize(text)
    
    # Removing punctuation and stop words
    tokens_no_punctuation = [token for token in tokens if token not in string.punctuation]
    
    # POS tagging and lemmatizing
    pos_tagged = pos_tag(tokens_no_punctuation)
    lemmatized_text = [lemmatizer.lemmatize(token, get_wordnet_pos(tag)) for token, tag in pos_tagged]
    tokens_no_stop_words = [token for token in lemmatized_text if token.lower() not in stop_words]
    
    # Creating episode string from tokens
    processed_text = ' '.join(tokens_no_stop_words)
    # Adding row to processed data
    processed_data.append([season, episode_number, episode_title, processed_text])
    
    # Creating a frequency distribution of the words
    fd = FreqDist(tokens_no_stop_words)
    
    # Plotting the 10 most common words
    most_common_words = fd.most_common(10)
    words, counts = zip(*most_common_words)
    
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Season {season} Episode {episode_number}: 10 Most Common Words')
    plt.savefig(os.path.join(output_dir, f'season_{season}_episode_{episode_number}_common_words.png'))
    plt.close()
    
    # Creating the word cloud
    wordcloud = WordCloud(background_color='black', mask=mask_image, contour_color='white', contour_width=7, color_func=friends_color_func, font_path=font_path).generate(' '.join(tokens_no_stop_words))
    wordcloud.to_file(os.path.join(output_dir, f'season_{season}_episode_{episode_number}_wordcloud.png'))

# 9) Saving processed data to a CSV file
processed_df = pd.DataFrame(processed_data, columns=['season', 'episode_number', 'episode_title', 'processed_text'])
processed_df.to_csv('episode_csv/processed_episodes.csv', index=False)

print("Analysis complete. Plots and word clouds saved to the 'episode_analysis' directory. Processed text data saved to 'processed_episodes.csv'.")