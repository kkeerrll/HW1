import isodate
from googleapiclient.discovery import build
api_key: str = "AIzaSyDzK-EuKi2DdmdlIl9Pl0Xs1HKEVoOk2HI"
youtube = build('youtube', 'v3', developerKey=api_key)

class Video:
    """Класс видео"""
    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        self.title = None
        self.url = None
        self.view_count = None
        self.like_count = None

        try:
            self.url: str = 'https://youtu.be/' + self.video_id
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
            self.video_title: str = video_response['items'][0]['snippet']['title']
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        except Exception as e:
            print("Error:", str(e))


    def __str__(self):
        """Возвращает название"""
        return f"{self.video_title}"


class PLVideo:
    def __init__(self, PLVideo_id: str, playlist_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.PLVideo_id = PLVideo_id
        self.playlist_id = playlist_id
        playlists = youtube.playlists().list(channelId="UC-OVMPlMA3-YCIeg4z5z23A", part='contentDetails,snippet', maxResults=50,).execute()
        for playlist in playlists['items']:


            if playlist['id'] == self.playlist_id:
                playlist_videos = youtube.playlistItems().list(playlistId=self.playlist_id,part='contentDetails', maxResults=50,).execute()
                video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',id=self.PLVideo_id).execute()
                self.PLtitle: str = video_response['items'][0]['snippet']['title']
                self.url: str = 'https://youtu.be/' + self.PLVideo_id
                self.view_count: int = video_response['items'][0]['statistics']['viewCount']
                self.like_count: int = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        """Возвращает название"""
        return f"{self.PLtitle}"
