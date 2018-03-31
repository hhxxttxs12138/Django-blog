# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article, Tag, Classification
import http.client
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

def blog_classification(request):
	if request.method == 'GET':
		cc = request.GET.get('c')
	try:
		blog_list = Article.objects.all()
	except:
		raise Http404
	post_list = []
# model.objects.filter: invalid literal for int() with base 10: 'hyh'
	for blog in blog_list:
		if str(blog.Classification) == cc :
			post_list.append(blog)
	return render(request,'classification.html',{'blog_list':post_list,'classification':cc})