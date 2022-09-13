from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from re import template
from django.template import loader
from .models import AdmUser, Book

def index(request):
    books = Book.objects.all().values()
    if ('email' in request.session):
        context = {
            'session': request.session['email'],
            'book': books
        }
        return render(request,'records.html',context)
    context = {
        'book': books
    }
    template = loader.get_template('records.html')
    return HttpResponse(template.render(context,request))

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({},request))

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render({},request))

#Code to check the login credentials
def checklogin(request):
    #The Below Condition Checks If the email and pass Exists in Database if True session starts
    if AdmUser.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
        user = AdmUser.objects.filter(email=request.POST['email']).values()
        data = list(user)
        dict = data[0]
        request.session['email'] = dict['email']
        return HttpResponseRedirect(reverse('index'))
    return HttpResponseRedirect(reverse('index'))

#Code to logout the Admin and Delete session
def logout(request):
    request.session.delete()
    return HttpResponseRedirect(reverse('index'))


#Code to Signup The Admin USer
def checkregister(request):
    if request.method == "POST":
        adm = AdmUser()

        #the below Code checks if the email already exists
        if AdmUser.objects.filter(email=request.POST['email']).exists():
            return HttpResponseRedirect(reverse('index'))
        #if the email doesnt exist the info should added to database
        else:
            adm.email = request.POST['email']
            adm.password = request.POST['pass']
            cpass = request.POST['cpass']

            if adm.password != cpass:
                return redirect('register') 
            elif adm.email == "" or adm.password == "":
                return redirect('register')
            else:
                adm.save()
                return HttpResponseRedirect(reverse('index'))    
    else:
        template = loader.get_template('records.html')
        return HttpResponse(template.render())
    
def addrecord(request):
    if 'email' in request.session:
        template = loader.get_template('addrecord.html')
        return HttpResponse(template.render({},request))
    else:
        return HttpResponseRedirect(reverse('index'))

#Code to add Books entries
def checkentry(request):
    if 'email' in request.session:
        book = Book()
        book.bookTitle = request.POST['title']
        book.author = request.POST['author']
        book.publisher = request.POST['publisher']
        book.pages = request.POST['number']

        if book.bookTitle == "" or book.author == "" or book.publisher == "" or book.pages == "":
            return redirect('addrecord')
        else:
            book.save()
            return HttpResponseRedirect(reverse('index'))
    else :
        return HttpResponseRedirect(reverse('index'))


def update(request,id):
    book = Book.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'book': book,
    }
    return HttpResponse(template.render(context, request))


#Code to update Book entries
def updaterecord(request,id):
    book = Book.objects.get(id=id)
    title = request.POST['title']
    author = request.POST['author']
    publisher = request.POST['publisher']
    pages = request.POST['number']

    if title == "" or author == "" or publisher == "" or pages == "":
        return HttpResponseRedirect(reverse('index'))
    else:
        book.bookTitle = title
        book.author = author
        book.publisher = publisher
        book.pages = pages
        book.save()
        return HttpResponseRedirect(reverse('index'))


#code To delete the book entries
def delete(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return HttpResponseRedirect(reverse('index'))