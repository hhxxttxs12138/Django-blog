# coding:utf-8
from django.shortcuts import render
from blog.models import Article, Tag, Classification

def blog_list(request):
	blogs = Article.objects.all().order_by('-publish_time')

	return render(request, 'index.html', {"blogs": blogs})
# Create your views here.
