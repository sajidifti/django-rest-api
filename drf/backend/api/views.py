from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    data = {"message": "Hello World"}
    return JsonResponse(data)
