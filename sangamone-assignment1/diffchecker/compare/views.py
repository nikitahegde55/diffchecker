from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .utils import compare_texts  # Import the function

def compare_view(request):
    differences = []
    if request.method == "POST":  # Check if form is submitted
        text1 = request.POST.get("text1", "")  # Get first text
        text2 = request.POST.get("text2", "")  # Get second text
        differences = compare_texts(text1, text2)  # Call the function
    
    return render(request, "compare/compare.html", {"differences": differences})

from django.shortcuts import render

def home_view(request):
    return render(request, "compare/home.html")
  # Make sure "home.html" exists!



from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render

def feedback_view(request):
    if request.method == "POST":
        user_email = request.POST.get("email", "").strip()  # Get user's email
        feedback = request.POST.get("feedback", "").strip()  # Get feedback message

        if not user_email or not feedback:
            return HttpResponse("Both email and feedback are required!", status=400)

        # Email message format
        email_message = f"Sender: {user_email}\n\nFeedback:\n{feedback}"

        # Create an email with Reply-To option
        email = EmailMessage(
            subject="User Feedback",  # Email subject
            body=email_message,  # Email body with sender's email + message
            from_email="hegdenikita55@gmail.com",  # Your email (must match EMAIL_HOST_USER)
            to=["hegdenikita55@gmail.com"],  # Your email (recipient)
            reply_to=[user_email],  # This allows you to reply to the sender
        )

        email.send()  # Send the email
        return HttpResponse("Feedback sent successfully!")

    return render(request, "compare/feedback.html")  # 🔹 Correct path for the template



