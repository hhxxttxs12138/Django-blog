# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article, Tag, Classification
# Create your views here.

def blog_list(request):
	blogs = Article.objects.all().order_by('-publish_time')

	return render(request, 'index.html', {"blogs": blogs})

def blog_detail(request):
	if request.method == 'GET':
		id = request.GET.get('id','')
		id = str(id)
		try:
			blog = Article.objects.get(id=id)
		except Article.DoesNotExist:
			raise Http404

		return render(request, 'detail.html', {"blog": blog})
	else:
		raise Http404