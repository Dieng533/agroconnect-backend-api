from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "AgroConnect API is running 🚀"
    })

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('products.urls')),
]