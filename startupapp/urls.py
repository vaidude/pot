
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('contact/', views.contact_view, name='contact'),
    # path('virtual_furniture/',views.virtual_furniture,name='virtual_furniture'),
]