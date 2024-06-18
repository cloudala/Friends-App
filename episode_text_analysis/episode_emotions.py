import pandas as pd
from transformers import pipeline

# 1) Initializing the emotion classifier
emotion_classifier = pipeline('text-classification', model='j-hartmann/emotion-english-distilroberta-base', framework='pt', return_all_scores=True)

# 2) Loading the processed text data
processed_df = pd.read_csv('episode_csv/processed_episodes.csv')

# 3) Defining emotions which classifier detects
emotions = ['anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise']

# 4) Splitting text into chunks (model accepts text consisting of max 512 words)
def split_text(text, max_length=512):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        word_length = len(word) + 1  # +1 for the space
        if current_length + word_length <= max_length:
            current_chunk.append(word)
            current_length += word_length
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = word_length
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    
    return chunks

# 5) Detecting emotions in chunks
def get_emotions(text):
    chunks = split_text(text)
    all_results = {emotion: 0.0 for emotion in emotions}

    for chunk in chunks:
        results = emotion_classifier(chunk)
        for result in results[0]:
            all_results[result['label']] += result['score']
    
    return all_results

# 6) Processing each episode and storing the results
emotion_data = []

for episode_text in processed_df['processed_text']:
    episode_emotions = get_emotions(episode_text)
    total_score = sum(episode_emotions.values())
    normalized_scores = {label: score / total_score for label, score in episode_emotions.items()}
    emotion_data.append(normalized_scores)

# 7) Creating a DataFrame with the results
emotion_df = pd.DataFrame(emotion_data)

# 8) Combining the original DataFrame with the emotion scores
result_df = pd.concat([processed_df, emotion_df], axis=1)

# 9) Saving the result to a new CSV file
result_df.to_csv('episode_csv/emotion_analysis_results.csv', index=False)

print("Emotion analysis completed and saved to 'emotion_analysis_results.csv'")