
from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import WatchDetailAV, WatchListListAV, StreamPlatformMVS, ReviewList, ReviewCreate ,ReviewDetail

from rest_framework.routers import DefaultRouter 
router = DefaultRouter()
router.register('stream', StreamPlatformMVS, basename='streamplatform')

urlpatterns = [
    
    path('list/', WatchListListAV.as_view(), name = 'movies-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name = 'movie-detail'),
    

    # Router for the url
    path('', include(router.urls)),
    
    # path('stream', StreamPlatformAV.as_view(), name = 'stream'),
    # path('stream/<int:pk>', StreamDetailAv.as_view(), name = 'stream-detail'),
    
    
    path('stream/<int:pk>/review/', ReviewList.as_view(), name = 'reviews'),
    
    # Making a new url for post req to create a review for a watchlist without passing the watchlist
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name = 'reviews'),
    
    path('review/stream/<int:pk>', ReviewDetail.as_view(), name = 'reviewsDeatils'),
    
]

