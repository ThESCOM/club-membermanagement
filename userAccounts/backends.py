from userAccounts.models import AdminUser

class EmailAuthBackend(object):
    """
    custom authentication backend
    """

    def authenticate(self, email=None, password=None):
        """
        Authentication method
        """
        try:
            user = AdminUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except AdminUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = AdminUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except AdminUser.DoesNotExist:
            return None
