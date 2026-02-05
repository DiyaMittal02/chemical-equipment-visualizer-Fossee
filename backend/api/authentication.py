from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    SessionAuthentication that exempts CSRF checks.
    Useful for hybrid apps accessing the API from different origins/clients.
    """
    def enforce_csrf(self, request):
        return  # To bypass CSRF check
