import json
from django.views import View
from django.http import JsonResponse
from .models import Account


# from django.shortcuts import render

# Create your views here.

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        Account(
            email = data['email'],
            password = data['password']
        ).save()

        return JsonResponse({'message':'회원가입 완료'}, status=200)


class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        if Account.objects.filter(email = data['email']).exists() :
            user = Account.objects.get(email = data['email'])
            if user.password == data['password'] :
                return JsonResponse({'message':f'{user.email} 로그인 성공!'}, status=200)
            else :
                return JsonResponse({'message':'비밀번호 틀림'},status = 200)

        return JsonResponse({'message':'없는 이메일'},status=200)