from django.http import HttpResponseForbidden

class AdminIPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        if request.path.startswith('/admin/'):
            # Verifique se o usuário é superusuário (além de staff)
            if not request.user.is_authenticated or not request.user.is_superuser:
                return HttpResponseForbidden("Acesso negado")
        return self.get_response(request)