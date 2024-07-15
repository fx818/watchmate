
from django.urls import path
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import WatchDetailAV, WatchListListAV, StreamPlatformAV, StreamDetailAv, ReviewsAV, ReviewDetailAV

urlpatterns = [
    path('list/', WatchListListAV.as_view(), name = 'movies-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name = 'movie-detail'),
    path('stream', StreamPlatformAV.as_view(), name = 'stream'),
    path('stream/<int:pk>', StreamDetailAv.as_view(), name = 'stream-detail'),
    path('reviews', ReviewsAV.as_view(), name = 'reviews'),
    path('reviews/<int:pk>', ReviewDetailAV.as_view(), name = 'reviewsDeatils'),
    
]

