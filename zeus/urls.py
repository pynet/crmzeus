from django.contrib import admin
from django.urls import path

from zeus.core.views import home, report

urlpatterns = [
    path('', home, name='home'),
    path('report/', report, name='reports'),
    path('admin/', admin.site.urls),
]
