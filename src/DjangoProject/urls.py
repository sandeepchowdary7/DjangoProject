"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import (
        person_detail,
        create_person,
        delete_person,
        update_person
    )

from .views import (
    home_page,
    about_us,
    contact_us
)

urlpatterns = [
    path('', home_page),
    path('about-us', about_us),
    path('contact-us', contact_us),
    path('admin/', admin.site.urls),
    path('blog/<int:person_id>', person_detail),
    path('blog/person', create_person),
    path('blog/delete/person/<int:person_id>', delete_person),
    path('blog/update/person/<int:person_id>', update_person)
]
