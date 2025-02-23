from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def role_required(role):
    def check_role(user):
        if not user.is_authenticated:
            return False
        return user.userprofile.role == role
    return user_passes_test(check_role, login_url='login')
