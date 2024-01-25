from django.urls import path

from .views import BlogList, BlogDateDetailView, AboutPageView

urlpatterns = [
    path('', BlogList.as_view(), name='home'),
    path('post/<int:pk>/', BlogDateDetailView.as_view(), name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
]