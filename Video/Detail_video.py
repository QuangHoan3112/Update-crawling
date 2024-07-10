import os
import requests
from enum import Enum
from api import logger
from api.video.video_object import Video

def get_video_data_by_video_id(video_id, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/video/{}") -> Video:
    url = base_url.format(video_id)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # status 200 OK
        data = response.json()
        video_data = Video(data)
        return video_data

    except Exception as err:
        logger.info("API request failed with status code: {} response: {}".format(response.status_code, err))
    return None
