from django.urls import path
from .views import EbookAPIView, EbookDetails,RegisterUser,filterEbook


urlpatterns = [
    path('ebooks/',EbookAPIView.as_view()),
    path('register/',RegisterUser.as_view()),
    path('details/<int:id>/',EbookDetails.as_view()),
    path('filterEbook/',filterEbook.as_view()) 
]