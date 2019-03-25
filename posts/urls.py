from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:id>/edit/', views.edit, name="edit"),
    path('<int:id>/update/', views.update, name="update"),
    path('<int:id>/delete/', views.delete, name="delete"),

    path('<int:post_id>/comment/create', views.comment_create, name="comment_create"),
]
