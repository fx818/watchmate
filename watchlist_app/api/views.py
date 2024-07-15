from rest_framework.response import Response
from watchlist_app.models import WatchList, StreamPlatform, Reviews
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewsSerializer
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
# Function based view moved to file named functionBasedViews


class WatchListListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
        
        
    def post(self, request):
        data = request.data
        serializer = WatchListSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class WatchDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk = pk)
        except WatchList.DoesNotExist:
            return Response({'error':'Movie not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        
        movie = WatchList.objects.get(pk = pk)
        serializer = WatchListSerializer(movie, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
class StreamPlatformAV(APIView):
    
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = StreamPlatformSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error':"data not valid"},serializer.errors)
    
class StreamDetailAv(APIView):
    def get(self, request, pk):
        try:
            data = StreamPlatform.objects.get(pk = pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Platform not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = StreamPlatformSerializer(data)
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk = pk)
        serializer = StreamPlatformSerializer(platform, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        data = StreamPlatform.objects.get(pk=pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ReviewsAV(APIView):
    
    def get(self, request):
        data = Reviews.objects.all()
        serializer = ReviewsSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = ReviewsSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'Error': 'Invalid data provided'})
        
class ReviewDetailAV(APIView):
    # watchlist = serializers.String
    def get(self, request, pk):
        try:
            data = Reviews.objects.get(pk = pk)
        except Reviews.DoesNotExist:
            return Response({'Error': 'Specified review does not exist'})
        serializer = ReviewsSerializer(data)
        return Response(serializer.data)

    def put(self, request, pk):
        data= Reviews.objects.get(pk = pk)
        serializer = ReviewsSerializer(data, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'Error': 'Invalid'})
    
    def delete(self, request, pk):
        review = Reviews.objects.get(pk = pk)
        review.delete()
        return Response({'Success':'Deleted'}, status = status.HTTP_204_NO_CONTENT)