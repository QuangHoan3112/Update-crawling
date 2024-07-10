import os
import requests
from enum import Enum
from api import logger
from api.comment.comment_object import Comment

def get_comment_data_by_video_id(video_id, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/comments/{}") -> Comment:
    url = base_url.format(video_id)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # status 200 OK
        data = response.json()
        comments = [Comment(comment_data) for comment_data in data['data']['comments']]
        return comments

    except Exception as err:
        logger.info("API request failed with status code: {} response: {}".format(response.status_code, err))
    return None
