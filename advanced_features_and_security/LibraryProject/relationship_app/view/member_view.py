from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def is_member(user):
    return user.is_authenticated and user.userprofile.role == "Member"

@user_passes_test(is_member)
def member_dashboard(request):
    return HttpResponse("Welcome to the Member Dashboard")