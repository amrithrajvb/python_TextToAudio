from rest_framework import serializers

class TextSerializer(serializers.Serializer):
    Text = serializers.CharField(required=True,max_length=1000)
