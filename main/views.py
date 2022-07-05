from django.shortcuts import render, redirect, get_object_or_404
from .models import profile
from .forms import profileForm, commentForm
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import webster
from django.urls import reverse, reverse_lazy
from .models import comment,User
from .models import Likepost
from django.http import HttpResponseRedirect


def opening(request):
    return render(request, 'opening.html')

@login_required(login_url='signin')
def homepage(request):
    pro = profile.objects.all()
    return render(request, 'WebsterBlog.html', {'pro':pro})

@login_required(login_url='signin')
def search_profile(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        prf = profile.objects.filter(Author__username__contains=searched)
     
        return render(request, 'search.html', {
        'searched':searched,
        'prf':prf
        })
    else:
        return render(request, 'search.html', {})       

@login_required(login_url='signin')
def WebsterBlog_detail(request, pk):
    com = comment.objects.all()
    prol = profile.objects.get(id=pk)
    context = {
        'com':com,
        'prol': prol,
        }
    return render(request, 'WebsterBlog_detail.html', context)



@login_required(login_url='signin')
def like_post(request,pk):
    username = request.user.username

    post = profile.objects.get(pk=pk)

    like_filter = Likepost.objects.filter(post_id=post.id, username=username).first()

    if like_filter == None:
        new_like = Likepost.objects.create(post_id=post.id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/')    


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is Taken')
                return redirect('signup')


            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is Taken')   
                return redirect('signup') 


            else:
                Author = User.objects.create_user(username=username, email=email, password=password)
                Author.save()
                return redirect('opening') 

        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')
        
    return render(request, 'signup.html')   

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        Author = auth.authenticate(username=username, password=password)
        if Author is not None:
            auth.login(request, Author)
            return redirect('/')

        else:
            messages.info(request, "Sorry!! Not Registered ") 
            return redirect('signin')  
    return render(request, 'signin.html')     

# Create your views here.
@login_required(login_url='signin')
def WebsterBlog_create(request):

    if request.method == 'POST':
        user = request.user
        image = request.FILES.get('image')
        Text = request.POST['Text']
        Detail = request.POST['Detail']
        pro = profile.objects.all()
        new_post = profile.objects.create(Author =User(pk=user.pk), image=image, Detail=Detail, Text=Text)
        new_post.save()
        return render(request,'WebsterBlog.html',{'pro':pro})
      
    else:
        return render(request, 'WebsterBlog_create.html')

@login_required(login_url='signin')
def about(request):
    return render(request, 'about.html')  


@login_required(login_url='signin')
def ScheduleApp(request):
       
    profile = webster.objects.all()

    if request.method == 'POST':
        profile = webster(
            title = request.POST['title']
        )
        profile.save()
        return redirect('ScheduleApp')

    return render(request, 'todo.html' ,{'profiles': profile}) 
    
@login_required(login_url='signin')
def delete(request, pk):
    pro = profile.objects.get(id=pk)
    pro.delete()
    return redirect('/')   


@login_required(login_url='signin')
def logout(request):
   auth.logout(request)
   return redirect('signin')
    

@login_required(login_url='signin')
def question(request):
    return render(request, 'question.html')   

@login_required(login_url='signin')
def confirmpage(request):
    return render(request, 'confirmpage.html')

@login_required(login_url='signin')
def commentView(request,pk):
    article = profile.objects.get(pk=pk)
    if request.POST:
        author_id = article.Author_id
        article_id = article.id
        print(author_id,article_id)
        commt = request.POST.get('comment')
        comm = comment(name=User.username, body=commt, post_id=article_id,)
        comm.save()
        return render(request,'WebsterBlog_detail.html',{'prol':article , 'article':article})
    return render(request,'WebsterBlog_detail.html',{'article':article})

@login_required(login_url='signin')
def delete(request, pk):
    webster = webster.objects.get(id=pk)
    webster.delete()
    return redirect('/')  

@login_required(login_url='signin')
def deletepost(request, pk):
    pro = profile.objects.get(pk=pk)
    pro.delete()
    return redirect('/') 



@login_required(login_url='signin')
def allsetting(request):
    return render(request, 'allsetting.html')

@login_required(login_url='signin')
def settings(request):
    return render(request, 'settings.html', {})  










# Create your views here.

