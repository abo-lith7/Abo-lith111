import os
import random
import tweepy

# جلب المفاتيح من GitHub Secrets
API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

# التحقق من وجود المفاتيح
all_keys_present = True
for key_name, key_value in [("API_KEY", API_KEY), ("API_SECRET", API_SECRET),
                            ("ACCESS_TOKEN", ACCESS_TOKEN), ("ACCESS_TOKEN_SECRET", ACCESS_TOKEN_SECRET)]:
    if key_value:
        print(f"✅ {key_name} موجود")
    else:
        print(f"❌ {key_name} غير موجود")
        all_keys_present = False

if not all_keys_present:
    print("❌ توقف البوت: بعض المفاتيح مفقودة")
    exit(1)

# المصادقة باستخدام Tweepy API v2
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# قائمة المنشورات الحقيقية
tweets = [
    "🔮 مفسر أحلام متخصص! ✨\nالشيخ أبو ليث يفسر أحلامك بدقة وفق الكتاب والسنة 📖\nتواصل عبر الواتساب: https://wa.me/966507286134",
    "🌙 حلمت بشيء غريب؟ استشر مفسر أحلام محترف! 🌟\nتفسير شرعي دقيق لجميع الرؤى والأحلام\nراسل مفسر الأحلام الآن: https://wa.me/966507286134",
    "💫 مفسر أحلام معتمد يقدم لك خدمة مميزة! ⏰\nتفسير احترافي خلال 24 ساعة بأسعار تنافسية 🏆\nتواصل مع مفسر الأحلام: https://wa.me/966507286134",
    "📚 يحتاج إلى مفسر أحلام خبير؟ 👑\nالشيخ أبو ليث مفسر أحلام متخصص بتفسير الرؤى بدقة\n💬 WhatsApp مفسر الأحلام: https://wa.me/966507286134",
    "🌌 لديك حلم محير؟ استشر مفسر أحلام متمرس! 🌈\nتفسير احترافي لجميع أنواع الأحلام والرؤى\nمفسر أحلام على WhatsApp: https://wa.me/966507286134",
    "🎯 أفضل مفسر أحلام في الخليج! 🔍\nتفسير علمي شرعي دقيق لجميع الأحلام\n🚀 تواصل مع مفسر الأحلام: https://wa.me/966507286134",
    "⚡ مفسر أحلام سريع الاستجابة! ⚡\nتفسير فوري للأحلام والرؤى على مدار الساعة\n📲 مفسر أحلام على الواتس: https://wa.me/966507286134",
    "💎 تجربة مميزة مع مفسر أحلام محترف! 💎\nتفسير دقيق وواضح لجميع أحلامك\n🌟 مفسر الأحلام Abu Laith: https://wa.me/966507286134",
    "🌠 ثقة وخصوصية مع مفسر أحلام معتمد! 🔒\nتفسير احترافي مع الحفاظ على سرية المعلومات\n🤝 مفسر أحلام ثقة: https://wa.me/966507286134",
    "🏆 مفسر أحلام بخبرة أكثر من 10 سنوات! 📅\nآلاف التفسيرات الناجحة لعملاء راضين\n⭐ تواصل مع مفسر الأحلام: https://wa.me/966507286134",
    "✨ استشارة مجانية مع مفسر أحلام! 🎁\nاحصل على نظرة أولية مجانية لتفسير حلمك\n📞 مفسر أحلام مجاني: https://wa.me/966507286134",
    "🔥 مفسر أحلام متواجد 24/7! 🌙☀️\nتفسير فوري في أي وقت تناسبك\n⚡ مفسر أحلام سريع: https://wa.me/966507286134"
]

# تحميل سجل المنشورات السابقة
log_file = "log.txt"
if os.path.exists(log_file):
    with open(log_file, "r", encoding="utf-8") as f:
        posted_tweets = [line.strip() for line in f.readlines()]
else:
    posted_tweets = []

# اختيار منشور لم يتم نشره بعد
available_tweets = [t for t in tweets if t not in posted_tweets]

if not available_tweets:
    print("✅ تم نشر جميع المنشورات بالفعل. إعادة التدوير.")
    posted_tweets = []
    available_tweets = tweets.copy()

tweet = random.choice(available_tweets)

# محاولة النشر
try:
    response = client.create_tweet(text=tweet)
    print("✅ تم نشر التغريدة:", tweet)
    print("Tweet ID:", response.data["id"])
    
    # تحديث سجل المنشورات
    posted_tweets.append(tweet)
    with open(log_file, "w", encoding="utf-8") as f:
        for t in posted_tweets:
            f.write(t + "\n")
except Exception as e:
    print("❌ خطأ في النشر:", e)
