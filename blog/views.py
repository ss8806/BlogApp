from django.shortcuts import render

# Create your views here.

def index(request):
    #TOP画面を表示する関数
    # return render(request, 'index.html')
    return render(request, 'blog/index.html')  #変更箇所