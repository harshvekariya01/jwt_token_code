
from django.urls import path
# from rest_framework_simplejwt import views as jwt_views

from users.views import * 
  
urlpatterns = [ 
    path('hello/', Home.as_view(), name ='hello'), 
    path('api/custom-login/', CustomLoginView.as_view(), name='custom_login'),
] 