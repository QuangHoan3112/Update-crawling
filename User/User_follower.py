import os
import requests
from enum import Enum
from api import logger
from api.follower.follower_object import Follower

def get_follower_data_by_user_id(user_id, headers, base_url="https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/user/id/{}/followers") -> Follower:
    url = base_url.format(user_id)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # status 200 OK
        data = response.json()
        follower = Follower(data['data']['follower'])
        return follower

    except Exception as err:
        logger.info("API request failed with status code: {} response: {}".format(response.status_code, err))
    return None
