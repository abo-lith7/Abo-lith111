import os

# تحقق من وصول GitHub Secrets
secrets_list = ["API_KEY", "API_SECRET", "ACCESS_TOKEN", "ACCESS_TOKEN_SECRET"]

for secret in secrets_list:
    value = os.environ.get(secret)
    if value:
        print(f"✅ {secret} موجود وتعمل")
    else:
        print(f"❌ {secret} غير موجود أو خاطئة")
import os
import random
import tweepy

# قراءة المفاتيح من GitHub Secrets
API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

# طباعة للتأكد (لن تظهر القيم، فقط True/False)
print("API_KEY موجود:", bool(API_KEY))
print("API_SECRET موجود:", bool(API_SECRET))
print("ACCESS_TOKEN موجود:", bool(ACCESS_TOKEN))
print("ACCESS_TOKEN_SECRET موجود:", bool(ACCESS_TOKEN_SECRET))

# مصادقة V2
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# قائمة تغريدات
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


# اختيار تغريدة عشوائية
tweet = random.choice(tweets)

# محاولة النشر
try:
    client.create_tweet(text=tweet)
    print("✅ تم نشر التغريدة:", tweet)
except Exception as e:
    print("❌ خطأ في النشر:", e)
