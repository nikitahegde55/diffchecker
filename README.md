DiffChecker

DiffChecker is a Django-based web application that compares two text inputs and highlights the differences. It helps users visualize text modifications by marking added words in green and removed words in red.

🚀 Features
- Displays line numbers for both the original and changed text.
- Highlights added words in green and removed words in red for easy comparison.
- Built using Django (backend) and Bootstrap 5 (frontend) for a smooth UI experience.
- Allows users to copy the results easily.
- Includes an email feedback feature for users to send suggestions or report issues.

📥 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/nikitahegde55/diffchecker.git
cd diffchecker

2️⃣ Create a Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate      # For Windows
pip install -r requirements.txt

3️⃣ Run the Django Server
python manage.py runserver
Open http://127.0.0.1:8000/ in a browser.

📧 Email Feedback Feature
Users can submit feedback, and Django will send an email to the admin.
To configure email, update settings.py with SMTP settings:
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-email-password'

🌐 Deployment (Pending)
The project will be deployed on a Linode server soon.
A live demo link will be added once deployment is complete.


