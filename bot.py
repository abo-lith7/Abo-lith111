import tweepy
import os
import random
import time

# مفاتيح الدخول من بيئة GitHub Secrets
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# تسجيل الدخول
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# منشورات الشيخ أبو ليث
posts = [
    "📌 بسبب كثرة طلباتكم والرسائل اللي تجيني يوميًا 🌙 عن أشخاص يبحثون عن مفسر أحلام شرعي وثقة.\n\nحبيت أشارككم برقم الشيخ المفسر اللي يعتمد عليه كثير من الناس 🌿.\n\n📲 للتواصل: wa.me/966507286134\n\n#مفسر_أحلام",
    "🌙 كثير من الناس تسأل عن مفسر أحلام يكون ثقة ويفسر بالرؤية الشرعية.\n\nالشيخ أبو ليث من أهل الخبرة ويفسر لكم بدقة ووضوح ✨.\n\n📲 للتواصل: wa.me/966507286134\n\n#مفسر_أحلام",
    "🔮 إذا عندك رؤيا محيّرة وتبحث عن تفسير شرعي واضح 🌿.\n\nالشيخ أبو ليث موجود لخدمتكم ويفسر بالرؤية الصحيحة.\n\n📲 تواصل: wa.me/966507286134\n\n#مفسر_أحلام",
    "🌟 الكثير يرسلون لي يسألون عن مفسر رؤى يكون صادق وموثوق.\n\nأبشركم أن الشيخ أبو ليث هو الخيار المناسب 🌙.\n\n📲 للتواصل المباشر: wa.me/966507286134\n\n#مفسر_أحلام",
]

# الوسوم الإضافية
hashtags = ["#بهاج", "#النصر_التعاون", "#عبدالعزيز_بن_فهد"]

# هاشتاج الدعم
support_hashtag = "#دعم_امير"

def create_tweet():
    post = random.choice(posts)
    num_tags = random.randint(1, len(hashtags))
    chosen_tags = random.sample(hashtags, num_tags)
    tags_text = " ".join(chosen_tags)
    tweet = f"{post}\n\n{tags_text}"
    return tweet

def interact_with_support():
    try:
        tweets = api.search_tweets(q=support_hashtag, count=5, result_type="recent", lang="ar")
        for t in tweets:
            try:
                api.create_favorite(t.id)  # إعجاب
                api.retweet(t.id)           # إعادة تغريد
                print(f"🔹 تم التفاعل مع منشور دعم: {t.text[:50]}...")
                # تأخير عشوائي بين التفاعلات (5–15 ثانية)
                time.sleep(random.randint(5, 15))
            except:
                continue
    except Exception as e:
        print(f"❌ خطأ أثناء التفاعل مع دعم: {e}")

def retweet_random():
    try:
        tag = random.choice(hashtags)
        tweets = api.search_tweets(q=tag, count=5, result_type="recent", lang="ar")
        if tweets:
            chosen = random.choice(tweets)
            api.retweet(chosen.id)
            print(f"🔁 تمت إعادة تغريد: {chosen.text[:50]}...")
        else:
            print("⚠️ لا توجد تغريدات لإعادة تغريدها الآن")
    except Exception as e:
        print(f"❌ خطأ في إعادة التغريد: {e}")

def main():
    while True:
        # 1️⃣ التفاعل مع منشورات الدعم قبل النشر
        interact_with_support()
        
        # 2️⃣ نشر تغريدة الشيخ
        tweet = create_tweet()
        try:
            api.update_status(tweet)
            print(f"✅ تم نشر تغريدة الشيخ: {tweet}")
        except Exception as e:
            print(f"❌ خطأ في النشر: {e}")

        # 3️⃣ إعادة تغريد منشورات أخرى عشوائيًا
        for _ in range(random.randint(1, 3)):
            retweet_random()
            time.sleep(random.randint(20, 40))  # تأخير عشوائي بين كل إعادة تغريد

        # 4️⃣ انتظار 3 ساعات قبل الدورة التالية
        time.sleep(3 * 60 * 60)

if __name__ == "__main__":
    main()
