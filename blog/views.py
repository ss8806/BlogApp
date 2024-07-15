from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def index(request): #関数ベース
    #TOP画面を表示する関数
    # return render(request, 'index.html')
    return render(request, 'blog/index.html')  #変更箇所


class IndexView(TemplateView): #クラスベース
    #TOP画面を表示するクラス
    template_name = 'blog/index.html' 
