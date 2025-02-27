import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob

def delete_file(file_path):
    """Delete a file if it exists."""
    if file_path is not None:
        try:
            os.remove(file_path)
            print(f"Successfully removed {file_path}")
        except OSError as e:
            print(f"Error removing file {file_path}: {e}")
    else:
        print("Cannot remove the file because the path is None.")

def calculate_sentiment_score(text):
    """Calculate sentiment polarity score of the text."""
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity  # Returns a score between -1 (negative) and 1 (positive)
    return sentiment_score

def calculate_similarity_score(transcripts):
    """Calculate the cosine similarity between transcripts using TF-IDF."""
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(transcripts)  # Convert transcripts to TF-IDF matrix
    similarity_matrix = cosine_similarity(tfidf_matrix)  # Calculate cosine similarity between all transcripts
    return similarity_matrix

def select_best_video(videos):
    """Select the best video based on TF-IDF, Sentiment Scores, and Similarity."""
    if not videos:
        return None

    transcripts = [video['transcript'] for video in videos]

    # Calculate similarity scores
    similarity_matrix = calculate_similarity_score(transcripts)

    # Calculate sentiment scores for each video
    for video in videos:
        video['sentiment_score'] = calculate_sentiment_score(video['transcript'])

    # Calculate final score based on similarity and sentiment
    for i, video in enumerate(videos):
        # For simplicity, we take the average similarity with all other videos
        similarity_score = similarity_matrix[i].mean()
        sentiment_score = video['sentiment_score']
        
        # Final score (you can adjust the weights of similarity and sentiment as needed)
        video['final_score'] = (similarity_score * 0.7) + (sentiment_score * 0.3)

    # Select the video with the highest final score
    best_video = max(videos, key=lambda x: x['final_score'])
    return best_video
