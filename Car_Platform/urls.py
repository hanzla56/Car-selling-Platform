from django.contrib import admin
from django.urls import path
from . import views # added manually

app_name = "Car_Platform"  # addes manually good practice

urlpatterns = [
    path("admin/", admin.site.urls),
    path("" , views.home_page , name='home_page'),
    path("<int:ad_id>" , views.car_detail , name= 'detail_page'),
    path("new_ad/" , views.new_ad , name = 'new_ad'),

]


