from django.http import JsonResponse


def api_home(request):
    return JsonResponse({
        "API": "Kanvas",
        "Description": "API para gerenciamento de cursos e aulas.",
        "Version": "1.0.0",
        "Documentation": "/api/docs/swagger-ui/",
        "Endpoints": {
            "Login": "/api/login/",
            "Accounts": "/api/accounts/",
            "Courses": "/api/courses/",
        }
    })
