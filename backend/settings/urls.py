from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('api/', include('financas.urls')),
    path('investimentos/', include('investimentos.urls')),
    path('bots/', include('bots.urls')),
]
