# جزوه جامع راه‌اندازی اولیه و ساختاربندی حرفه‌ای پروژه Django

---

## Step 1: نقشه راه (Syllabus)

1. ساخت و فعال‌سازی محیط مجازی (Virtual Environment)
2. نصب فریم‌ورک Django
3. برون‌ریزی بسته‌ها در `requirements.txt`
4. خواندن و نصب دسته‌جمعی پکیج‌ها از روی فایل نیازمندی‌ها
5. غیرفعال‌سازی محیط مجازی
6. مقدمات پیکربندی پروژه
7. راه‌اندازی Git و اتصال به مخزن GitHub
8. ساخت فایل `.gitignore` استاندارد
9. فعال‌سازی مجدد محیط مجازی
10. ایجاد ساختار اولیه پروژه با دستور `django-admin startproject config .`
11. بررسی و تشریح فایل‌های هسته پروژه و تنظیمات `settings.py`
12. اجرای سرور توسعه (`runserver`)
13. تست تغییر مقادیر `DEBUG = False` و `ALLOWED_HOSTS`
14. بررسی خطای Bad Request (400)
15. ریشه‌یابی خطای ۴۰۰ در صورت درج پروتکل یا پورت و شیوه رفع آن
16. کدهای وضعیت پروتکل انتقال ابرمتن (HTTP Status Codes)
17. بررسی خطای Not Found (404) در چرخه درخواست
18. پیش‌نیازهای اتصال PostgreSQL به جنگو
19. ایجاد دیتابیس در PostgreSQL
20. نصب درایور ارتباطی `psycopg2`
21. جایگزینی SQLite با PostgreSQL در تنظیمات دیتابیس
22. تحلیل دستور `makemigrations` و دلیل بروز پیام `No changes detected`
23. آماده‌سازی جداول سیستمی در دیتابیس
24. اجرای دستور `migrate`
25. بررسی و صحت‌سنجی رفع هشدار Migration Pending در زمان اجرای سرور
26. تفکیک محیط‌های توسعه (Development) و استقرار نهایی (Production)
27. کاربرد و شیوه نصب پکیج `python-decouple`
28. ایجاد فایل `.env` و ذخیره امن داده‌های حساس
29. شیوه فراخوانی و اعتبارسنجی متغیرها با `config` و `Csv`
30. معماری ماژولار تنظیمات پروژه (Multi-Settings Architecture)
31. تبدیل فایل تنظیمات به پکیج با ساخت دایرکتوری `settings`
32. ایجاد ماژول‌های `__init__.py`، `base.py`، `dev.py` و `prod.py`
33. انتقال تنظیمات عمومی به `base.py` و پاک‌سازی فایل قدیمی
34. مدیریت خودکار لود تنظیمات بر اساس متغیرهای محیطی در `__init__.py`
35. تصحیح متغیر `BASE_DIR` و اختصاص تنظیمات تفکیکی
36. تنظیم مسیر جدید ماژول تنظیمات در فایل اجرایی `manage.py`
37. ریشه‌یابی و رفع خطای `ModuleNotFoundError`
38. راه‌اندازی سرور با فلگ صریح `--settings`
39. تعریف پیش‌فرض محیط با متغیر محیطی `DJANGO_SETTINGS_MODULE`
40. تفاوت بنیادین فایل‌های ایستا (`Static`) و فایل‌های بارگذاری‌شده (`Media`)
41. کاربرد پارامتر `STATIC_URL`
42. تنظیم عملیاتی `STATIC_URL`
43. تنظیم عملیاتی `MEDIA_URL`
44. کاربرد دایرکتوری‌های ریشه و سیستم ذخیره‌سازی (`STATIC_ROOT` و `MEDIA_ROOT`)
45. تعریف مسیرهای سفارشی با `STATICFILES_DIRS`
46. مفهوم ماژولار بودن جنگو و ساخت اپلیکیشن
47. ایجاد اپلیکیشن `user` با `startapp`
48. تشریح اجزای اپلیکیشن و لزوم افزودن `urls.py`
49. تفاوت مسیریابی ریشه پروژه با مسیریابی داخلی اپلیکیشن
50. ثبت مسیرهای اپلیکیشن در پروژه با تابع `path` و `include`
51. ثبت و فعال‌سازی نهایی اپلیکیشن در آرایه `INSTALLED_APPS`

---

## Step 2: آموزش جامع و گام‌به‌گام

### ۱. ساخت و فعال‌سازی محیط مجازی

برای جلوگیری از تداخل نسخه‌های مختلف پکیج‌ها میان پروژه‌ها، از یک محیط ایزوله استفاده می‌کنیم:

```bash
# لینوکس و مک
python3 -m venv venv
source venv/bin/activate

# ویندوز (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

```

خروجی در ترمینال (پیشوند محیط فعال‌شده):

```text
(venv) user@system:~/project$

```

---

### ۲. نصب جنگو

نصب فریم‌ورک جنگو درون محیط فعال:

```bash
pip install django

```

خروجی:

```text
Collecting django
  Downloading Django-5.1.x-py3-none-any.whl (...)
Installing collected packages: asgiref, sqlparse, django
Successfully installed asgiref-3.8.1 django-5.1.0 sqlparse-0.5.1

```

---

### ۳. نمایش کتابخانه‌ها داخل فایل requirements.txt

ذخیره فهرست دقیق پکیج‌های نصب‌شده به همراه نسخه آن‌ها:

```bash
pip freeze > requirements.txt
cat requirements.txt

```

خروجی:

```text
asgiref==3.8.1
Django==5.1.0
sqlparse==0.5.1

```

---

### ۴. خواندن کتابخانه‌ها از داخل فایل و نصب یکجای آن‌ها

در صورتی که پروژه را روی سرور یا سیستم دیگری بالا بیاورید، تمام پیش‌نیازها به شکل یکجا نصب می‌شوند:

```bash
pip install -r requirements.txt

```

خروجی:

```text
Requirement already satisfied: asgiref==3.8.1 in ./venv/lib/...
Requirement already satisfied: Django==5.1.0 in ./venv/lib/...
Requirement already satisfied: sqlparse==0.5.1 in ./venv/lib/...

```

---

### ۵. غیرفعال کردن محیط مجازی

برای خروج موقت از محیط مجازی:

```bash
deactivate

```

خروجی:

```text
user@system:~/project$
# پیشوند (venv) از ابتدای خط فرمان حذف می‌شود.

```

---

### ۶. شروع تنظیمات پروژه جنگو

پوشه پروژه باید ساختار استانداردی داشته باشد. پوشه اصلی را آماده کرده و وارد آن می‌شویم.

---

### ۷. ساخت گیت و لینک کردن ریپازیتوری گیت‌هاب

کنترل نسخه پروژه با گیت:

```bash
git init
git branch -M main
git remote add origin https://github.com/username/Silvermoon-test-project.git

```

خروجی:

```text
Initialized empty Git repository in /path/to/project/.git/

```

---

### ۸. ساخت فایل .gitignore در آدرس اصلی فایل‌ها

فایل‌هایی مانند کش پایتون، محیط مجازی و فایل‌های حساس نباید روی گیت‌هاب قرار گیرند. فایلی با نام `.gitignore` در ریشه پروژه بسازید:

```text
venv/
*.pyc
__pycache__/
db.sqlite3
.env
media/
staticfiles/
.DS_Store

```

---

### ۹. فعال‌سازی مجدد محیط مجازی

```bash
# لینوکس/مک:
source venv/bin/activate

# ویندوز:
.\venv\Scripts\Activate.ps1

```

خروجی:

```text
(venv) user@system:~/project$

```

---

### ۱۰. استارت پروژه با نقطه انتهایی

استفاده از کاراکتر نقطه (`.`) از ایجاد یک پوشه تو در توی اضافی جلوگیری می‌کند و فایل `manage.py` را مستقیماً در ریشه پروژه قرار می‌دهد:

```bash
django-admin startproject config .

```

خروجی در فایل سیستم:

```text
.
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── .gitignore

```

---

### ۱۱. توضیح کلی فایل‌های پوشه config

- `manage.py`: اسکریپت خط فرمانی جنگو برای اجرای تسک‌های مدیریتی (اجرای سرور، مایگریشن و...).
- `config/__init__.py`: یک فایل خالی که به پایتون می‌فهماند این دایرکتوری یک ماژول پایتونی است.
- `config/wsgi.py`: واسط WSGI (Web Server Gateway Interface) جهت استقرار همگام (Synchronous) روی وب‌سرورهایی مانند Gunicorn/uWSGI.
- `config/asgi.py`: واسط ASGI جهت پشتیبانی از اتصالات ناهمگام (Asynchronous) مانند WebSockets.
- `config/urls.py`: جدول مرکزی مسیریابی درخواست‌های ورودی به سمت Viewهای مربوطه.
- `config/settings.py`: قلب تپنده پیکربندی‌های کلی پروژه:
- `BASE_DIR`: آدرس پوشه ریشه پروژه در سیستم‌عامل.
- `SECRET_KEY`: کلید امنیتی برای هش کردن نشست‌ها، توکن‌های CSRF و رمزگذاری داده‌ها.
- `DEBUG`: حالت اشکال‌زدایی؛ در زمان توسعه فعال (`True`) و در زمان پروداکشن حتماً باید غیرفعال (`False`) باشد.
- `ALLOWED_HOSTS`: دامنه‌ها و آی‌پی‌هایی که مجاز به پاسخگویی به درخواست‌های ورودی به این پروژه هستند.
- `INSTALLED_APPS`: آرایه‌ای از اپلیکیشن‌های فعال پروژه (شامل ماژول‌های داخلی جنگو و اپ‌های سفارشی).
- `MIDDLEWARE`: لایه‌های پردازشی میان درخواست کاربر و پاسخ ویوها (احراز هویت، امنیت، سشن و...).
- `ROOT_URLCONF`: آدرس ماژول اصلی مسیریابی جنگو.
- `TEMPLATES`: موتور رندر قالب‌های HTML.
- `DATABASES`: تنظیمات موتور دیتابیس پروژه.
- `AUTH_PASSWORD_VALIDATORS`: قوانین امنیتی پسورد کاربران.
- `LANGUAGE_CODE` و `TIME_ZONE`: بومی‌سازی زمان و زبان.

---

### ۱۲. اجرای سرور توسعه

دستور اجرای سرور توسعه محلی:

```bash
python manage.py runserver

```

خروجی:

```text
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s)...
Django version 5.1, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

---

### ۱۳. تست مقادیر DEBUG = False و ALLOWED_HOSTS

در فایل `config/settings.py` این تغییر را اعمال کنید:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain', 'localhost']

```

با اجرای `python manage.py runserver` و باز کردن `[http://127.0.0.1:8000](http://127.0.0.1:8000)` در مرورگر، خطای زیر رخ می‌دهد:

```text
Command Error: Bad Request (400)

```

---

### ۱۴. توضیح ارور Bad Request (400)

کد ۴۰۰ به این معناست که سرور درخواست را به دلیل نامعتبر بودن پردازش نمی‌کند.
وقتی `DEBUG = False` می‌شود، جنگو الزامات امنیتی سفت‌وسختی را روی هدر `Host` درخواست اعمال می‌کند. از آنجا که شما با آدرس `127.0.0.1` سایت را باز کرده‌اید، اما در `ALLOWED_HOSTS` فقط `'localhost'` را تعریف کرده‌اید، جنگو این درخواست را مسدود می‌کند.

---

### ۱۵. دلیل بروز ارور ۴۰۰ با وجود نوشتن URL کامل و شیوه حل آن

اگر متغیر را به این شکل بنویسید:

```python
# غلط:
ALLOWED_HOSTS = ['yourdomain', 'http://127.0.0.1:8000/']

```

باز هم با خطای ۴۰۰ مواجه خواهید شد.
**دلیل:** مقدار `ALLOWED_HOSTS` صرفاً نام دامنه یا آدرس IP است (**Hostname**)، نه پروتکل و مسیر (**Uniform Resource Locator**). پروتکل (`http://`)، پورت (`:8000`) و اسلش پایانی (`/`) جزء Host نیستند.

**فرم صحیح:**

```python
ALLOWED_HOSTS = ['yourdomain', '127.0.0.1', 'localhost']

```

---

### ۱۶. کدهای وضعیت HTTP (HTTP Status Codes)

تمام تعاملات کلاینت-سرور با کدهای وضعیت پاسخ داده می‌شوند. استاندارد دسته‌بندی:

- **1xx (Informational):** دریافت درخواست و ادامه پردازش.
- **2xx (Success):** موفقیت‌آمیز بودن عملیات (مانند `200 OK`, `201 Created`).
- **3xx (Redirection):** نیاز به اقدام اضافی برای انتقال آدرس (مانند `301 Moved Permanently`, `302 Found`).
- **4xx (Client Error):** خطای سمت کلاینت در ارسال درخواست (مانند `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`).
- **5xx (Server Error):** خطای سمت سرور حین پردازش درخواست (مانند `500 Internal Server Error`, `502 Bad Gateway`).

> عبارت **"HTTP response status codes"** را در مستندات MDN سرچ کنید تا تمام کدها را دقیق مطالعه کنید.

---

### ۱۷. خطای Not Found (404)

اگر آدرسی را در مرورگر وارد کنید که برای آن هیچ روت یا مسیری در `urls.py` تعریف نشده باشد، جنگو این خطا را صادر می‌کند:

```text
[22/Sep/2026 12:00:00] "GET /unknown-path/ HTTP/1.1" 404 2110

```

در حالت `DEBUG = True`، لیست تمام مسیرهای معتبر به شما نشان داده می‌شود. در حالت `DEBUG = False`، صفحه امن و سفارشی ۴۰۴ به کاربر نمایش داده خواهد شد.

---

### ۱۸. اتصال PostgreSQL به جنگو

برای رفتن به سطح استاندارد محیط‌های عملیاتی، پایگاه داده SQLite3 را کنار گذاشته و از PostgreSQL استفاده می‌کنیم. مطمئن شوید سرور PostgreSQL روی سیستم نصب و سرویس آن در پورت ۵۴۳۲ در حال اجراست.

---

### ۱۹. ساخت دیتابیس داخل PostgreSQL

وارد محیط خط فرمان `psql` شوید و دیتابیس را بسازید:

```bash
# ورود به psql با کاربر postgres
sudo -u postgres psql

```

دستورات SQL برای ساخت دیتابیس:

```sql
CREATE DATABASE "Silvermoon-test-project";
\q

```

خروجی:

```text
CREATE DATABASE

```

---

### ۲۰. نصب درایور psycopg2

جنگو برای ارتباط پایتون با دیتابیس Postgres به رابط C یا باینری نیاز دارد:

```bash
pip install psycopg2-binary

```

خروجی:

```text
Collecting psycopg2-binary
  Downloading psycopg2_binary-2.9.9-...whl (...)
Successfully installed psycopg2-binary-2.9.9

```

---

### ۲۱. جایگزینی SQLite با PostgreSQL در settings.py

بخش `DATABASES` را در فایل تنظیمات به شکل زیر ویرایش کنید:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Silvermoon-test-project',
        'USER': 'postgres',
        'PASSWORD': 'your_secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

---

### ۲۲. توضیح کاربرد makemigrations و دلیل No changes detected

```bash
python manage.py makemigrations

```

خروجی:

```text
No changes detected

```

**تحلیل:**
دستور `makemigrations` کدهای موجود در فایل‌های `models.py` اپلیکیشن‌های شما را اسکن کرده و تغییرات ساختار داده‌ها را به قالب فایل‌های دستوری پایتونی (Migration Files) تبدیل می‌کند.
دلیل دریافت `No changes detected` این است که شما هنوز هیچ اپلیکیشن و مدل جدیدی ایجاد نکرده‌اید که نیاز به ساخت فایل مایگریشن داشته باشد.

---

### ۲۳ و ۲۴. شناساندن دیتابیس به جنگو و اجرای migrate

اپلیکیشن‌های پیش‌فرض جنگو (auth, admin, contenttypes, sessions) فایل‌های مایگریشن آماده دارند اما هنوز روی PostgreSQL اعمال نشده‌اند:

```bash
python manage.py migrate

```

خروجی:

```text
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying sessions.0001_initial... OK

```

---

### ۲۵. تست اجرای سرور بدون خطای Migration Pending

حالا مجدداً سرور را ران کنید:

```bash
python manage.py runserver

```

خروجی:

```text
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 5.1, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
# دقت کنید که پیام قرمز رنگ اخطار unapplied migrations کاملاً برطرف شده است.

```

---

### ۲۶. تعریف دو استیج Development و Production

- **Development (توسعه):** محیط لوکال شما؛ نیازمند `DEBUG = True`، پیام‌های خطای خوانا، و دیتابیس تستی محلی.
- **Production (پروداکشن):** سرور نهایی در دسترس کاربران؛ نیازمند `DEBUG = False`، لایه‌های امنیتی SSL/HSTS، دیتابیس پایدار و کلیدهای رمزگذاری محافظت‌شده.

---

### ۲۷. نصب پکیج python-decouple

این پکیج متغیرهای محیطی و حساس را از سورس‌کد جدا می‌کند تا سورس شما ایمن بماند و روی گیت قرار نگیرد:

```bash
pip install python-decouple

```

خروجی:

```text
Successfully installed python-decouple-3.8

```

---

### ۲۸. ساخت فایل .env

یک فایل به نام `.env` در ریشه پروژه (کنار `manage.py`) بسازید:

```ini
D_SECRET_KEY=django-insecure-_@@bjhpe3mtmu9gv!5zigj#z6u2bk@6l8segx94j1ufo7$1c_w
D_DEBUG=True
D_ALLOWED_HOSTS=localhost,127.0.0.1
D_NAME=Silvermoon-test-project
D_USER=postgres
D_PASSWORD=your_secure_password
D_HOST=localhost
D_PORT=5432

```

**دلیل استفاده از پیشوند `D_`:**
پیشوندگذاری (Namespace) مانند `D_` (مخفف Django) مانع از تداخل متغیرهای این پروژه با متغیرهای سیستمی و سراسری سرور سیستم‌عامل (OS Environment Variables) می‌شود.

---

### ۲۹. نحوه ایمپورت decouple

در بالای فایل تنظیمات:

```python
from decouple import config, Csv

# خواندن متغیر با تعیین مقدار پیش‌فرض و Type Casting
SECRET_KEY = config('D_SECRET_KEY')
DEBUG = config('D_DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('D_ALLOWED_HOSTS', cast=Csv())

```

---

### ۳۰ و ۳۱. ساخت پوشه settings در داخل config

برای معماری ماژولار:

```bash
mkdir config/settings

```

---

### ۳۲. ایجاد فایل‌های تفکیکی در settings

درون `config/settings/` چهار فایل ایجاد کنید:

```bash
touch config/settings/__init__.py
touch config/settings/base.py
touch config/settings/dev.py
touch config/settings/prod.py

```

---

### ۳۳. انتقال تنظیمات به base.py و حذف settings.py قدیمی

محتوای فایل قبلی `config/settings.py` را کات کرده و درون `config/settings/base.py` قرار دهید. سپس فایل قبلی را حذف کنید:

```bash
rm config/settings.py

```

---

### ۳۴. تنظیم خودکار فایل `__init__.py`

برای اینکه مشخص کنیم بر اساس متغیر محیطی کدام تنظیمات خوانده شود، در `config/settings/__init__.py` می‌نویسیم:

```python
from decouple import config

# پیش‌فرض روی محیط توسعه تنظیم می‌شود
ENVIRONMENT = config('DJANGO_ENV', default='dev')

if ENVIRONMENT == 'prod':
    from .prod import *
else:
    from .dev import *

```

---

### ۳۵. تصحیح BASE_DIR و تفکیک فایل‌ها

چون فایل `base.py` یک پله عمیق‌تر از فایل قبلی رفته است، باید یک `.parent` دیگر به `BASE_DIR` اضافه کنیم تا ریشه پروژه به درستی شناسایی شود:

در `config/settings/base.py`:

```python
from pathlib import Path
from decouple import config, Csv

# قبلاً: Path(__file__).resolve().parent.parent
# اکنون: سه بار parent می‌گیریم تا به پوشه اصلی پروژه برسیم
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('D_SECRET_KEY')
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('D_NAME'),
        'USER': config('D_USER'),
        'PASSWORD': config('D_PASSWORD'),
        'HOST': config('D_HOST'),
        'PORT': config('D_PORT'),
    }
}

```

در `config/settings/dev.py`:

```python
from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

```

در `config/settings/prod.py`:

```python
from .base import *

DEBUG = False
ALLOWED_HOSTS = config('D_ALLOWED_HOSTS', cast=Csv())
# تنظیمات امنیتی پروداکشن
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

```

---

### ۳۶ و ۳۷. ریشه‌یابی خطای ModuleNotFoundError و تنظیم manage.py

اگر فایل `settings.py` قبلی را حذف کرده باشید، اجرای دستورات با خطای زیر متوقف می‌شود:

```text
ModuleNotFoundError: No module named 'config.settings'

```

**ریشه خطا:** در فایل‌های `manage.py`, `wsgi.py` و `asgi.py` مسیر ماژول به صورت `config.settings` ثبت شده است، در حالی که ما پوشه‌ای به همین نام ساختیم که فایل `__init__.py` دارد. پایتون به صورت پیش‌فرض پوشه `config/settings` را به عنوان یک پکیج می‌شناسد. اگر لود پیش‌فرض پکیج انجام نشود یا بخواهید صراحتاً فایل مشخص را بدهید، باید آن را آدرس‌دهی کنید.

در `manage.py` خط زیر را اصلاح کنید:

```python
# خط پیش‌فرض:
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# مسیر صریح و بدون ابهام:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

```

---

### ۳۸. اجرای سرور با فلگ صریح --settings

شما می‌توانید مشخصاً اعلام کنید سرور با کدام فایل بالا بیاید:

```bash
python manage.py runserver --settings=config.settings.dev

```

خروجی:

```text
Django version 5.1, using settings 'config.settings.dev'
Starting development server at http://127.0.0.1:8000/

```

---

### ۳۹. تعیین پیش‌فرض محیط با متغیر محیطی DJANGO_SETTINGS_MODULE

در سطح سیستم‌عامل می‌توانید متغیر را ست کنید تا دیگر نیازی به نوشتن فلگ نباشد:

```bash
# لینوکس/مک
export DJANGO_SETTINGS_MODULE=config.settings.dev

# ویندوز PowerShell
$env:DJANGO_SETTINGS_MODULE="config.settings.dev"

```

---

### ۴۰. تفاوت بنیادین فایل‌های Static و Media

- **Static Files:** فایل‌های ایستا که توسط **توسعه‌دهنده** آماده شده و بدنه فرانت‌اند را می‌سازند (CSS, JS, فونت‌ها، تصاویر قالب). این فایل‌ها با تغییر کارکرد کاربر تغییر نمی‌کنند.
- **Media Files:** فایل‌هایی که توسط **کاربر یا مدیر سیستم** حین استفاده از نرم‌افزار بارگذاری می‌شوند (عکس پروفایل، فایل رزومه، تصاویر مقالات).

---

### ۴۱ و ۴۲. مفهوم و کاربرد STATIC_URL

آدرس پیشوند URL است که کلاینت‌ها از طریق مرورگر می‌توانند به فایل‌های استاتیک دسترسی پیدا کنند:

در `config/settings/base.py`:

```python
STATIC_URL = 'static/'

```

وقتی کاربر تصویری به نام `logo.png` را صدا می‌زند، آدرس درخواست برابر `[http://domain.com/static/logo.png](http://domain.com/static/logo.png)` خواهد بود.

---

### ۴۳. مفهوم و کاربرد MEDIA_URL

پیشوند URL جهت دسترسی عمومی مرورگر به فایل‌های بارگذاری شده توسط کاربران:

در `config/settings/base.py`:

```python
MEDIA_URL = 'media/'

```

---

### ۴۴. کاربرد دایرکتوری‌های ریشه (STATIC_ROOT و MEDIA_ROOT)

- `MEDIA_ROOT`: آدرس مطلق فیزیکی در هارددیسک سیستم که فایل‌های بارگذاری شده کاربران باید در آنجا ذخیره شوند.
- `STATIC_ROOT`: مسیری روی دیسک که با اجرای دستور `collectstatic`، جنگو تمام استاتیک‌های اپ‌های مختلف را در آنجا یکپارچه می‌کند تا وب‌سروری مانند Nginx مستقیماً به آن سرویس دهد.

در `config/settings/base.py`:

```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_ROOT = BASE_DIR / 'media'

```

---

### ۴۵. مسیرهای استاتیک سفارشی با STATICFILES_DIRS

اگر فایل‌های استاتیکی دارید که متعلق به یک اپلیکیشن خاص نیستند (مانند قالب کلی سایت)، پوشه‌ای به نام `static` در ریشه پروژه ساخته و آدرس آن را به جنگو معرفی کنید:

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

```

---

### ۴۶ و ۴۷. ساخت اپلیکیشن user

جنگو از معماری کامپوننت‌محور با اپ‌های مستقل استفاده می‌کند:

```bash
python manage.py startapp user

```

خروجی در فایل سیستم:

```text
user/
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

```

---

### ۴۸. تشریح فایل‌های داخل اپ و ساخت urls.py

- `models.py`: ساختار دیتابیس و مدل‌های ORM.
- `views.py`: متدهای پردازش درخواست کاربر و تولید پاسخ (Logic).
- `admin.py`: تنظیمات نحوه نمایش مدل‌ها در پنل ادمین جنگو.
- `apps.py`: تنظیمات متادیتای اپلیکیشن.
- `tests.py`: کدهای تست خودکار (Unit Tests).
- `migrations/`: تاریخچه تغییرات ساختاری دیتابیس این اپ.

برای تفکیک تمیز مسیرها، فایلی به نام `urls.py` داخل پوشه `user` ایجاد کنید:

```bash
touch user/urls.py

```

---

### ۴۹. تفاوت urls داخل اپ با config/urls.py

- `config/urls.py`: دروازه ورودی اصلی سرور است؛ این فایل به عنوان هاب مرکزی مشخص می‌کند هر آدرس پایه به کدام اپ هدایت شود.
- `user/urls.py`: مسیریابی‌های ریز و اختصاصیِ همان اپ را نگه‌داری می‌کند (مانند `/login`, `/profile`).

---

### ۵۰. اتصال مسیرهای اپ به پروژه با include و path

در فایل `user/urls.py`:

```python
from django.urls import path

urlpatterns = [
    # مسیرهای داخلی اپلیکیشن اینجا قرار می‌گیرند
]

```

در فایل اصلی `config/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
]

```

---

### ۵۱. ثبت نهایی اپ در INSTALLED_APPS

برای اینکه جنگو مدل‌ها و تمپلیت‌های این اپلیکیشن را بارگذاری کند، کلاس کانفیگ آن را در `config/settings/base.py` اضافه کنید:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom Apps
    'user.apps.UserConfig',
]

```

تست نهایی برای اطمینان از سلامت کامل اتصالات و تنظیمات:

```bash
python manage.py check

```

خروجی:

```text
System check identified no issues (0 silenced).

```
