# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article, Tag, Classification
# Create your views here.

def article_content(request):
	return HttpResponse(Article.content)

def blog_list(request):
	blogs = Article.objects.all().order_by('-publish_time')

	return render(request, 'index.html', {"blogs": blogs})

