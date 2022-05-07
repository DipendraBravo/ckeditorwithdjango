from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.BlogCreate.as_view(), name="create_blog"),
    path('list/', views.BlogView.as_view(), name="view_blog"),

]