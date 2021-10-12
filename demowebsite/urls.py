from pages.views import home_view,about_view,contact_view

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls'))

]
