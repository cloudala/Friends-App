import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

# Load the processed text data
processed_df = pd.read_csv('data/friends_episodes_final.csv')

# Convert 'tags' column from string to list
processed_df['tags'] = processed_df['tags'].apply(ast.literal_eval)

# Create a TF-IDF Vectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(processed_df['processed_text'])

# Calculate the cosine similarity matrix
cosine_sim_matrix = cosine_similarity(tfidf_matrix)

# Function to get all episodes
def get_episodes():
    episodes = processed_df[['season', 'episode_number', 'episode_title', 'tags', 'anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise']]

     # Convert the episodes to a list of dictionaries
    episodes_list = episodes.to_dict(orient='records')
    
    # Return the details of the episodes
    return episodes_list

# Function to get episode with a given season and episode number
def get_episode(season, episode_number):
    # Extract the details of the specified episode
    episode = processed_df[(processed_df['season'] == season) & (processed_df['episode_number'] == episode_number)]

    if episode.empty:
        return None

    # Convert the episode details to a dictionary
    episode_dict = episode[['season', 'episode_number', 'episode_title', 'tags', 'anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise']].to_dict(orient='records')[0]

    return episode_dict

# Function to get episode recommendations
def get_recommendations(season, episode_number, top_n=5):
    # Find the index of the given episode
    episode_index = processed_df[(processed_df['season'] == season) & (processed_df['episode_number'] == episode_number)].index[0]
    
    # Get the similarity scores for the given episode
    sim_scores = list(enumerate(cosine_sim_matrix[episode_index]))
    
    # Sort the episodes based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices of the top_n most similar episodes
    top_similar_indices = [i[0] for i in sim_scores[1:top_n+1]]

    # Extract the details of the top_n most similar episodes
    recommendations = processed_df.iloc[top_similar_indices][['season', 'episode_number', 'episode_title', 'tags', 'anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise']]

     # Convert the recommendations to a list of dictionaries
    recommendations_list = recommendations.to_dict(orient='records')
    
    # Return the details of the top_n most similar episodes
    return recommendations_list