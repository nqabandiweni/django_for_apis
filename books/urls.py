from django.urls import path
from . views import BookListView

urlpatterns=[
    #path for Book List View
    path('',BookListView.as_view(),name='home')
]