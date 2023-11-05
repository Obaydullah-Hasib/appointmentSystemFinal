from django.contrib import admin
from django.urls import path,include
from . import views as v


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("",v.role_index,name="role_index"),
    path("user_role/",v.role_insert,name='role_insert')
]