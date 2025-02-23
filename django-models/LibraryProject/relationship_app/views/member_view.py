from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def check_member(user):
    return user.userprofile.role == 'MEMBER'

@user_passes_test(check_member)
def member_view(request):
    return render(request, 'member/dashboard.html', {
        'title': 'Member Dashboard'
    })