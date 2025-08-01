# 🗓️ Booking System API (Django REST Framework)

A backend API system where users can set weekly availability and guests can book time slots without overlaps.

---

## 📌 Features

- Set weekly availability per user (e.g., Monday, 10 AM–12 PM)
- Book 15–60 minute slots as a guest
- Prevents overlapping bookings
- Swagger documentation included
- SQLite-based lightweight backend

---

## ⚙️ Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework (DRF)
- drf-yasg (Swagger UI)
- SQLite (default Django DB)

---

## 🚀 Getting Started

### Step 1: Clone the Repo
```bash
git clone https://github.com/yourusername/booking-system.git
cd booking-system
```

### Step 2: Set Up Virtual Environment
```bash
python -m venv env
env\Scripts\activate  # Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
# Or manually:
pip install django djangorestframework drf-yasg
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Run Server
```bash
python manage.py runserver
```

---

## 📬 API Endpoints

### Base URL: `http://127.0.0.1:8000/`

### 🔹 `/api/availabilities/`
- `POST` – Create availability
- `GET` – List all availabilities

```json
{
  "user": "John",
  "weekday": "Monday",
  "start_time": "10:00:00",
  "end_time": "12:00:00"
}
```

---

### 🔹 `/api/bookings/`
- `POST` – Create a booking
- `GET` – View bookings

```json
{
  "guest_name": "Alice",
  "date": "2025-08-04",
  "start_time": "10:15:00",
  "end_time": "10:45:00"
}
```

> ⛔ Overlapping bookings will be rejected with a validation error.

---

### 🔍 Swagger Docs

Visit: `http://127.0.0.1:8000/swagger/`  
You can test all endpoints from this interactive UI.

---

## 📂 Project Structure

```
booking_system/
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── booking_system/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

---

## 🙋‍♂️ Developer Notes

- You can extend it with authentication.
- Add filters by weekday/date for smarter booking logic.
- Frontend can be integrated using React, HTML, or any mobile stack.

---

## 🧑‍💻 Author

**Pankaj Bharti**  
🔗 [GitHub](https://github.com/Panku1080)  
🔗 [LinkedIn](https://linkedin.com/in/pankaj-bharti-47256b21a)


