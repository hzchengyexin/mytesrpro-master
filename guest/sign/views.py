from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event
from sign.models import Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def index(request):
	return render(request,"index.html")

def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			response = HttpResponseRedirect('/event_manage/')
			#response.set_cookie('user',username,3600)
			request.session['user'] = username
			return response
		else:
			return render(request,'index.html',{'error':'username or password error!'})

@login_required
def event_manage(request):
	event_list = Event.objects.all()
	#username = request.COOKIES.get('user','')
	username = request.session.get('user','')
	return render(request,'event_manage.html',{'user':username,'events':event_list})

@login_required
def guest_manage(request):
	username = request.session.get('user','')
	guest_list = Guest.objects.all()
	paginator = Paginator(guest_list,2)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request,'guest_manage.html',{'user':username,'guests':contacts})


@login_required
def search_name(request):
	username = request.session.get('user','')
	search_name = request.GET.get("name","")
	event_list = Event.objects.filter(name__contains=search_name)
	return render(request,"event_manage.html",{"user":username,"events":event_list})

@login_required
def search_realname(request):
	username = request.session.get('user','')
	search_realname = request.GET.get("realname","")
	guest_list = Guest.objects.filter(realname__contains=search_realname)
	return render(request,"guest_manage.html",{"user":username,"guests":guest_list})

@login_required
def sign_index(request,eid):
	username = request.session.get('user','')
	event = get_object_or_404(Event,id=eid)
	guest_list = len(get_list_or_404(Guest,event_id=eid))
	guest_sign = len(get_list_or_404(Guest,event_id=eid,sign=1))
	return render(request,'sign_index.html',{"user":username,'event':event,'guest_list':guest_list,'guest_sign':guest_sign})

@login_required
def sign_index_action(request,eid):
	username = request.session.get('user','')
	event = get_object_or_404(Event,id=eid)
	guest_list = len(get_list_or_404(Guest,event_id=eid))
	guest_sign = len(get_list_or_404(Guest,event_id=eid,sign=1))
	phone = request.POST.get('phone','')
	# print(phone)
	result = Guest.objects.filter(phone=phone)
	if not result:
		return render(request,'sign_index.html',{"user":username,'event':event,'hint':'phone error.','guest_list':guest_list,'guest_sign':guest_sign})
	result = Guest.objects.filter(phone=phone,event_id=eid)
	if not result:
		return render(request,'sign_index.html',{"user":username,'event':event,'hint':'event id or phone error.','guest_list':guest_list,'guest_sign':guest_sign})
	result = Guest.objects.get(phone=phone,event_id=eid)
	if result.sign:
		return render(request,'sign_index.html',{"user":username,'event':event,'hint':'user has sign in','guest_list':guest_list,'guest_sign':guest_sign})
	else:
		Guest.objects.filter(phone=phone,event_id=eid).update(sign='1')
		guest_sign = guest_sign + 1
		return render(request,'sign_index.html',{"user":username,'event':event,'hint':'sign in success!','guest':result,'guest_list':guest_list,'guest_sign':guest_sign})

@login_required
def logout(request):
	auth.logout(request)
	response = HttpResponseRedirect('/index/')
	return response