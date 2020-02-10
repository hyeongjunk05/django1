import json
from django.views import View
from django.http import JsonResponse
from .models import Comments


# from django.shortcuts import render

# Create your views here.

class Comment(View):
    def post(self, request):
        data = json.loads(request.body)
        Comments(
            email = data['email'],
            comment = data['comment']
        ).save()

        return JsonResponse({"코멘트":"성공"}, status=200)

