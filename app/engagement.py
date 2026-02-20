
from bot import YouTubeEngagementBot

class EngagementTask:
    def __init__(self, bot, video_id, comment=None):
        self.bot = bot
        self.video_id = video_id
        self.comment = comment

    def perform_task(self):
        self.bot.like_video(self.video_id)
        if self.comment:
            self.bot.comment_on_video(self.video_id, self.comment)
    