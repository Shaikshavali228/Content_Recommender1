
import requests

def get_video_data(video_url):
    # Replace with your YouTube Data API Key
    API_KEY = "AIzaSyD8MAHtts2r7caEbpO79L3Q7rK-xE7_GRQ"
    video_id = video_url.split('v=')[-1]
    url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={API_KEY}&part=snippet,contentDetails'
    
    response = requests.get(url)
    data = response.json()

    if 'items' in data and len(data['items']) > 0:
        video_info = data['items'][0]
        return {
            'title': video_info['snippet']['title'],
            'url': video_url,
            'description': video_info['snippet']['description'],
            'transcript': '',  # Add code to fetch transcript if available
        }
    return None
