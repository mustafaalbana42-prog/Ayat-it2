from django.shortcuts import render
import datetime

# =============================================================
# 1. تعريف الكلاس (Class / Object-Oriented Programming)
# =============================================================
class DesignProject:
    def __init__(self, title, style, length, width, base_price_per_meter):
        self.title = title
        self.style = style
        self.length = length
        self.width = width
        self.base_price_per_meter = base_price_per_meter

    # دالة داخل الكلاس لحساب المساحة
    def calculate_area(self):
        return self.length * self.width

    # دالة داخل الكلاس لحساب السعر الإجمالي
    def calculate_total_cost(self):
        return self.calculate_area() * self.base_price_per_meter


def index(request):
    # -------------------------------------------------------------
    # أ) استخدام الكلاس (Creating Object from Class)
    # -------------------------------------------------------------
    project_obj = DesignProject(
        title="  mimar luxury living room  ",
        style="NEO-CLASSIC",
        length=6,
        width=5,
        base_price_per_meter=100.0
    )

    # -------------------------------------------------------------
    # ب) المتغيرات المحلية ودوال التحويل الـ 9 + upper و lower
    # -------------------------------------------------------------
    # 1. upper() & 2. lower()
    style_upper = project_obj.style.upper()
    style_lower = project_obj.style.lower()

    # 3. strip() & 4. title()
    clean_title = project_obj.title.strip().title() # -> "Mimar Luxury Living Room"

    # 5. float() & 6. int() & 7. str()
    area_int = int(project_obj.calculate_area())            # -> 30 (int)
    cost_float = float(project_obj.calculate_total_cost())   # -> 3000.0 (float)
    area_str = str(area_int) + " متر مربع"                  # -> "30 متر مربع" (str)

    # 8. len() & 9. replace()
    title_len = len(clean_title)
    formatted_style = style_upper.replace("NEO-CLASSIC", "نيوكلاسيك فاخر")

    # -------------------------------------------------------------
    # ج) جمل الشرط بكل أنواعها (If Statements)
    # -------------------------------------------------------------
   
    # 1. [if منفردة]: تغيير حالة ولون المتغير بناءً على الوقت الحاضر
    current_hour = datetime.datetime.now().hour
    theme_color = "dark" # اللون الافتراضي
    greeting = "مرحباً بك في منصة مِعمار"

    if current_hour >= 18 or current_hour < 6:
        # إذا كان الوقت بعد 6 مساءً نغير لون الثيم
        theme_color = "night-gold"
        greeting = "مساء الخير والأنوار المعمارية ✨"

    # 2. [if ... else]: فحص ثنائي (هل المساحة تعتبر كبيرة أم صغيرة؟)
    if area_int > 25:
        space_type = "مساحة واسعة (تتطلب توزيع إضاءة متعدد)"
    else:
        space_type = "مساحة مدمجة (تتطلب أثاثاً ذكياً)"

    # 3. [if ... elif ... else]: فحص متعدد (تصنيف فئة السعر)
    if cost_float >= 5000:
        tier_category = "فئة VIP الرخامية"
        discount = 0.20
    elif cost_float >= 2500 and cost_float < 5000:
        tier_category = "فئة التميز النيوكلاسيك"
        discount = 0.10
    else:
        tier_category = "فئة العملي المودرن"
        discount = 0.05

    final_price = cost_float * (1 - discount)

    # -------------------------------------------------------------
    # د) حلقات التكرار (Loops)
    # -------------------------------------------------------------

    # 1. [For Loop]: للمرور على قائمة عناصر محددة المدى
    raw_services = ["تصميم داخلي", "مخطط 3D", "جدول كميات", "إشراف هندسي"]
    processed_services = []
    for service in raw_services:
        processed_services.append("📌 " + service)

    # 2. [While Loop]: للتكرار بناءً على شرط (حساب جدول الأقساط المتاحة)
    installments_plan = []
    remaining_balance = final_price
    monthly_payment = 500.0
    month_counter = 1

    # حلقة أثناء ما المتبقي أكبر من صفر
    while remaining_balance > 0 and month_counter <= 4:
        remaining_balance -= monthly_payment
        if remaining_balance < 0:
            remaining_balance = 0
        installments_plan.append(f"القسط {month_counter}: المتبقي ${remaining_balance:.1f}")
        month_counter += 1

    # -------------------------------------------------------------
    # هـ) إرسال النتائج إلى التمبلت (Context)
    # -------------------------------------------------------------
    context = {
        'project_title': clean_title,
        'style_upper': style_upper,
        'style_lower': style_lower,
        'formatted_style': formatted_style,
        'area': area_str,
        'cost': cost_float,
        'final_price': final_price,
        'title_len': title_len,
       
        # نتائج الشروط والحلقة والكلاس
        'greeting': greeting,
        'theme_color': theme_color,
        'space_type': space_type,
        'tier_category': tier_category,
        'services': processed_services,
        'installments': installments_plan,
    }

    return render(request, 'cline/index.html', context)