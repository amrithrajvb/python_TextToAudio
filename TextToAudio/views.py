from django.http import FileResponse
from rest_framework.exceptions import APIException
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import TextSerializer
from gtts import gTTS
import io
from TextToAudio.serializers import TextSerializer
# Create your views here.

class TextToSpeech(APIView,APIException):
    serializer_class=TextSerializer

    status_code = 400
    default_detail = 'The text provided is too long.'
    default_code = 'text_too_long'

    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            text=serializer.validated_data['Text']
            if not text:
                return Response({'error': 'No text provided'}, status=400)
            if len(text) > 1000:
                raise TextToSpeech()
        else:
            return Response(serializer.errors)
            
        try:
             #taking and storing the audio
            TTS=gTTS(text=text,lang='en')
            audio_file=io.BytesIO()
            TTS.write_to_fp(audio_file)
            audio_file.seek(0)

            response=FileResponse(audio_file,content_type="audio/mp3",filename="output.mp3")
            return response

        except Exception as e:
            return Response({'error':str(e)},status=500)


