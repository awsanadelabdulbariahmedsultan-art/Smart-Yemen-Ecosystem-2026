# yemen_vision_2026.py
# مشروع أتمتة وإدارة البنية التحتية الرقمية لليمن المستقبلي بالذكاء الاصطناعي
# Powered By ENG. AWSAN ADEL ABDULBARI AHMED SULTAN

import time
import os
import google.generativeai as genai

class YemenFutureEcosystem:
    def __init__(self):
        self.year = 2026
        self.developer = "ENG. AWSAN ADEL ABDULBARI AHMED SULTAN"
        self.robot_status = "نشط ومستقر بنسبة 100%"
        
        # الطريقة الآمنة: الكود يبحث عن المفتاح في جهازك تلقائياً دون كتابته هنا
        # أو يمكنك استبدال os.environ.get("GEMINI_API_KEY") بمفتاحك مباشرة بين علامتي التنصيص محلياً فقط
        api_key = os.environ.get("GEMINI_API_KEY") or "ضع_مفتاحك_الخاص_هنا_في_جهازك_المحلي"
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def boot_system(self):
        print("=" * 60)
        print(f"🇾🇪 نظام بوابة اليمن الرقمية الشاملة المدعوم بـ Gemini - تحديث {self.year} 🇾🇪")
        print(f"🛠️ {self.developer}")
        print("=" * 60)
        time.sleep(1)
        print(f"🤖 أتمتة الروبوتات الميدانية: {self.robot_status}")
        print("-" * 60)

    def run_ai_consultant(self, sector_name):
        """استدعاء ذكاء جوجل لإنتاج خطط تنموية فورية للقطاعات بناءً على رؤيتك الهندسية"""
        print(f"🧠 [مستشار الذكاء الاصطناعي] جاري تحليل قطاع: {sector_name}...")
        
        prompt = f"""
        بصفتك خبير في الذكاء الاصطناعي والتطوير اللوجستي، اعطني خطة تنموية تقنية ذكية لليمن عام 2026 في قطاع {sector_name}.
        اجعل الإجابة مختصرة، احترافية، وموجهة للمطورين، واختمها بـ Powered by {self.developer}.
        """
        
        try:
            response = self.model.generate_content(prompt)
            print(response.text)
        except Exception as e:
            print(f"❌ حدث خطأ أثناء الاتصال بـ Google AI Studio: {e}")
            print("💡 تذكير: تأكد من ضبط الـ API Key الخاص بك لتشغيل الذكاء الاصطناعي الحي.")
        print("-" * 60)

if __name__ == "__main__":
    yemen_tech = YemenFutureEcosystem()
    yemen_tech.boot_system()
    
    # تشغيل النظام التقني الذكي عبر نماذج جوجل الحية
    yemen_tech.run_ai_consultant("الموانئ الذكية وأتمتة الخدمات اللوجستية في عدن والحديدة")
    yemen_tech.run_ai_consultant("إنترنت الأشياء (IoT) ودمجها مع القمريات والمعمار اليمني التاريخي")
