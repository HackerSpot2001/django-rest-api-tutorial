from django.http import JsonResponse
def home_page(req):
    freids = [
        'helo',
        'i',
        'have',
        'manu'
    ]
    return JsonResponse(freids,safe=False)