import tweepy
import os
from datetime import datetime

# جلب مفاتيح تويتر من GitHub Secrets
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']
# قائمة التغريدات اليومية
tweets = [
    "✨ منصة أبو ليث لتفسير الأحلام ✨\nللتواصل عبر الواتس: https://wa.me/966507286134",
    "🔮 هل رأيت رؤيا وتريد تفسيرها؟\nتواصل الآن مع الشيخ أبو ليث على الواتس: https://wa.me/966507286134",
    "🌙 تفسير الرؤى على نهج الكتاب والسنة 🌙\nواتساب: https://wa.me/966507286134",
    "📖 تفسير ابن سيرين بين يديك مع الشيخ أبو ليث\nراسلنا عبر الواتس: https://wa.me/966507286134",
    "💡 خدمة التفسير الشرعي للرؤى والأحلام\nواتساب مباشر: https://wa.me/966507286134",
    "🌟 تواصل الآن مع الشيخ أبو ليث لتفسير أحلامك\nرابط الواتس: https://wa.me/966507286134",
    "🔔 رؤياك قد تحمل لك بشارة أو تنبيه!\nراسل الشيخ على الواتس: https://wa.me/966507286134"
]

def main():
    # الاتصال بتويتر باستخدام v1.1 API للنشر
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    
    # اختيار التغريدة بناءً على يوم الأسبوع
    today = datetime.now().weekday()
    tweet = tweets[today % len(tweets)]
    
    try:
        api.update_status(tweet)
        print(f"✅ تم النشر بنجاح: {tweet}")
    except Exception as e:
        print(f"❌ خطأ في النشر: {e}")

if __name__ == "__main__":
    main()
    schedule.every().day.at("16:00").do(job)

print("⏳ البوت يعمل وينتظر الوقت المحدد...")

while True:
    schedule.run_pending()
    time.sleep(60)
