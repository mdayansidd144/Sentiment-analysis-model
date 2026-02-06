from googleapiclient.discovery import build
import os
import os
print("DEBUG ▶ YOUTUBE_API_KEY =", os.getenv("YOUTUBE_API_KEY"))
def get_youtube_client():
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        raise RuntimeError("YOUTUBE_API_KEY is not set")

    return build("youtube", "v3", developerKey=api_key)
def fetch_youtube_comments(video_id, limit=50):
    youtube = get_youtube_client()
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=min(limit, 100),
        textFormat="plainText"
    )

    response = request.execute()

    for item in response.get("items", []):
        text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(text)

    return comments

# 