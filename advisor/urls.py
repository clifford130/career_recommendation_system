# from django.urls import path
# from . import views

# urlpatterns = [
#     # Add your app's URL patterns here later
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.career_recommendation, name='career_recommendation'),
]
