from django.urls import path
from .views import SummarizeBlogView

urlpatterns = [
    path('summarize/', SummarizeBlogView.as_view(), name='summarize_blog'),
]
