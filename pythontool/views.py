from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth.models import User
from django.http import HttpRequest,HttpResponse
from django.template import loader
from models import Book
from django.db import connection

# Create your views here.
def hello(request,a):
    print(a)
    print(isinstance(request,HttpRequest))
    print(request.path)
    print(request.method)
    print(request.GET.get('key'))

    user_list = User.objects.all()  #orm  sql查询
    print(user_list.query)
    # return render(request,'table.html',{'user_list':user_list})
    # return render_to_response('table.html',{'user_list':user_list})
    print(locals())
    return render_to_response('table.html',locals())

def hello1(request):
    response = HttpResponse("here is the text of the Web page",mimetype="text/plain")
    return response

def hello2(request):
    t = loader.get_template('table.html')
    c = {'foo':'bar'}
    return HttpResponse(t.render(c,request),content_type="text/html")

def hello3(request):
    redirect('http://www.baidu.com')

def sql(request):
    # Book.objects.filter(id=1).delete()
    # Book.objects.filter(title='bbcc').values('publisher') 关联查询
    # Book.objects.filter(title='bbcc').values('publisher__name') 关联查询
    # Book.objects.filter(author__name='bbb') 关联查询
    # Book.objects.filter(publisher__name='bbb').extra(where=['price>50']) sql查询 结果集修改器
    # Book.objects.filter(publisher__name='bbb',price_gt=50) 修改sql查询
    # Book.objects.extra(select={'count':'select count(*) from hello_book'}) sql查询 结果集修改器
    # Book.objects.extra(select={'count':'select count(*) from hello_book'}) sql查询 结果集修改器
    # Book.objects.raw('select * from hello_book');  原生sql

    cursor = connection.cursor()  #获得一个游标对象
    cursor.execute("insert into hello_author(name) values('ccc')") #插入操作
    cursor.execute("select * from hello_author")
    #raw = cursor.fetchone()  #返回结果行
    cursor.fetchall() 

    redirect('http://www.baidu.com')
