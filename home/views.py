
from email import message
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render , redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from blog.models import Post
# Create your views here.
def home(request):
   return render(request , 'home/home.html')

def aboutus(request):
    return render(request , 'home/aboutus.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phoneNumber = request.POST['phoneNumber']
        City = request.POST['City']
        description = request.POST['description']
        if len(name)<3 or len(email)<4 or len(address)<5 or len(phoneNumber)<10 or len(City)<1:
            messages.error(request, "Please fill the form properly")
        else:
            contact = Contact(name=name,email=email,address=address,phoneNumber=phoneNumber,city=City,description=description)
            contact.save()
            messages.success(request,"Your form has been submitted")
        
    return render(request , 'home/contact.html')

def search(request):
    query = request.GET['search']
    if len(query)> 90:
        allPosts = Post.objects.none()
    else:
        
        allPostsTitle = Post.objects.filter(title__icontains = query)
        allPostsContent = Post.objects.filter(context__icontains = query)
        allPostsAuthor = Post.objects.filter(author__icontains = query)
        allPosts= allPostsTitle.union(allPostsContent,allPostsAuthor)
    if allPosts==0:
        messages.warning("No results found please refine your query")
    context = {'allPosts': allPosts , 'query': query}
    return render(request , 'home/search.html', context )

def handleSignup(request):
    if request.method == 'POST':
        Username = request.POST['Uname']
        fname = request.POST['fname']
        ltname =request.POST['ltname']
        email = request.POST['email']
        Pass1 = request.POST['Pass1']
        Pass2 = request.POST['Pass2']
        
        if len(Username)<10:
            messages.error(request, "Username must be of 10 characters")
            return redirect ('/')
        if not Username.isalnum():
            messages.error(request,"Username must contain letters and numbers" )
            return redirect ('/')
        if (Pass1 != Pass2):
            messages.error(request,"Password doea not match")
            return redirect('/')
            
        
        
        myuser = User.objects.create_user(Username, email, Pass1)
        myuser.first_name = fname
        myuser.last_name= ltname
        myuser.save()
        messages.success(request, "Your form has been submitted succesfully")
        return redirect('/')
    else:
        return HttpResponse("404 - Not Found")

def handleLogin(request):
    if request.method=='POST':
        loginUsername = request.POST['loginUsername']
        loginPassword = request.POST['loginPassword']
        
        user = authenticate(username= loginUsername , password= loginPassword)
        if user is not None:
            login(request ,user)
            messages.success(request, 'You have succesfully logged in')
            return redirect("/")
            
        else:
            messages.warning(request, 'Incorrect credentials')
            return redirect("/")
        
            
def handleLogout(request):
    logout(request)
    messages.success(request, "You have succesfully logged out")
    return redirect("/")
        