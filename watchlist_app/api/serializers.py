from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Reviews


# If we use foriegn key in our model we will need to make chnages in our serializers too

class ReviewsSerializer(serializers.ModelSerializer):
    
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Reviews
        exclude = ('watchlist',)
        # fields = "__all__"



class WatchListSerializer(serializers.ModelSerializer):
    
    reviews = ReviewsSerializer(many=True, read_only=True)
    
    class Meta:
        # create and update are automatically stored here
        model = WatchList
        fields = "__all__"
        

class StreamPlatformSerializer(serializers.ModelSerializer):
    # use the variable name you given in the model related_name = "-------"
    watchlist = WatchListSerializer(many=True, read_only = True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        
