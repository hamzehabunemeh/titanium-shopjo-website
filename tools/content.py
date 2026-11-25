"""All website text and business data, in Arabic and English.

Edit this file to change any wording, phone number or price, then run:
    python3 tools/build.py
and commit the regenerated .html files.

Every text value is L(arabic, english).
"""


def L(ar, en):
    return {"ar": ar, "en": en}


# --------------------------------------------------------------------------
# Business details
# --------------------------------------------------------------------------
SITE_URL = "https://titaniumshopjo.netlify.app"  # change when the domain is ready
BRAND = "Titanium Shop"

CONTACT = {
    "phone_display": "0793 888 444",
    "phone_tel": "+962793888444",
    "mgmt_display": "0799 888 444",
    "mgmt_tel": "+962799888444",
    "whatsapp": "962799888444",  # wa.me number, no + or spaces
    "whatsapp_display": "+962 7 9988 8444",
    "email": "titaniumshopjo@gmail.com",
    "address": L("برج الكرادشة، الطابق الأول، عمّان، الأردن",
                 "Al-Karadsheh Tower, 1st Floor, Amman, Jordan"),
    "map_url": "https://www.google.com/maps/search/?api=1&query=Al+Karadsheh+Tower+Amman+Jordan",
    "instagram": "https://www.instagram.com/titaniumshopjo/",
    "instagram_events": "https://www.instagram.com/titanium_event.jo/",
    "facebook": "https://www.facebook.com/TitaniumShopJO",
}

# Form submissions go to this FormSubmit endpoint. After the first submission,
# FormSubmit emails a confirmation link to this address — click it once.
FORM_ACTION = "https://formsubmit.co/titaniumshopjo@gmail.com"

# Price shown on every service page. Replace a service's "price" below with
# real text, e.g. L("يبدأ من 150 دينار يومياً", "From 150 JOD per day").
PRICE_ON_REQUEST = L("عرض سعر خلال 5 دقائق", "A quote within 5 minutes")

# --------------------------------------------------------------------------
# Shared interface text
# --------------------------------------------------------------------------
UI = {
    "home": L("الرئيسية", "Home"),
    "services": L("خدماتنا", "Services"),
    "about": L("من نحن", "About"),
    "contact": L("تواصل معنا", "Contact"),
    "request": L("اطلب خدمتك", "Request a service"),
    "request_this": L("اطلب هذه الخدمة", "Request this service"),
    "whatsapp": L("واتساب", "WhatsApp"),
    "call": L("اتصل بنا", "Call us"),
    "menu": L("القائمة", "Menu"),
    "close": L("إغلاق", "Close"),
    "lang_switch": L("English", "العربية"),
    "lang_switch_label": L("Switch to English", "التبديل إلى العربية"),
    "discover": L("اكتشف المزيد", "Discover more"),
    "all_services": L("جميع الخدمات", "All services"),
    "included": L("ماذا تشمل الخدمة", "What's included"),
    "how": L("كيف تحجز", "How to book"),
    "details": L("التفاصيل", "Key details"),
    "gallery": L("من الداخل", "A closer look"),
    "faq": L("أسئلة شائعة", "Frequently asked questions"),
    "price": L("السعر", "Price"),
    "payment": L("الدفع", "Payment"),
    "payment_value": L("نقداً، تحويل بنكي، أو بطاقة", "Cash, bank transfer or card"),
    "skip": L("تخطَّ إلى المحتوى", "Skip to content"),
    "rights": L("جميع الحقوق محفوظة", "All rights reserved"),
    "privacy": L("سياسة الخصوصية", "Privacy policy"),
    "follow": L("تابعنا", "Follow us"),
    "reach": L("للتواصل", "Get in touch"),
    "cs_247": L("خدمة العملاء على مدار الساعة", "Customer service 24/7"),
    "footer_line": L("فخامة بلا حد. كل ما تحتاجه في الأردن، في مكان واحد.",
                     "Unlimited luxury. Everything you need in Jordan, in one place."),
    "cta_title": L("اطلب ما تشاء، متى تشاء", "Whatever you need, whenever you need it"),
    "cta_text": L("فريقنا متاح على مدار الساعة، ونرد على طلبك خلال 5 دقائق.",
                  "Our team is available around the clock and replies within 5 minutes."),
    "back_home": L("العودة إلى الرئيسية", "Back to home"),
}

STEPS_DEFAULT = [
    (L("أرسل طلبك", "Send your request"),
     L("عبر الواتساب أو الهاتف أو نموذج الطلب في الموقع.",
       "By WhatsApp, phone or the request form on this site.")),
    (L("عرض خلال 5 دقائق", "A reply in 5 minutes"),
     L("نرسل لك التفاصيل وعرض السعر بسرعة ووضوح.",
       "We send you the details and a clear quote.")),
    (L("تأكيد الحجز", "Confirm"),
     L("نثبّت الحجز بعد موافقتك، ونرتّب كل التفاصيل.",
       "Once you approve, we lock in the booking and arrange every detail.")),
    (L("نتولى الباقي", "We take it from there"),
     L("نبقى على تواصل معك حتى نهاية الخدمة.",
       "We stay in touch with you until the service is complete.")),
]

# --------------------------------------------------------------------------
# Car fleet  (image name = file in assets/img without size suffix)
# --------------------------------------------------------------------------
CAR_CATEGORIES = {
    "suv": L("دفع رباعي", "SUV"),
    "sedan": L("سيدان", "Sedan"),
    "van": L("فان VIP", "VIP Van"),
}
FLEET = [
    ("escalade", "Cadillac Escalade", "suv"),
    ("range-rover-vogue", "Range Rover Vogue", "suv"),
    ("range-rover-sport", "Range Rover Sport", "suv"),
    ("defender", "Land Rover Defender", "suv"),
    ("yukon", "GMC Yukon", "suv"),
    ("tahoe", "Chevrolet Tahoe", "suv"),
    ("land-cruiser", "Toyota Land Cruiser", "suv"),
    ("s-class", "Mercedes-Benz S-Class", "sedan"),
    ("bmw-750", "BMW 750", "sedan"),
    ("e-class", "Mercedes-Benz E-Class", "sedan"),
    ("bmw-530", "BMW 530", "sedan"),
    ("c-class", "Mercedes-Benz C-Class", "sedan"),
    ("v-class-maybach", "Mercedes-Benz V-Class Maybach", "van"),
]

JET_CLASSES = [
    ("6", L("رحلات العمل السريعة والمجموعات الصغيرة", "Quick business trips and small groups")),
    ("8", L("رجال الأعمال والعائلات", "Executives and families")),
    ("12", L("الوفود وفرق العمل", "Delegations and teams")),
    ("16", L("الوفود الكبيرة والمناسبات", "Large delegations and occasions")),
]

CELEBRITIES = [
    ("mike-tyson", L("مايك تايسون", "Mike Tyson")),
    ("tamer-hosny", L("تامر حسني", "Tamer Hosny")),
    ("ronaldinho", L("رونالدينيو", "Ronaldinho")),
    ("najwa-karam", L("نجوى كرم", "Najwa Karam")),
    ("ahmed-saad", L("أحمد سعد", "Ahmed Saad")),
    ("fadel-chaker", L("فضل شاكر", "Fadel Chaker")),
]

WEDDING_ARTISTS = [L("ميريام فارس", "Myriam Fares"), L("أحمد سعد", "Ahmed Saad"), L("نانسي عجرم", "Nancy Ajram")]

# --------------------------------------------------------------------------
# Services — one page each
# --------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "cars",
        "img": "s-class",
        "card_img": "escalade",
        "title": L("السيارات الفاخرة", "Luxury Cars"),
        "kicker": L("أسطول 2024–2026", "2024–2026 fleet"),
        "short": L("أسطول حديث من أفخم السيارات، مع سائق خاص أو بقيادتك.",
                   "A modern fleet of premium cars, with a private chauffeur or self-drive."),
        "lead": L("13 سيارة فاخرة من موديلات 2024–2026، جاهزة لرجال الأعمال وضيوف الأردن. اختر سيارتك، وقرّر بنفسك: تقودها، أو نرسل معها سائقاً خاصاً.",
                  "Thirteen luxury cars, all 2024–2026 models, ready for executives and guests of Jordan. Choose your car, then decide: drive it yourself, or have a private chauffeur."),
        "meta": L("استئجار سيارات فاخرة في عمّان مع سائق أو بدون: إسكاليد، رينج روفر، مرسيدس S-Class، مايباخ وأكثر. موديلات 2024–2026.",
                  "Luxury car rental in Amman with or without a chauffeur: Escalade, Range Rover, Mercedes S-Class, Maybach and more. 2024–2026 models."),
        "includes": [
            L("سيارات دفع رباعي وسيدان وفان VIP", "SUVs, sedans and a VIP van"),
            L("مع سائق خاص أو بقيادتك، الخيار لك", "Private chauffeur or self-drive, your choice"),
            L("موديلات حديثة 2024–2026", "Recent 2024–2026 models"),
            L("يمكن دمجها مع الاستقبال من المطار والحراسة", "Can be combined with airport reception and protection"),
        ],
        "facts": [
            (L("أقل مدة للحجز", "Minimum rental"), L("يومان", "Two days")),
            (L("السائق", "Chauffeur"), L("اختياري", "Optional")),
            (L("الموديلات", "Models"), L("2024–2026", "2024–2026")),
        ],
        "faqs": [
            (L("هل يمكنني استئجار السيارة بدون سائق؟", "Can I rent a car without a chauffeur?"),
             L("نعم. الخيار لك: سائق خاص، أو قيادة السيارة بنفسك.", "Yes. It's your choice: a private chauffeur, or drive it yourself.")),
            (L("ما أقل مدة للاستئجار؟", "What is the minimum rental period?"),
             L("يومان.", "Two days.")),
            (L("هل يمكن دمج السيارة مع خدمات أخرى؟", "Can I combine the car with other services?"),
             L("نعم، مثل الاستقبال من باب الطائرة أو الحراسة الشخصية، ضمن طلب واحد.", "Yes, such as airport reception or personal protection, all in one request.")),
            (L("ما طرق الدفع المتاحة؟", "How can I pay?"),
             L("نقداً، أو تحويل بنكي، أو بطاقة.", "Cash, bank transfer or card.")),
        ],
        "gallery": [],
    },
    {
        "slug": "jets",
        "img": "jet-exterior",
        "card_img": "jet-exterior",
        "title": L("الطائرات الخاصة", "Private Jets"),
        "kicker": L("من 6 إلى 16 راكباً", "6 to 16 passengers"),
        "short": L("رحلات خاصة إلى معظم الدول العربية، على جدولك أنت.",
                   "Private flights to most Arab countries, on your schedule."),
        "lead": L("سافر في الوقت الذي يناسبك. نرتّب لك طائرة خاصة تناسب عدد المسافرين ووجهتك، بخصوصية وراحة كاملتين، من لحظة الحجز حتى الهبوط.",
                  "Fly when it suits you. We arrange a private jet sized to your party and destination, with complete privacy and comfort from booking to landing."),
        "meta": L("حجز طائرات خاصة من الأردن إلى معظم الدول العربية، لـ 6 أو 8 أو 12 أو 16 راكباً. الحجز قبل 24 ساعة.",
                  "Private jet charter from Jordan to most Arab countries, for 6, 8, 12 or 16 passengers. Book 24 hours ahead."),
        "includes": [
            L("طائرة بالحجم المناسب لعدد المسافرين", "An aircraft sized to your party"),
            L("تنسيق كامل للرحلة", "Full flight coordination"),
            L("رحلات إلى معظم الدول العربية الآمنة", "Flights to most safe Arab destinations"),
            L("استقبال وسيارة بانتظارك عند الوصول", "Reception and a car waiting on arrival"),
        ],
        "facts": [
            (L("الحجز قبل", "Book at least"), L("24 ساعة", "24 hours ahead")),
            (L("السعة", "Capacity"), L("6 أو 8 أو 12 أو 16 راكباً", "6, 8, 12 or 16 passengers")),
            (L("الوجهات", "Destinations"), L("معظم الدول العربية الآمنة", "Most safe Arab countries")),
        ],
        "faqs": [
            (L("كم من الوقت قبل الرحلة يجب أن أحجز؟", "How far ahead should I book?"),
             L("قبل 24 ساعة على الأقل.", "At least 24 hours before the flight.")),
            (L("ما الوجهات المتاحة؟", "Where can I fly?"),
             L("معظم الدول العربية الآمنة. أخبرنا بوجهتك ونؤكد لك التوفر فوراً.", "Most safe Arab countries. Tell us your destination and we'll confirm availability right away.")),
            (L("ما المعلومات المطلوبة للحجز؟", "What do you need from me to book?"),
             L("عدد المسافرين، ومن أين وإلى أين، وتاريخ الرحلة ووقتها.", "The number of passengers, departure and destination, and the date and time.")),
            (L("هل يمكن ترتيب سيارة عند الوصول؟", "Can you arrange a car on arrival?"),
             L("نعم، ويمكن أن يرافقها فريق حراسة عند الطلب.", "Yes, with a protection team if you wish.")),
        ],
        "gallery": ["jet-cabin-aft", "jet-sofa", "jet-cabin-forward"],
    },
    {
        "slug": "yachts",
        "img": "yacht-exterior",
        "card_img": "yacht-exterior",
        "title": L("اليخوت الفاخرة", "Luxury Yachts"),
        "kicker": L("رحلات بحرية خاصة", "Private cruises"),
        "short": L("ساعات خاصة على البحر، على متن يخوت فاخرة.",
                   "Private hours at sea aboard luxury yachts."),
        "lead": L("ساعات من الهدوء على البحر، لك ولضيوفك فقط. نرتّب لك يختاً فاخراً لرحلة نهارية أو عند الغروب، في معظم الدول.",
                  "Quiet hours at sea, for you and your guests alone. We arrange a luxury yacht for a day or sunset cruise, in most countries."),
        "meta": L("تأجير يخوت فاخرة برحلات خاصة بالساعات، في معظم الدول.",
                  "Luxury yacht charter for private hourly cruises, in most countries."),
        "includes": [
            L("يخوت فاخرة لرحلات خاصة", "Luxury yachts for private cruises"),
            L("رحلات بالساعات، نهاراً أو عند الغروب", "Hourly trips, by day or at sunset"),
            L("متوفرة في معظم الدول", "Available in most countries"),
            L("يمكن تنسيق التنقل إلى المرسى", "Transfer to the marina can be arranged"),
        ],
        "facts": [
            (L("نوع الرحلات", "Trip type"), L("بالساعات، بدون مبيت", "Hourly, no overnight stays")),
            (L("الأماكن", "Locations"), L("معظم الدول", "Most countries")),
        ],
        "faqs": [
            (L("هل تتوفر رحلات مع مبيت؟", "Do you offer overnight trips?"),
             L("لا، الرحلات بالساعات فقط.", "No, trips are by the hour only.")),
            (L("أين تتوفر اليخوت؟", "Where are the yachts available?"),
             L("في معظم الدول. أخبرنا بالمدينة والتاريخ وعدد الضيوف.", "In most countries. Tell us the city, the date and the number of guests.")),
            (L("هل يمكن إضافة سيارة للتنقل إلى المرسى؟", "Can I add a car to the marina?"),
             L("نعم، يمكن دمج أي خدمة من خدماتنا في طلب واحد.", "Yes, any of our services can be combined in one request.")),
        ],
        "gallery": ["yacht-salon"],
    },
    {
        "slug": "protection",
        "img": "convoy-guards",
        "card_img": "convoy-guards",
        "title": L("الحراسة والمرافقة", "Protection & Escort"),
        "kicker": L("أمانك أولاً", "Your safety first"),
        "short": L("حماية شخصية ومرافقة لرجال الأعمال والدبلوماسيين، وتأمين الفعاليات.",
                   "Close protection and escort for executives and diplomats, and event security."),
        "lead": L("أمانك أولاً. فريق ذو خبرة في الحماية الشخصية والمرافقة، يعمل بتكتّم واحترافية، ليبقى تركيزك على ما جئت من أجله.",
                  "Your safety comes first. An experienced close-protection team that works with discretion and professionalism, so you can focus on why you came."),
        "meta": L("حماية شخصية ومرافقة لرجال الأعمال والدبلوماسيين وتأمين الفعاليات في الأردن.",
                  "Close protection, escort and event security in Jordan for executives and diplomats."),
        "includes": [
            L("حماية شخصية لرجال الأعمال والدبلوماسيين", "Close protection for executives and diplomats"),
            L("مرافقة خلال التنقل", "Escort while you travel"),
            L("تأمين الفعاليات", "Event security"),
            L("تكامل مع سياراتنا والاستقبال من المطار", "Works seamlessly with our cars and airport reception"),
        ],
        "facts": [
            (L("لمن", "For"), L("رجال الأعمال، الدبلوماسيين، والفعاليات", "Executives, diplomats and events")),
            (L("الفريق", "Team"), L("ذو خبرة في الحماية", "Experienced in protection")),
            (L("التراخيص", "Licensing"), L("مرخّصون بالكامل", "Fully licensed")),
        ],
        "faqs": [
            (L("من يمكنه طلب الخدمة؟", "Who can request this service?"),
             L("رجال الأعمال، والدبلوماسيون، والشخصيات العامة، ومنظمو الفعاليات.", "Executives, diplomats, public figures and event organizers.")),
            (L("هل تعملون بتراخيص رسمية؟", "Are you licensed?"),
             L("نعم، نعمل بجميع التراخيص اللازمة، ونزوّدك بالتفاصيل عند التواصل.", "Yes, we hold all the required licenses and share the details when you contact us.")),
            (L("هل يمكن تأمين فعالية أو مناسبة؟", "Can you secure an event?"),
             L("نعم، أخبرنا بنوع الفعالية وموعدها وعدد الحضور.", "Yes. Tell us the type of event, the date and the number of guests.")),
        ],
        "gallery": ["escort-tarmac-sunset"],
    },
    {
        "slug": "airport",
        "img": "tarmac-meet",
        "card_img": "tarmac-meet",
        "title": L("الاستقبال من باب الطائرة", "VIP Airport Reception"),
        "kicker": L("من باب الطائرة", "From the aircraft door"),
        "short": L("استقبال VIP من باب الطائرة حتى باب سيارتك.",
                   "VIP reception from the aircraft door to your car."),
        "lead": L("من لحظة هبوط طائرتك، نتولى كل شيء: الاستقبال من باب الطائرة، وإجراءات الجوازات، والأمتعة، وصالة كبار الزوار، حتى تصل إلى سيارتك.",
                  "From the moment you land, we handle everything: reception at the aircraft door, passport formalities, luggage and the VIP lounge, all the way to your car."),
        "meta": L("استقبال VIP من باب الطائرة في مطار الملكة علياء ومطار عمّان المدني: جوازات، أمتعة، صالة VIP وسيارة فاخرة.",
                  "VIP meet and greet from the aircraft door at Queen Alia and Amman Civil airports: passports, luggage, VIP lounge and a luxury car."),
        "includes": [
            L("الاستقبال من باب الطائرة", "Reception at the aircraft door"),
            L("إنهاء إجراءات الجوازات", "Passport formalities handled"),
            L("استلام الأمتعة عنك", "Luggage collected for you"),
            L("صالة كبار الزوار", "VIP lounge"),
            L("سيارة فاخرة بانتظارك", "A luxury car waiting for you"),
        ],
        "facts": [
            (L("المطارات", "Airports"), L("مطار الملكة علياء الدولي، ومطار عمّان المدني (ماركا)", "Queen Alia International and Amman Civil (Marka)")),
            (L("المطلوب منك", "What we need"), L("رقم الرحلة وموعد الوصول وعدد المسافرين", "Flight number, arrival time and number of passengers")),
        ],
        "steps": [
            (L("أرسل بيانات رحلتك", "Send your flight details"),
             L("رقم الرحلة وموعد الوصول وعدد المسافرين.", "Flight number, arrival time and number of passengers.")),
            (L("نؤكد الاستقبال", "We confirm"),
             L("نرسل لك التأكيد وعرض السعر خلال 5 دقائق.", "You get confirmation and a quote within 5 minutes.")),
            (L("نستقبلك من باب الطائرة", "We meet you at the door"),
             L("ونتولى الجوازات والأمتعة عنك.", "And take care of passports and luggage.")),
            (L("إلى سيارتك", "To your car"),
             L("سيارة فاخرة بانتظارك إلى وجهتك.", "A luxury car takes you on to your destination.")),
        ],
        "faqs": [
            (L("ما المطارات التي تغطونها؟", "Which airports do you cover?"),
             L("مطار الملكة علياء الدولي، ومطار عمّان المدني (ماركا).", "Queen Alia International Airport and Amman Civil Airport (Marka).")),
            (L("ماذا تشمل الخدمة؟", "What does the service include?"),
             L("الاستقبال من باب الطائرة، والجوازات، والأمتعة، وصالة كبار الزوار، وسيارة فاخرة.", "Reception at the aircraft door, passports, luggage, the VIP lounge and a luxury car.")),
            (L("هل يمكن إضافة حراسة شخصية؟", "Can I add personal protection?"),
             L("نعم، ضمن نفس الطلب.", "Yes, in the same request.")),
        ],
        "gallery": ["chauffeur-luggage"],
    },
    {
        "slug": "hotels",
        "img": "ritz-carlton-amman",
        "card_img": "ritz-carlton-amman",
        "title": L("حجوزات الفنادق", "Hotel Reservations"),
        "kicker": L("فنادق الخمس نجوم", "Five-star hotels"),
        "short": L("حجوزات في جميع فنادق الخمس نجوم في الأردن.",
                   "Reservations at every five-star hotel in Jordan."),
        "lead": L("أخبرنا بما تفضّله، ونحجز لك في أي فندق خمس نجوم في الأردن، مع تنسيق وصولك وتنقلاتك.",
                  "Tell us what you prefer and we'll book any five-star hotel in Jordan, coordinated with your arrival and transfers."),
        "meta": L("حجوزات فنادق الخمس نجوم في الأردن مع تنسيق الاستقبال من المطار والتنقلات.",
                  "Five-star hotel reservations in Jordan, coordinated with airport reception and transfers."),
        "includes": [
            L("جميع فنادق الخمس نجوم في الأردن", "Every five-star hotel in Jordan"),
            L("الغرفة أو الجناح حسب رغبتك", "The room or suite you prefer"),
            L("تنسيق مع الاستقبال من المطار والسيارة", "Coordinated with airport reception and your car"),
        ],
        "facts": [
            (L("الفنادق", "Hotels"), L("جميع فنادق الخمس نجوم في الأردن", "All five-star hotels in Jordan")),
        ],
        "faqs": [
            (L("في أي فنادق تحجزون؟", "Which hotels can you book?"),
             L("جميع فنادق الخمس نجوم في الأردن.", "Every five-star hotel in Jordan.")),
            (L("هل يمكن دمج الحجز مع الاستقبال والسيارة؟", "Can I combine it with airport reception and a car?"),
             L("نعم، نرتّب لك رحلتك كاملة في طلب واحد.", "Yes, we arrange your whole trip in one request.")),
        ],
        "gallery": [],
    },
    {
        "slug": "concierge",
        "img": "whatever-tray",
        "card_img": "whatever-tray",
        "title": L("Whatever, Whenever", "Whatever, Whenever"),
        "kicker": L("أي طلب، في أي وقت", "Any request, any time"),
        "short": L("أي طلب، في أي وقت. نتولى التفاصيل عنك.",
                   "Any request, at any hour. We handle the details."),
        "lead": L("بعض الطلبات لا تندرج تحت أي قائمة. أخبرنا بما تحتاجه، في أي ساعة من اليوم، ونتولى تنفيذه بدقة وتكتّم.",
                  "Some requests don't fit on any list. Tell us what you need, at any hour, and we'll handle it with precision and discretion."),
        "meta": L("خدمة كونسييرج على مدار الساعة في الأردن: أي طلب، في أي وقت.",
                  "24/7 concierge service in Jordan: whatever you need, whenever you need it."),
        "includes": [
            L("تجهيز المؤتمرات والاجتماعات", "Conference and meeting setup"),
            L("خدمات رجال الأعمال", "Services for business travellers"),
            L("سيارة مع سائق في أي وقت", "A car with a chauffeur at any hour"),
            L("أي طلب خاص آخر", "Any other special request"),
        ],
        "facts": [
            (L("التوفر", "Availability"), L("على مدار الساعة", "Around the clock")),
            (L("الرد", "Response"), L("خلال 5 دقائق", "Within 5 minutes")),
        ],
        "faqs": [
            (L("ما نوع الطلبات التي تنفذونها؟", "What kind of requests do you handle?"),
             L("من تجهيز المؤتمرات وخدمات رجال الأعمال، إلى سيارة مع سائق في منتصف الليل. أخبرنا وسنرتّب الأمر.", "From conference setup and business services to a chauffeured car at midnight. Tell us and we'll arrange it.")),
            (L("هل الخدمة متاحة ليلاً؟", "Is it available at night?"),
             L("نعم، خدمة العملاء متاحة على مدار الساعة.", "Yes, customer service is available around the clock.")),
        ],
        "gallery": ["concierge-gift"],
    },
    {
        "slug": "events",
        "img": "wedding-garden-tables",
        "card_img": "wedding-garden-tables",
        "title": L("الأعراس والمؤتمرات", "Weddings & Conferences"),
        "kicker": L("من الألف إلى الياء", "From A to Z"),
        "short": L("تنظيم الأعراس الفاخرة والمؤتمرات من الألف إلى الياء.",
                   "Luxury weddings and conferences, planned from A to Z."),
        "lead": L("نحن لا ننظّم حفلات فقط، بل نصنع ذكريات لا تُنسى. ننظّم الأعراس الفاخرة والمؤتمرات من الألف إلى الياء، بتصميم خاص لكل مناسبة.",
                  "We don't just organize parties, we create memories that last. We plan luxury weddings and conferences from A to Z, each one designed from scratch."),
        "meta": L("تنظيم أعراس فاخرة ومؤتمرات في الأردن من الألف إلى الياء، مع حجز أي فنان عربي.",
                  "Luxury wedding and conference planning in Jordan from A to Z, including booking any Arab artist."),
        "includes": [
            L("تنظيم وتنسيق كامل من الألف إلى الياء", "Complete planning and coordination, A to Z"),
            L("تصميم خاص لكل عرس، دون باقات جاهزة", "Every wedding designed from scratch, no fixed packages"),
            L("حجز أي فنان عربي لحفلكم", "Any Arab artist booked for your night"),
            L("سيارات الزفة والحراسة والفندق في نفس الطلب", "Wedding cars, protection and hotel in the same request"),
        ],
        "facts": [
            (L("الحجز قبل", "Book at least"), L("3 أشهر من موعد العرس", "3 months before the wedding")),
            (L("المناسبات", "Occasions"), L("الأعراس والمؤتمرات الفاخرة", "Luxury weddings and conferences")),
            (L("الأماكن", "Venues"), L("أغلب فنادق الأردن", "Most hotels in Jordan")),
        ],
        "price": L("عند الطلب، حسب تفاصيل مناسبتكم", "On request, based on your occasion"),
        "faqs": [
            (L("هل لديكم باقات جاهزة؟", "Do you have fixed packages?"),
             L("لا. كل عرس يُصمَّم حسب طلبكم وذوقكم.", "No. Every wedding is designed around your wishes.")),
            (L("متى يجب أن نحجز؟", "When should we book?"),
             L("قبل 3 أشهر على الأقل من موعد العرس.", "At least 3 months before the wedding.")),
            (L("هل يمكنكم إحضار فنان إلى العرس؟", "Can you bring an artist to our wedding?"),
             L("نعم، نحجز لكم أي فنان عربي حسب جدول مواعيده.", "Yes, we book any Arab artist, subject to their schedule.")),
            (L("هل تنظمون الخطوبات والحفلات الصغيرة؟", "Do you plan engagements or small parties?"),
             L("نركّز على الأعراس والمؤتمرات الفاخرة فقط، لنمنحها كامل اهتمامنا.", "We focus only on luxury weddings and conferences, so each gets our full attention.")),
        ],
        "gallery": ["wedding-lounge-lemons"],
    },
]

HOME = {
    "title": L("Titanium Shop | فخامة بلا حد في الأردن", "Titanium Shop | Unlimited Luxury in Jordan"),
    "meta": L("سيارات فاخرة، طائرات خاصة، يخوت، حراسة شخصية، استقبال VIP من المطار، فنادق، وتنظيم أعراس في الأردن. نرد خلال 5 دقائق، على مدار الساعة.",
              "Luxury cars, private jets, yachts, close protection, VIP airport reception, hotels and weddings in Jordan. A reply within 5 minutes, 24/7."),
    "hero_kicker": L("منذ 2018 · عمّان", "Since 2018 · Amman"),
    "hero_title": L("فخامة بلا حد", "Unlimited Luxury"),
    "hero_text": L("من الأرض إلى السماء، كل ما تحتاجه في مكان واحد.",
                   "From the ground to the sky, everything you need in one place."),
    "hero_cta2": L("استكشف خدماتنا", "Explore our services"),
    "intro_title": L("مكان واحد لكل طلباتك", "One place for every request"),
    "intro_text": L("سيارة بانتظارك عند باب الطائرة، وفريق حراسة يرافقك، وجناح جاهز في فندقك، ويخت عند الغروب. نرتّب كل ذلك في طلب واحد، ونتابعه معك حتى آخر تفصيل.",
                    "A car waiting at the aircraft door, a protection team at your side, a suite ready at your hotel, a yacht at sunset. We arrange it all in one request, and follow every detail through."),
    "stats": [
        (L("5 دقائق", "5 min"), L("للرد على طلبك", "to reply to your request")),
        (L("24/7", "24/7"), L("خدمة العملاء", "customer service")),
        (L("2018", "2018"), L("سنة التأسيس", "founded")),
        (L("5 دول", "5 countries"), L("شبكة خدماتنا", "in our network")),
    ],
    "services_title": L("خدماتنا", "Our services"),
    "services_text": L("ثماني خدمات، ومعيار واحد: الكمال.", "Eight services, one standard: perfection."),
    "feature_kicker": L("الاستقبال من باب الطائرة", "VIP airport reception"),
    "feature_title": L("رحلتك تبدأ قبل أن تصل", "Your journey starts before you arrive"),
    "feature_text": L("نستقبلك من باب الطائرة، ونتولى الجوازات والأمتعة، وسيارتك بانتظارك. لا طوابير ولا انتظار.",
                      "We meet you at the aircraft door, handle passports and luggage, and your car is waiting. No queues, no waiting."),
    "fleet_title": L("أسطولنا", "Our fleet"),
    "fleet_text": L("13 سيارة فاخرة، موديلات 2024–2026، مع سائق أو بدون.",
                    "Thirteen luxury cars, 2024–2026 models, with or without a chauffeur."),
    "fleet_cta": L("شاهد الأسطول كاملاً", "View the full fleet"),
    "celebs_title": L("وثقوا بنا", "They trusted us"),
    "celebs_text": L("نجوم العالم والوطن العربي يختارون Titanium Shop عند زيارتهم الأردن.",
                     "Stars from around the world and the Arab region choose Titanium Shop when they visit Jordan."),
    "founder_kicker": L("كلمة المؤسس", "From our founder"),
    "founder_quote": L("نؤمن بأن الفخامة الحقيقية لا تكتمل إلا بالثقة.",
                       "We believe true luxury is built on trust."),
    "founder_cta": L("تعرّف علينا", "About us"),
}

ABOUT = {
    "title": L("من نحن", "About us"),
    "meta": L("Titanium Shop منذ 2018 في عمّان: خدمات الفخامة لرجال الأعمال والفنانين وضيوف الأردن، في مكان واحد.",
              "Titanium Shop, Amman, since 2018: luxury services for executives, artists and guests of Jordan, all in one place."),
    "lead": L("تأسست Titanium Shop عام 2018 في عمّان، بفكرة واحدة: أن يجد ضيوفنا كل ما يحتاجونه من خدمات الفخامة في مكان واحد، من السيارات والطائرات الخاصة واليخوت، إلى الحماية الشخصية والاستقبال من المطار وتنظيم الأعراس.",
              "Titanium Shop was founded in Amman in 2018 with a single idea: that our guests should find every luxury service they need in one place, from cars, private jets and yachts to close protection, airport reception and weddings."),
    "values_title": L("مبادئنا", "Our principles"),
    "values": [
        (L("المصداقية", "Integrity"), L("نَعِد بما نستطيع، ونفي بكل ما نَعِد.", "We promise what we can deliver, and deliver all we promise.")),
        (L("الدقة", "Precision"), L("في كل موعد، وفي كل تفصيل.", "In every appointment and every detail.")),
        (L("حماية الضيف", "Guest protection"), L("نحمي ضيوفنا من أي خطأ، مهما كان صغيراً.", "We protect our guests from even the smallest mistake.")),
    ],
    "network_title": L("شبكتنا", "Our network"),
    "network_text": L("الأردن مقرّنا، مع شبكة تعاون في دبي والسعودية ومصر ولبنان.",
                      "Jordan is our home, with a partner network in Dubai, Saudi Arabia, Egypt and Lebanon."),
    "founder_title": L("كلمة المؤسس", "Founder's message"),
    "founder_paragraphs": [
        L("منذ أن أسّسنا Titanium Shop عام 2018، كان هدفنا واضحاً: أن نقدّم لضيوفنا فخامةً بلا حدود، وأن نكون الجهة الواحدة التي تلبّي كل طلباتهم، من الأرض إلى السماء.",
          "When we founded Titanium Shop in 2018, our goal was clear: to offer our guests unlimited luxury, and to be the one place that answers every request, from the ground to the sky."),
        L("نؤمن بأن الفخامة الحقيقية لا تكتمل إلا بالثقة. لذلك بنينا عملنا على ثلاثة مبادئ لا نتنازل عنها: المصداقية في كل وعد، والدقة في كل موعد، وحماية ضيوفنا من أي خطأ مهما كان صغيراً.",
          "We believe true luxury is built on trust. That is why our work rests on three principles we never compromise: integrity in every promise, precision in every appointment, and protecting our guests from even the smallest mistake."),
        L("سواء كنت رجل أعمال، أو فناناً، أو ضيفاً يزور الأردن، فإن فريقنا في خدمتك على مدار الساعة. اطلب ما تشاء، ومتى تشاء، واترك التفاصيل علينا.",
          "Whether you are a business leader, an artist, or a guest visiting Jordan, our team is at your service around the clock. Whatever you need, whenever you need it, leave the details to us."),
    ],
    "founder_name": L("حمزة خشمان", "Hamza Khashman"),
    "founder_role": L("المؤسس والرئيس التنفيذي", "Founder & CEO"),
}

CONTACT_PAGE = {
    "title": L("تواصل معنا", "Contact us"),
    "meta": L("اطلب أي خدمة من Titanium Shop عبر الواتساب أو الهاتف أو نموذج الطلب. نرد خلال 5 دقائق، على مدار الساعة.",
              "Request any Titanium Shop service by WhatsApp, phone or our form. We reply within 5 minutes, 24/7."),
    "lead": L("أخبرنا بما تحتاجه، ونعود إليك خلال 5 دقائق.", "Tell us what you need, and we'll get back to you within 5 minutes."),
    "form_title": L("نموذج الطلب", "Request form"),
    "direct_title": L("تواصل مباشر", "Direct contact"),
    "name": L("الاسم الكامل", "Full name"),
    "phone": L("رقم الهاتف (مع رمز الدولة)", "Phone number (with country code)"),
    "email": L("البريد الإلكتروني (اختياري)", "Email (optional)"),
    "service": L("الخدمة المطلوبة", "Service"),
    "choose": L("اختر الخدمة", "Choose a service"),
    "other": L("طلب آخر", "Other request"),
    "date": L("التاريخ", "Date"),
    "details": L("تفاصيل إضافية (اختياري)", "Additional details (optional)"),
    "send": L("إرسال الطلب", "Send request"),
    "note": L("بالضغط على إرسال، أنت توافق على سياسة الخصوصية. نستخدم بياناتك فقط للرد على طلبك.",
              "By sending, you agree to our privacy policy. We only use your details to reply to your request."),
    "driver": L("السائق", "Chauffeur"),
    "with_driver": L("مع سائق", "With chauffeur"),
    "self_drive": L("بدون سائق", "Self-drive"),
    "days": L("عدد الأيام", "Number of days"),
    "car": L("السيارة المفضّلة (اختياري)", "Preferred car (optional)"),
    "passengers": L("عدد المسافرين", "Passengers"),
    "route": L("من أين وإلى أين", "From – to"),
    "guests": L("عدد الضيوف", "Number of guests"),
    "city": L("المدينة أو الدولة", "City or country"),
    "airport": L("المطار", "Airport"),
    "flight": L("رقم الرحلة وموعد الوصول", "Flight number and arrival time"),
    "event_type": L("نوع المناسبة", "Occasion"),
    "wedding": L("عرس", "Wedding"),
    "conference": L("مؤتمر", "Conference"),
    "mgmt": L("الإدارة والشكاوى", "Management & complaints"),
    "address_title": L("العنوان", "Address"),
    "open_map": L("افتح على الخريطة", "Open in Maps"),
    "hours_title": L("أوقات الخدمة", "Hours"),
}

THANKS = {
    "title": L("شكراً لك", "Thank you"),
    "text": L("وصلنا طلبك، وسيتواصل معك فريقنا خلال 5 دقائق.",
              "We've received your request. Our team will contact you within 5 minutes."),
    "wa_text": L("مستعجل؟ تابع طلبك مباشرة على الواتساب.", "In a hurry? Continue on WhatsApp now."),
    "wa_btn": L("تابع على الواتساب", "Continue on WhatsApp"),
}

NOT_FOUND = {
    "title": L("الصفحة غير موجودة", "Page not found"),
    "text": L("يبدو أن هذه الصفحة غير موجودة. لكننا هنا لأي طلب آخر.",
              "This page doesn't seem to exist. But we're here for anything else."),
}

PRIVACY = {
    "title": L("سياسة الخصوصية", "Privacy policy"),
    "sections": [
        (L("ما البيانات التي نجمعها", "What we collect"),
         L("عند إرسال نموذج الطلب، نستلم الاسم ورقم الهاتف، والبريد الإلكتروني إن أضفته، وتفاصيل الخدمة التي تطلبها.",
           "When you send the request form, we receive your name, phone number, email if you add it, and the details of the service you request.")),
        (L("كيف نستخدمها", "How we use it"),
         L("نستخدم بياناتك فقط للرد على طلبك وتنفيذ الخدمة. لا نبيعها ولا نشاركها لأغراض تسويقية.",
           "We use your details only to reply to your request and deliver the service. We never sell them or share them for marketing.")),
        (L("كيف تصلنا", "How it reaches us"),
         L("يُرسَل النموذج إلى بريدنا الإلكتروني عبر خدمة FormSubmit. وإذا تابعت عبر الواتساب، تخضع المحادثة لسياسة واتساب.",
           "The form is delivered to our email through the FormSubmit service. If you continue on WhatsApp, the conversation is subject to WhatsApp's policy.")),
        (L("ملفات تعريف الارتباط", "Cookies"),
         L("لا يستخدم هذا الموقع ملفات تعريف ارتباط للتتبع أو الإعلانات.",
           "This website does not use tracking or advertising cookies.")),
        (L("حقوقك", "Your rights"),
         L("يمكنك طلب الاطلاع على بياناتك أو حذفها في أي وقت عبر البريد الإلكتروني titaniumshopjo@gmail.com.",
           "You can ask to see or delete your details at any time by emailing titaniumshopjo@gmail.com.")),
    ],
}
