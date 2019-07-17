from django.shortcuts import render

def index(request):
	"""学习笔记的主页"""
	return render(request,'learning_log/index.html')
# Create your views here.
