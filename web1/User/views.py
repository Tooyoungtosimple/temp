from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from User.models import User
from User.form import UserForm
from django.template import RequestContext
# Create your views here.
def UserInf(request,offset):
    a=User.objects.filter(id=offset)
    if a.exists():
        #b=a.get(id=offset)
        return render_to_response('user-inf.html', {'userlist':a})#{'id': b.id,'nickname':b.nickname,'phonenum':b.phonenum}
    else:
        return HttpResponse('not exist!')
def UserInf(request,offset=0):
    a=User.objects.all()
    return render_to_response('user-inf.html', {'userlist': a})




def Userload(request):
    if 'phone' in request.POST and 'passwords' in request.POST:
        temp_user=User(phonenum=request.POST['phone'],passwords=request.POST['passwords'])
        if request.POST['department']:
            temp_user.department=request.POST['department']
        if request.POST['nickname']:
            temp_user.nickname=request.POST['nickname']
        if request.POST['gender']=='1':
            temp_user.sex='男'
        else:
            temp_user.sex='女'
        temp_user.save()
        return 1
    else:
        return 0
def UserRegist(request):
    #old version
    if 'phone' in request.POST and 'passwords' in request.POST:
        p = User.objects.filter(phonenum=request.POST['phone'])
        if p.exists():
            return render_to_response('book-zhu.html', {'errorlog': 'exist'}, RequestContext(request))
        else:
            u = User(phonenum=request.POST['phone'], passwords=request.POST['passwords'], nickname=request.POST['nickname'])
            u.save()
            return render_to_response('book-zhu.html', {'errorlog': 'ok'}, RequestContext(request))

    else:
        return render_to_response('book-zhu.html', {'errorlog': 'error'}, RequestContext(request))

    #new version
    '''
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.save()
            return HttpResponseRedirect(reverse("book-index.html"))
        else:
            return render_to_response('book-zhu.html', {'errorlog': 'ok'}, RequestContext(request))
    else:
        form=UserForm()
        return render_to_response('formtest.html', {'form': form})
        '''
def UserLogin(request):
    return HttpResponse("userlogin")

def UserHomePage(request):
    if request.method=='POST':
        if 'account'in request.POST and 'passwords'in request.POST:
            objs=User.objects.filter(phonenum=request.POST['account'])
            if objs.exists():
                user=User.objects.get(phonenum=request.POST['account'])
                if user.passwords==request.POST['passwords']:
                    return render_to_response('book-index.html',{'mystate':'log','nickname':user.nickname}, RequestContext(request))
                else:
                    render_to_response('book-index.html', {'mystate': 'passwords error', 'nickname': '登录'},
                                       RequestContext(request))
            else:
                render_to_response('book-index.html', {'mystate': 'user unexist', 'nickname': '登录'}, RequestContext(request))
    return render_to_response('book-index.html',{'mystate':'unlog','nickname':'登录'}, RequestContext(request))

