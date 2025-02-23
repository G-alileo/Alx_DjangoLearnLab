from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def check_librarian(user):
    return user.userprofile.role == 'LIBRARIAN'

@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request, 'librarian/dashboard.html', {
        'title': 'Librarian Dashboard'
    })