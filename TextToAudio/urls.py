from django.urls import path

from TextToAudio import views
# from .views import TextToSpeech


urlpatterns=[
    path("text",views.TextToSpeech.as_view(),name='text-to-speech')
]