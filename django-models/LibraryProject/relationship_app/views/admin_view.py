from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def check_admin(user):
    return user.userprofile.role == 'ADMIN'

@user_passes_test(check_admin)
def admin_view(request):
    return render(request, 'admin/dashboard.html', {
        'title': 'Admin Dashboard'
    })