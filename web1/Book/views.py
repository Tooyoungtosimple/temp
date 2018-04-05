#coding=UTF-8
from django.shortcuts import render
from Book.models import Indent,Book
from User.models import User

from django.shortcuts import render_to_response
from django.http import HttpResponse
from Book.form import BookForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core.files.base import ContentFile
STATIC_ROOT='http://127.0.0.1:8000/static'

# Create your views here.
def BookHomePage(request):
    indentlist=Indent.objects.all()
    return render_to_response('book-dky.html',{'indentlist':indentlist})
    #return HttpResponse('bookhomepage')
def test(request):
    if request.method == 'POST':
        '''
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return HttpResponseRedirect(reverse("book-index.html"))
        else:
            print(form.errors)
            return render_to_response('book-zhu.html', {'errorlog': form.errors}, RequestContext(request))
        '''

        photo=request.FILES.get('image','')
        print(request.FILES)
        if 'sport' in request.POST:
            print('check on')
        else:
            print('check out')
        #print(request.POST['sport'])
        if 'image' in request.FILES:
            print('exist')
        if photo:
            print('run')
            file_content = ContentFile(photo.read())
            book = Book()
            book.img.save(photo.name,file_content)
            book.save()
            print('ok')
            return render_to_response('book-zhu.html', {'errorlog': 'ok'}, RequestContext(request))
        else:
            print('fail')
            return render_to_response('book-zhu.html', {'errorlog': 'fail'}, RequestContext(request))
    else:
        #form = BookForm()
        return render_to_response('formtest.html')

#@csrf_exempt
def showImg(request):
    books = Book.objects.all()
    for i in books:
        print(i.id)
    #return render(request, 'showimg.html', content)
    return  render_to_response('showimg.html',{'books':books})


def BookSub(request):
    if request.method=='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return HttpResponseRedirect(reverse("book-index.html"))
        else:
            print(form.errors)
            return HttpResponseRedirect(reverse("book-index.html"))
    else:
        form=BookForm()
        return render_to_response('booksub.html',{'form':form})

def IndentSub(request):
    return HttpResponse(
        'indent'
    )

def user_check(user,check):
    if User.objects.filter(phonenum=user).exists():
        obj=User.objects.get(phonenum=user)
        if obj.checkcode!=0 and obj.checkcode==int(check):
            return True
        else:
            return False
    else:
        return False

def BookDonate(request,user,check):
    if request.method=='POST':
        if user_check(user,check):
            userobj=User.objects.get(phonenum=user)
            i = Indent(seller=userobj)
            i.save()
            for book in Book.objects.all():
                if book.title in request.POST:
                    i.book.add(book)
            i.save()
            return HttpResponseRedirect(reverse("bookhome"))
        else:
            print('post check error')
            HttpResponse("身份验证错误，请重新登录")
    else:
        if user_check(user,check):
            books=Book.objects.all()
            return render_to_response('book-donate.html',
                                      {'static': STATIC_ROOT, 'books': books, 'linkurl': 'http://127.0.0.1:8000/book'})
        else:
            return HttpResponse("身份验证错误，请重新登录")
