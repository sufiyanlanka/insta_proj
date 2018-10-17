
from insta import models
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import userprofile,userpost,postuploads
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def myview(request):
	username=request.user
	user=User.objects.get(username=username)
	followercount=userprofile.objects.filter(following=username).count()
	followingcount=userprofile.objects.filter(followers=username).count()
	profilepic=userpost.objects.filter(username=request.user)
	return render (request,"home.html",{"user":user,"followingcount":followingcount,"followercount":followercount,"profilepic":profilepic})

def users(request):
	if request.method=="POST":
		userdict=request.POST
		listuser=[x for x in userdict.values()]
		selected=User.objects.get(username=listuser[1])
		user=User.objects.get(username=request.user)
		if userprofile.objects.filter(followers=request.user,following=selected):
			followinglist=userprofile.objects.filter(followers=request.user,following=selected).delete()
			
		else:
			followinglist=userprofile.objects.get_or_create(followers=user,following=selected)
		return redirect("http://127.0.0.1:8000/accounts/profile/users")
	followinglist=userprofile.objects.filter(followers=request.user).values_list("following__username",flat=True)
	profilepic=userpost.objects.all().exclude(username=request.user)
	return render (request,"users.html",{"followinglist":followinglist,"profilepic":profilepic})
	
def friendsprofile(request,username):
	
	selecteduser=User.objects.get(username=username)
	followercount=userprofile.objects.filter(following=selecteduser).count()
	followingcount=userprofile.objects.filter(followers=selecteduser).count()
	profilepic=userpost.objects.filter(username=selecteduser)
	return render (request,"friendsprof.html",{"profilepic":profilepic,"selecteduser":selecteduser,"followingcount":followingcount,"followercount":followercount})

def followers(request):
	u=userprofile.objects.filter(following=request.user).values_list("followers__username",flat=True)
	if request.method=="POST":
		listuser=[x for x in request.POST.values()][1]
		selected=User.objects.get(username=listuser)
		if userprofile.objects.filter(followers=request.user,following=selected):
			followinglist=userprofile.objects.filter(followers=request.user,following=selected).delete()
		else:
			followinglist=userprofile.objects.get_or_create(followers=request.user,following=selected)
		return redirect("followers")
	b=userprofile.objects.filter(followers=request.user).values_list("following__username",flat=True)
	profilepic=userpost.objects.all().exclude(username=request.user)
	return render (request,"followers.html",{"u":u,"b":b,"profilepic":profilepic})

def following(request):
	if request.method=="POST":
		listuser=[x for x in request.POST.values()][1]
		selected=User.objects.get(username=listuser)
		followinglist=userprofile.objects.filter(followers=request.user,following=selected).delete()
	profilepic=userpost.objects.all().exclude(username=request.user)
	followinglist=userprofile.objects.filter(followers=request.user).values_list("following__username",flat=True)
	return render (request,"following.html",{"followinglist":followinglist,"profilepic":profilepic})

def friendsfollowers(request,username):
	if request.method=="POST":
		listuser=[x for x in request.POST.values()][1]
		selected=User.objects.get(username=listuser)
		if userprofile.objects.filter(followers=request.user,following=selected):
			followinglist=userprofile.objects.filter(followers=request.user,following=selected).delete()
		else:
			followinglist=userprofile.objects.get_or_create(followers=request.user,following=selected)

	use=User.objects.filter(username=request.user).values_list("username",flat=True)
	selecteduser=User.objects.get(username=username)
	profilepic=userpost.objects.all()
	u=userprofile.objects.filter(followers=request.user).exclude(following=request.user).values_list("following__username",flat=True)
	friendsfollowerlist=userprofile.objects.filter(following=selecteduser).values_list("followers__username",flat=True)
	return render (request,"friendsfollowers.html",{"use":use,"u":u,"friendsfollowerlist":friendsfollowerlist,"profilepic":profilepic})

def friendsfollowing(request,username):
	selecteduser=User.objects.get(username=username)
	followinglist=userprofile.objects.filter(followers=selecteduser).values_list("following__username",flat=True)
	return render (request,"friendsfollowing.html",{"followinglist":followinglist})


def uploads(request):
	if request.method=="POST":
		listuser=[x for x in request.POST.values()][1]
		selected=User.objects.get(username=listuser)
		likeslist=postuploads.objects.get_orcreate(username=request.user,likes=selected)
	

	post=postuploads.objects.all()
	u=userprofile.objects.filter(followers=request.user).values_list("following__username",flat=True)
	return render (request,"posthome.html",{"u":u,"post":post})