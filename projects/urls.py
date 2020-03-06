from django.urls import path
from . import views

urlpatterns = [
    # root URL to project_index
    path("", views.project_index, name="project_index"),
    # dynamically generate URLS with primary key 
    path("<int:pk>/", views.project_detail, name="project_detail"),
]