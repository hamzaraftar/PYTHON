from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed 

def login_success(sender, request, user, **kwargs):
    print("-------------------------------------------")
    print("User logged in successfully.")
    print("sender:", sender)
    print("request:", request)
    print("user:", user)
    print("kwargs:", kwargs)

user_logged_in.connect(login_success,sender=User)