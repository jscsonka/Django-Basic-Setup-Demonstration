from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('movie/<int:movie_id>', views.movie_by_id, name='book_by_id'),
]