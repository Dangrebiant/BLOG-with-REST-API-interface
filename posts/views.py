from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate, login, logout
from .forms import PostForm
from .models import Post

# Create your views here.
@login_required
def post_create(request):
	if not request.user.is_authenticated():
		return redirect("posts:list")


	form = PostForm(request.POST or None, request.FILES or None)
	context = {
	"form":form,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully created")
		return redirect(instance.get_absolute_url())

	else:
		return render(request, "post_form.html", context)




def post_detail(request, id=None):
	instance = get_object_or_404(Post, id = id)
	context = {
		"title":"Detail",
		"instance":instance,
	}
	return render(request, "post_detail.html", context)




def post_list(request):
	queryset_list = Post.objects.all()
	paginator = Paginator(queryset_list, 5) # Shows 5 posts per page
	page = request.GET.get('page')

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
	"object_list":queryset,
	"title":"List",}
			
	return render(request, "post_list.html", context)

@login_required	
def post_mylist(request):
	queryset_list = Post.objects.filter(user=request.user)
	paginator = Paginator(queryset_list, 5) # Shows 5 posts per page
	page = request.GET.get('page')

	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
	"object_list":queryset,
	"title":"List",}
			
	return render(request, "post_list.html", context)
	
		



def listing(request):
    contact_list = Contacts.objects.all()
 

@login_required
def post_update (request, id=None):
	instance = get_object_or_404(Post, id = id)
	form = PostForm(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "The post was modified")
		return redirect(instance.get_absolute_url())

	
	context = {
		"title": instance.title,
		"instance":instance,
		"form":form,
	}
	return render(request, "post_form.html", context)


@login_required		
def post_delete(request, id=None):
	instance = get_object_or_404(Post, id = id)
	instance.delete()
	messages.success(request, "The post was deleted")
	return redirect("posts:list")

	
	