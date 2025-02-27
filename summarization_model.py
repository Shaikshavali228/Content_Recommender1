import re

def remove_emojis(text):
    """Remove emojis from the text using regex."""
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F700-\U0001F77F"  # alchemical symbols
        u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U0001FA00-\U0001FA6F"  # Chess Symbols
        u"\U00002702-\U000027B0"  # Dingbats
        u"\u2600-\u26FF"          # Miscellaneous Symbols
        u"\u2700-\u27BF"          # Dingbats
        "]+", flags=re.UNICODE)
    
    return emoji_pattern.sub(r'', text)

def remove_links(text):
    """Remove URLs from the text using regex."""
    url_pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 
        re.IGNORECASE)
    return url_pattern.sub('', text)

def summarize_video(video_data):
    """Summarize the video content without emojis and irrelevant links."""
    # Assuming video_data contains a 'transcript' or 'description'
    content = video_data.get('transcript') or video_data.get('description', '')
    
    # Clean content: remove emojis and links
    clean_content = remove_emojis(content)
    clean_content = remove_links(clean_content)

    # Optional: Further refine the content to focus on key subject matter
    # This could involve using NLP techniques to extract key sentences
    # For simplicity, here we just return the first 1500 characters
    summary = clean_content.strip()

    # If the clean content is too long, truncate it
    if len(summary) > 5000:
        summary = summary[:5000] + '...'  # Indicate that the content is truncated
    
    return summary.strip()
