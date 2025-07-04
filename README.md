# 🛡️ DevSecOps Portfolio Website

Welcome to my **DevSecOps Portfolio**, a personal website built using Django to showcase my skills, projects, and experience in DevSecOps, cloud infrastructure, CI/CD, Kubernetes, and secure application delivery.

![Python](https://img.shields.io/badge/Built_with-Django-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🚀 Live Demo

📌 _Coming soon: Hosted on AWS EC2 with Nginx and Gunicorn_  
(You can add your deployment link here)

---

## 🧰 Tech Stack

- **Backend:** Django (Python)
- **DevSecOps Tools:** SonarQube, OWASP ZAP, Jenkins
- **Container Orchestration:** Kubernetes
- **Infrastructure as Code:** Terraform
- **Cloud Hosting:** AWS (EC2, S3, IAM, RDS)
- **API Testing:** Postman
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```plaintext
portfolio_website/
├── manage.py
├── portfolio/   
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── admin.py
├── blog/  
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   │   ├── blog           
│   │   └── portfolio
├── media/
├── db.sqlite3
├── requirements.txt
└── README.md



---

## 🧑‍💻 Features

- ✅ Responsive landing page with personal intro
- ✅ Dynamic **projects** and **skills** from Django admin
- ✅ Clean, SEO-optimized Bootstrap UI
- ✅ "About Me" section with full DevSecOps stack
- ✅ Django Admin panel for managing content
- ✅ Ready for production deployment

---

## 🛠️ Local Setup

Follow these steps to run this project locally:

```bash
# 1. Clone the repo
git clone https://github.com/Sakshi9111/mywebsite.git
cd mywebsite

# 2. Create virtual environment
python3 -m venv portfolio_env
source portfolio_env/bin/activate

# 3. Install dependencies
pip3 install django pillow django-crispy-forms crispy-bootstrap5 django-ckeditor

# 4. Apply migrations and run server
python3 manage.py makemigrations portfolio
python3 manage.py makemigrations blog
python manage.py migrate
python manage.py createsuperuser  # create admin user
python manage.py runserver
