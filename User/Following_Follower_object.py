class Follower:
    def __init__(self, data: dict) -> None:
        self.id = data.get('id', None)
        self.region = data.get('region', None)
        self.sec_uid = data.get('sec_uid', None)
        self.unique_id = data.get('unique_id', None)
        self.nickname = data.get('nickname', None)
        self.signature = data.get('signature', None)
        self.avatar = data.get('avatar', None) 
        self.verified = data.get('verified', None)
        self.secret = data.get('secret', None)
        self.aweme_count = data.get('aweme_count', -1)
        self.follower_count = data.get('follower_count', -1)
        self.favoriting_count = data.get('favoriting_count', -1)
        self.total_favorited = data.get('total_favorited', -1)
        self.ins_id = data.get('ins_id', None)
        self.youtube_channel_title = data.get('youtube_channel_title', None)
        self.youtube_channel_id = data.get('youtube_channel_id', None)
        self.twitter_name = data.get('twitter_name', None)
        self.twitter_id = data.get('twitter_id', None)

    def __str__(self) -> str:
        output_string = (
            f"ID: {self.id}\n" +
            f"Region: {self.region}\n" +
            f"Sec UID: {self.sec_uid}\n" +
            f"Unique ID: {self.unique_id}\n" +
            f"Nickname: {self.nickname}\n" +
            f"Signature: {self.signature}\n" +
            f"Verified: {self.verified}\n" +
            f"Secret: {self.secret}\n" +
            f"Aweme count: {self.aweme_count}\n" +
            f"Follower count: {self.follower_count}\n" +
            f"Favoriting count: {self.favoriting_count}\n" +
            f"Total favorited: {self.total_favorited}\n" +
            f"Ins ID: {self.ins_id}\n" +
            f"YouTube channel title: {self.youtube_channel_title}\n" +
            f"YouTube channel ID: {self.youtube_channel_id}\n" +
            f"Twitter name: {self.twitter_name}\n" +
            f"Twitter ID: {self.twitter_id}\n" +
            f"Avatar: {self.avatar}\n"
        )
        return output_string


class Following(Follower):
    pass