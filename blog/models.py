# coding:utf-8
from django.db import models

# Create your models here.

class Tag(models.Model):
	tag_name = models.CharField(max_length=20)
	create_time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return tag_name

class Classification(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return name

class Author(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField(blank=True)
	website = models.URLField(blank=True)
	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=30)
	publish_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(Author,on_delete=models.CASCADE)
	Classification = models.ForeignKey(Classification,on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, blank=True)
	content = models.TextField()
	def __str__(self):
		return self.title
