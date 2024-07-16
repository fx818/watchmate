from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlatform, Reviews
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewsSerializer
from rest_framework.exceptions import ValidationError
# from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics, viewsets
from rest_framework.views import APIView
# Custom import
from watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# Function based view moved to file named functionBasedViews


class WatchListListAV(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


        
class WatchDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    
        
        
        
# Lets use viewset and router for the StreamPlatform

# class StreamPlatformVS(viewsets.ViewSet):
    
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(user)
#         return Response(serializer.data)

# Lets use ModelViewsets

class StreamPlatformMVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


# class StreamPlatformAV(generics.ListCreateAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
    
    
# class StreamDetailAv(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
    
     

    
# Now we will use concreate view classes
class ReviewList(generics.ListAPIView):
    # queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    
    # path('stream/<int:pk>/review', ReviewList.as_view(), name = 'reviews'),
    # customizing the querset for the above url
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Reviews.objects.filter(watchlist = pk)
    # Using watchlist as this is the related name in the model class
    # Using this you will only the reviews for a movie specified in the url
    
    
    

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewsSerializer
    
    
    def get_queryset(self):
        return Reviews.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        data = WatchList.objects.get(pk = pk)
        review_user = self.request.user
        review_queryset = Reviews.objects.filter(watchlist = data, review_user = review_user)
        
        if review_queryset.exists():
            raise ValidationError("You have already reviewed")
        
        
        if data.number_rating == 0:
            data.avg_rating = serializer.validated_data['rating']
        else:
            data.avg_rating = (data.avg_rating + serializer.validated_data['rating'])/2
        data.number_rating += 1
        data.save()
        
        serializer.save(watchlist = data, review_user = review_user)
    
    # We also need to override the serializer class, remove the watchlist field
    
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [ReviewUserOrReadOnly]
    
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer