from django.shortcuts import render

from .speechtotext import transcribe_audio
from .text_transcript import transc_ai
from .text_tospeech import text_tospeech

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .voice_record import start_recording, stop_recording

@csrf_exempt
def start_record(request):
    start_recording()
    return JsonResponse({'message': 'Recording started.'}, status=200)

@csrf_exempt
def stop_record(request):
    stop_recording()
    return JsonResponse({'message': 'Recording stopped and saved.'}, status=200)



class AddCandidateAPI(APIView):
    @csrf_exempt
    def post(self,request):

        transcript = transcribe_audio(request)

        language = "Hindi"
        result = transc_ai(transcript, language)
        print(result)

        text_tospeech(result)
        print('stored!')

        data={}
        data['orignal transcript'] = transcript
        data['translated transcript'] = result

        return Response(data, status=HTTP_200_OK)
