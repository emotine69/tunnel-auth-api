# Import models.
from .models import Auth
from user.models import User
# Import rest_framework.
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

# Create your views here.

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self):
        return


