from django.urls import path
from . import views
app_name = "blog"

urlpatterns = [
    path("", views.all_belog, name="all_belog"),
    path("<int:blog_id>", views.details, name="details")
]
