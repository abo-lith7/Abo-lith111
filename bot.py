import tweepy
import schedule
import time
from datetime import datetime
import os

API_KEY = "AkrbkxqlFcFU0AaDQnzuOEXQk"
API_SECRET = "ZGSeVmILr5uLI82ZpJ3DRHqlVXMbQoAnviQqdmhB5Iae7r0c8Z"
ACCESS_TOKEN = "1856324410338422784-gyCXpcoll8PVmd64VX5NYjoFQc2JM7"
ACCESS_SECRET = "oPzthwCyztrBonL3udyvM0kqWvt6hMRrfJdACh6R7gvwR"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

tweets = [
    "✨ منصة أبو ليث لتفسير الأحلام ✨\nللتواصل عبر الواتس: https://wa.me/966507286134",
    "🔮 هل رأيت رؤيا وتريد تفسيرها؟\nتواصل الآن مع الشيخ أبو ليث على الواتس: https://wa.me/966507286134",
    "🌙 تفسير الرؤى على نهج الكتاب والسنة 🌙\nواتساب: https://wa.me/966507286134",
    "📖 تفسير ابن سيرين بين يديك مع الشيخ أبو ليث\nراسلنا عبر الواتس: https://wa.me/966507286134",
    "💡 خدمة التفسير الشرعي للرؤى والأحلام\nواتساب مباشر: https://wa.me/966507286134",
    "🌟 تواصل الآن مع الشيخ أبو ليث لتفسير أحلامك\nرابط الواتس: https://wa.me/966507286134",
    "🔔 رؤياك قد تحمل لك بشارة أو تنبيه!\nراسل الشيخ على الواتس: https://wa.me/966507286134"
]

def job():
    today = datetime.now().weekday()
    tweet = tweets[today % len(tweets)]
    try:
        api.update_status(tweet)
        print("✅ تم النشر:", tweet)
    except Exception as e:
        print("❌ خطأ:", e)

schedule.every().day.at("16:00").do(job)

print("⏳ البوت يعمل وينتظر الوقت المحدد...")

while True:
    schedule.run_pending()
    time.sleep(60)
