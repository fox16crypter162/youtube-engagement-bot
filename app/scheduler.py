
import schedule
import time
from bot import YouTubeEngagementBot

def job():
    bot = YouTubeEngagementBot(youtube_api)
    bot.like_video('12345')
    bot.comment_on_video('12345', 'Great video!')

def run_scheduler():
    schedule.every(1).hour.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
    