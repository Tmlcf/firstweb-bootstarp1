ไฟล์และโฟลเดอร์ที่ควรมีในโปรเจกต์ Django ของคุณ:

mywebbst/
├── mysite/                # Django project
│   ├── manage.py
│   ├── db.sqlite3
│   ├── mysite/            # Project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   └── myweb/             # Django app
│       ├── __init__.py
│       ├── views.py
│       ├── urls.py
│       └── templates/
│           └── myweb/
│               ├── base.html
│               └── for.html

ไฟล์อื่นๆ (about.html, contact.html, index.html, for.html, mapage.html, mypage.html, myweb/) ที่อยู่นอก mysite/ ไม่จำเป็นสำหรับ Django และควรลบออกเพื่อความเป็นระเบียบ
