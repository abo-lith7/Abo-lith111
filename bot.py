import os
import tweepy
import random
import time

# مفاتيح الدخول من GitHub Secrets
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# المصادقة باستخدام Tweepy Client v2
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# منشورات الشيخ أبو ليث
posts = [
    "🔮 تبحث عن مفسر أحلام موثوق وذو خبرة؟\nالشيخ أبو ليث يقدم لك تفسير شرعي ودقيق لرؤاك وأحلامك 🌙\n📲 wa.me/+966507286134",
    "🌙 كثير من الناس يسألون عن مفسر أحلام ثقة وموثوق ✅\nالشيخ أبو ليث يفسر رؤاك بوضوح وصدق 🌟\n📲 wa.me/+966507286134",
    "✨ هل رأيت رؤيا وتريد تفسيرها؟\nالشيخ أبو ليث مفسر أحلام بخبرة سنوات طويلة 🔮\n📲 wa.me/+966507286134",
    "🌟 تبحث عن تفسير شرعي لرؤاك؟\nالشيخ أبو ليث مفسر موثوق يقدم لك أجوبة واضحة ✨\n📲 wa.me/+966507286134"
]

# الوسوم الإضافية
hashtags = ["#بهاج", "#النصر_التعاون", "#عبدالعزيز_بن_فهد"]
support_hashtag = "#دعم_امير"

# دالة لإنشاء تغريدة مع هاشتاجات عشوائية
def create_tweet():
    post = random.choice(posts)
    tags_text = " ".join(random.sample(hashtags, k=random.randint(1, len(hashtags))))
    return f"{post}\n{tags_text}"

# التفاعل مع منشورات الدعم قبل النشر
def interact_with_support():
    try:
        results = client.search_recent_tweets(query=support_hashtag, max_results=5)
        if results.data:
            for t in results.data:
                try:
                    client.like(tweet_id=t.id)
                    client.retweet(tweet_id=t.id)
                    print(f"🔹 تم التفاعل مع منشور دعم: {t.id}")
                    time.sleep(random.randint(5, 10))
                except:
                    continue
    except Exception as e:
        print(f"❌ خطأ أثناء التفاعل مع دعم: {e}")

# إعادة تغريد منشورات عشوائية من الوسوم
def retweet_random():
    try:
        tag = random.choice(hashtags)
        results = client.search_recent_tweets(query=tag, max_results=5)
        if results.data:
            chosen = random.choice(results.data)
            client.retweet(tweet_id=chosen.id)
            print(f"🔁 تمت إعادة تغريد: {chosen.id}")
    except Exception as e:
        print(f"❌ خطأ في إعادة التغريد: {e}")

# تنفيذ البوت مرة واحدة لكل تشغيل
interact_with_support()
tweet_text = create_tweet()
try:
    response = client.create_tweet(text=tweet_text)
    print(f"✅ تم نشر تغريدة الشيخ: {response.data['id']}")
except Exception as e:
    print(f"❌ خطأ في النشر: {e}")

for _ in range(random.randint(1,3)):
    retweet_random()
    time.sleep(random.randint(10,20))
