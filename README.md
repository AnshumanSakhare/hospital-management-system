#project structure :-

hospital-management-system/
│
├── hospital_management_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── patients/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── patients/
│   │       └── patient_list.html
│   ├── static/
│   │   └── patients/
│   └── migrations/
│
├── doctors/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── doctors/
│   │       └── doctor_list.html
│   ├── static/
│   │   └── doctors/
│   └── migrations/
│
├── appointments/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── appointments/
│   │       └── appointment_list.html
│   ├── static/
│   │   └── appointments/
│   └── migrations/
│
├── manage.py
└── README.md
