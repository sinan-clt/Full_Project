import json
from myappp import serializers
from django.db import reset_queries
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from random import random
from django.http import HttpResponse
from . models import students, upload, userregister,doctors,upload,ajaxx                 #///to connect database with views////
from django.core.files.storage import FileSystemStorage
from myappp.serializers import user_api
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# Create your views here.
def test1(request):
    return HttpResponse ('<h1 align="center">hellloooo</h1>')
def test2(request):
    return render(request,'head.html')

user_list=[]                                          #///declare a global list////
def jinja(request):
    # print(request.method)                  #///to check its which method and on cmd prmpt print////
    if request.method=="POST":
        getuser=request.POST['user']        #///give a variable to store////
        getpass=request.POST['password']
        getdob=request.POST['dob']
        getplace=request.POST['places']
        # print(getuser)                          #///to check its printing on cmd ////
        user_dict={"userre":getuser,"passwrde":getpass,"dobrthe":getdob,"placee":getplace}               #///dictionary  to store datas by input////
        user_list.append(user_dict)                 #///append datas ////

        print(user_dict)
        print(user_list)

    return render(request,'jinja.html')

def displayusers(request):
    # for any in user_list:                        #///to check weather its working,printing//// 
        # print(any)                               #///to check its printing on cmd ////

    return render(request,'displayusers.html',{"us":user_list})



 #///database connection clss- dbconnection.html ////
def dbconnection(request):
    if request.method=="POST":
        fname=request.POST['f_name']
        lname=request.POST['l_name']
        age=request.POST['age']
        email=request.POST['email']
        gender=request.POST['gender']

        obj=userregister(firstname=fname,lastname=lname,age=age,email=email,gender=gender)    #///created an object  to store datas to database by input////
        print(obj.firstname,obj.lastname,obj.age,obj.email,obj.gender)

        obj.save()                                                               #///saved the object///
        return render(request,'dbconnection.html',{"message":"user saved"})         #//to display on html page ///
        
    return render(request,'dbconnection.html')


def text(request):
    if request.method=='POST':
        name=request.POST['fname']
        print(name)
        return render(request,'text.html',{"user":name})
    return render(request,'text.html')

# def text2(request):
#     name=request.GET['fname']
#     print(name)
#     return render(request,'text.html')  

def sample(request):
    if request.method=='POST':
        name=request.POST['fname']
        number=request.POST['number']
        date=request.POST['date']

        obj=students(firstname=name,contact=number,dob=date)
        obj.save()

        return redirect('display')
    return render(request,'sample.html')
    

def display(request):
    user=students.objects.all()
    return render(request,'display.html',{"users":user})

def todo(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        mobile=request.POST['mobile']
        department=request.POST['department']
        birth=request.POST['dob']
        gender=request.POST['gender']
        email=request.POST['email']

        doc_obj=doctors(firstname=firstname,lastname=lastname,mobile=mobile,department=department,dob=birth,gender=gender,email=email)
        doc_obj.save()
        
        return redirect('todo')

    doc_data=doctors.objects.all()
    return render(request,'todo.html',{"hospitals":doc_data})


def delete(request,id):
    doctors.objects.get(id=id).delete()
    return redirect('todo')


def viewdata(request,id):
    singleobj=doctors.objects.get(id=id)
    return render(request,'update.html',{"data":singleobj})

def update(request,id):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        mobile=request.POST['mobile']
        department=request.POST['department']
        birth=request.POST['dob']
        gender=request.POST['gender']
        email=request.POST['email']
        doctors.objects.filter(id=id).update(firstname=firstname,lastname=lastname,mobile=mobile,department=department,dob=birth,gender=gender,email=email)
      
        return redirect('todo')
    
  
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            login=doctors.objects.get(email=username)
            if login.email==username and str(login.mobile)==password:
                request.session['user_session']=login.id
                return redirect('user')
            else:
                return render(request,'login.html',{"message":"Invalid Username and Password"})
        except doctors.DoesNotExist:
            return render(request,'login.html',{"message":"Invalid Username and Password"})
        
    
    return render(request,'login.html')

def user(request):        
    user_data=request.session['user_session']
    profile=doctors.objects.get(id=user_data)
    
    return render(request,'user.html',{"user":profile})


def file(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        email=request.POST['email']
        file=request.FILES['file']
        # print(file.name)                                #//to print the name of the file that we uploaded//

        file_name=str(random())+file.name                           #// file upload//
        print(file_name)  
        
        obj=FileSystemStorage()
        obj.save(file_name,file)

        user=upload(name=name,contact=contact,email=email,image=file_name)
        user.save()
        return redirect('file')

    obj2=upload.objects.all()                            #//to display the datas on the database//
    return render(request,'file.html',{"data":obj2})


def ajax(request):
    return render(request,'ajax.html')

def add_ajax(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        email=request.POST['email']

        obj=ajaxx(name=name,contact=contact,email=email)
        obj.save()
        return JsonResponse({'message':'data inserted'})


def ajax2(request):
    return render(request,'ajax2.html')

def add_ajax2(request):
    name=request.POST['names']
    number=request.POST['mobile']
    email=request.POST['mail']

    obj2=ajaxx(name=name,contact=number,email=email)
    obj2.save()
    return JsonResponse({"message1":'data inserted succesfully :) '})

def viewajax(request):
    customers=ajaxx.objects.all()
    data=[{'id':x.id,'name':x.name,'contact':x.contact,'email':x.email } for x in customers]
    return JsonResponse({'result':data})

def delajax(request):
    delid=request.POST['cid']
    deletee=ajaxx.objects.get(id=delid).delete()
    return JsonResponse({'mssgg':'data deleted sucesfully'})

def viewajax2(request):
    users=ajaxx.objects.all()
    datas=[{'id':x.id,'name':x.name,'contact':x.contact,'email':x.email } for x in users]
    return JsonResponse({'valuess':datas})

def delajax2(request):
    delete_user=request.POST['uid']
    de=ajaxx.objects.get(id=delete_user).delete()
    return JsonResponse({'message':'data deleted sucesfully'})


    # /////API/////

@csrf_exempt
def select_data(request,id=0):
    if request.method=='GET':
        seldata=ajaxx.objects.all()
        serializerdata=user_api(seldata, many='True')
        return JsonResponse(serializerdata.data, safe=False)
    elif request.method=='POST':
        userdata=JSONParser().parse(request)
        serlzerdata=user_api(data=userdata)
        if serlzerdata.is_valid():
            serlzerdata.save()
            return JsonResponse('Data inserted succesfully', safe=False)
        return JsonResponse('An error occured', safe=False)
    elif request.method=='DELETE':
        deldatae=ajaxx.objects.get(id=id)
        deldatae.delete()
        print(id)
        return JsonResponse('data deleted' ,safe=False)
    elif request.method=='PUT':
        userdata=JSONParser().parse(request)
        user=ajaxx.objects.get(id=userdata['id'])
        serializerdata=user_api(user,userdata)
        if serializerdata.is_valid():
            serializerdata.save()
            return JsonResponse('Data updated succesfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)

 