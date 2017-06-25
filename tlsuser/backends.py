from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from cryptography import x509
from cryptography.hazmat.backends import default_backend


class ClientTLSBackend(object):
    def authenticate(self, request):
        UserModel = get_user_model()
        translator = settings.TLSUSER_TRANSLATOR

        der = request.META.get("HTTPS_CLIENT_CERTIFICATE")
        if der is None:
            return None

        cert = x509.load_der_x509_certificate(der, default_backend())
        username = translator.get_username(cert)
        if username is None:
            return None

        is_admin = username in settings.ADMINS

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.is_staff = is_admin
            user.is_admin = is_admin
            user.is_superuser = is_admin
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
