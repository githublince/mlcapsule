from django.shortcuts import render  #important user addition
from django.http import HttpResponse  #important user addition
from rest_framework import serializers
from django.core.paginator import Paginator

#important user addition
from .models import *
from django.template import loader
from django.http import Http404
import os, os.path
import math , json
import random, string
from django.http import JsonResponse
import re
import shutil


# Create your views here.

def this(request):
    return HttpResponse('This is home Page')

def privarcy(request):
    return HttpResponse('<h1 style="color: red">We respect privacy, so must you</h1> ')

def home(request):
# connecting to database

    customers=cpeoples.objects.all()                          
    template=loader.get_template('home/home.html')
    infos={
        'customers':customers,
    }

    return HttpResponse(template.render(infos,request))


def ulogin(request):

# check user integrity

                              
    template=loader.get_template('home/ulogin.html')
    infos={
        'customers':'ed',
    }

    return HttpResponse(template.render(infos,request))


def signup(request):
# connecting to database

    if request.method == 'POST': # login from signup page

        # error for if user already exist
        u= request.POST["email"]
        if(cpeoples.objects.filter(email=u).exists()==True):
            return HttpResponse('<h1 style="color: red">We respect privacy so shall you</h1> ')

        #save user
        newuser=cpeoples(fname=request.POST["first_name"],sname=request.POST["last_name"],email=request.POST["email"],password=request.POST["password"])
        newuser.save()


        #create a folder in the name of username
        while(True):
            try:
                x = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
                os.makedirs("home\\static\\userarticlePzUAUMAcUi3OoxWY\\"+x)
                break
            except FileExistsError:
                continue


        #register foldername in USERBOX model
        newbox=userbox(email=newuser,foldername="userarticlePzUAUMAcUi3OoxWY\\"+x)
        newbox.save()




        template=loader.get_template('home/login.html')
        infos={'customers':'customers',}
        return HttpResponse(template.render(infos,request))

    
                            
    template=loader.get_template('home/signup.html')
    infos={
        'customers':'customers',
    }

    return HttpResponse(template.render(infos,request))


def capdata(request):
# connecting to database

    customers=cpeoples.objects.all()                          
    template=loader.get_template('home/capdata.html')
    infos={
        'customers':customers,
    }

    return HttpResponse(template.render(infos,request))


def capsulein(request):

    if request.method == 'GET': 
        print(request.GET)
        article=user_work.objects.filter(id=request.GET["id"])
        jsonname=article[0].articlepath

        with open(jsonname, "r") as read_file:
            jdata = json.load(read_file)
        
        print(type(jdata))
        jdata = json.dumps(jdata)

        
        template=loader.get_template('home/capdata.html')
        infos={'jdata':jdata,}
        return HttpResponse(template.render(infos,request))


def capsule(request):


    try:
        print(request.GET)

        caps=capinitials.objects.filter(articename__contains=request.GET['search']).order_by('vote')

        paginator = Paginator(caps, 16)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        infos={'caps':page_obj,'tag':request.GET.get('search')}        

        template=loader.get_template('home/capsule.html')
        return HttpResponse(template.render(infos,request))

    except:
        pass
        


        
    
    caps=capinitials.objects.all().order_by('vote')
    paginator = Paginator(caps, 16)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    infos={
        'caps':page_obj,
    }        

    template=loader.get_template('home/capsule.html')
    return HttpResponse(template.render(infos,request))


def login(request):
    if request.method == 'GET': #login from anywhere 
        print(request.GET)
        template=loader.get_template('home/login.html')

        if("user" in list(request.GET.keys())):
            infos={'loginuser':request.GET["user"],}
        else:
            infos={'customers':"c",}

        return HttpResponse(template.render(infos,request))



    if request.method == 'POST': #login page 
        user=cpeoples.objects.filter(email=request.POST["email"])
        userworks=user_work.objects.filter(email=request.POST["email"])

        
        template=loader.get_template('home/loggeduser.html')

        infos={'user':user[0].getfname(),'email':user[0].getemail(),"userworks":userworks}

        return HttpResponse(template.render(infos,request))


    

def checkemail(request):
    u= request.POST.get('email', None)
    print(u)
    data = {
        'exist': cpeoples.objects.filter(email=u).exists()
    }

    return JsonResponse(data)

def checkuser(request):
    print(request.POST.get('email', None))
    print(request.POST.get('password', None))
  
    data = {
        'exist': cpeoples.objects.filter(email=request.POST.get('email', None),password=request.POST.get('password', None)).exists()
    }

    
    return JsonResponse(data)

def deletecapsule(request):
    if request.method == 'POST':

        work=user_work.objects.filter(id=request.POST["id"])
        artpath=work[0].articleimagespath.removesuffix("image").replace("\\\\","\\")
        jpath=work[0].articleimagespath.replace("\\\\","\\")
        shutil.rmtree(artpath)
        shutil.rmtree(jpath)

        
        user_work.objects.filter(id=request.POST["id"]).delete()


        user=cpeoples.objects.filter(email=request.POST["email"])
        userworks=user_work.objects.filter(email=request.POST["email"])

        
        template=loader.get_template('home/loggeduser.html')
        infos={'user':user[0].getfname(),'email':user[0].getemail(),"userworks":userworks}
        return HttpResponse(template.render(infos,request))



def addnewcapsule(request):
# connecting to database
    if request.method == 'GET':
        user=cpeoples.objects.filter(email=request.GET["email"])
                             
        template=loader.get_template('home/addnewarticles.html')
        infos={'user':user[0].getfname(),'email':user[0].getemail()}
        return HttpResponse(template.render(infos,request))

def editcapsule(request):
# connecting to database
    if request.method == 'POST':
        

        print(request.POST)
        # # Opening JSON file
        jsonfilepath=user_work.objects.filter(id=request.POST['id'])[0].articlepath.replace("\\\\","\\")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$",jsonfilepath)
        with open(jsonfilepath, "r") as read_file:
            jdata = json.load(read_file)
        
        print(type(jdata))
        #  returns JSON object as a dictionary

        jdata = json.dumps(jdata,indent=4)

        user=cpeoples.objects.filter(email=request.POST["email"])
                             
        template=loader.get_template('home/editcapsule.html')
        infos={'user':user[0].getfname(),'email':user[0].getemail(),'jdata':jdata,'id':request.POST['id']}
        return HttpResponse(template.render(infos,request))

def editusercapsule(request):

    if request.method == 'POST':
        print(type(request.POST))
        print(request.POST["id"])
        
        art=user_work.objects.filter(id=request.POST["id"])

        print(art[0].articlepath)

        print("##########",art[0].articlepath,"$$$$$$$$")
        os.remove(art[0].articlepath)

        imagelist=[]
        #Save images to Folder_image
        for key in request.FILES:
            if ('image'.upper() in key.upper()):
                img = request.FILES[key]
                unique = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                img_save_path =art[0].articleimagespath+"\\\\"+unique+key+request.FILES[key].name
                imagelist.append(img_save_path)
                with open(img_save_path, 'wb+') as f:
                    for chunk in img.chunks():
                        f.write(chunk)

        jsondict={}
        imagecount=0
        #Create Json file and save to ' Folder '
        for key in request.POST:
            
            if ('subtopic'.upper() in key.upper()):
                jsondict[key]=request.POST[key]
                print("subtopic")
            elif ('topic'.upper() in key.upper()):
                jsondict[key]=request.POST[key]
                print("topic")
            elif ('para'.upper() in key.upper()):
                jsondict[key]=request.POST[key]
                print("para")
            elif ('code'.upper() in key.upper()):
                jsondict[key]=request.POST[key]
            elif ('picture'.upper() in key.upper()):
                if(request.POST[key]=="pict"):
                    print("#####################################################")
                    jsondict[key.replace("picture","image")]=imagelist[imagecount].replace("\\\\","\\").replace("home\\","")
                    imagecount+=1
            elif ('resquepic'.upper() in key.upper()):
                jsondict["image"+key]=request.POST[key]          
            elif ('capsulename'.upper() in key.upper()):
                jsondict[key]=request.POST["capsulename"]
                print("capsulename")
            elif ('desc'.upper() in key.upper()):
                jsondict[key]=request.POST["desc"]
                print("desc")
        print(jsondict)
        jstr = json.dumps(jsondict, indent=4)
        print(jstr)

        

        with open(art[0].articlepath, "w") as outfile:
            outfile.write(jstr)

        user=cpeoples.objects.filter(email=request.POST["email"])
        userworks=user_work.objects.filter(email=request.POST["email"])

        
        template=loader.get_template('home/loggeduser.html')
        infos={'user':user[0].getfname(),'email':user[0].getemail(),"userworks":userworks}
        return HttpResponse(template.render(infos,request))


 

def addusercapsule(request):
    from os import listdir
    print("############################################################",os.listdir())
# connecting to database

    if request.method == 'POST': #login page
        print(request.POST)


        #Get folder path from userbox
        requestuserbox=userbox.objects.filter(email=request.POST["email"])
        print(requestuserbox[0].foldername)


        #Create two folders in above path 1.Folder 2.Folder_image
        while(True):
            try:
                x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                folder="home\\static\\"+requestuserbox[0].foldername.replace("\\","\\\\")+"\\"+x
                os.makedirs(folder)
                break
            except FileExistsError:
                continue

        while(True):
            try:
                folderimage=folder+"image"
                os.makedirs(folderimage)
                break
            except FileExistsError:
                continue

        
        imagelist=[]
        #Save images to Folder_image
        for key in request.FILES:
            if ('image'.upper() in key.upper()):
                img = request.FILES[key]
                unique = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                img_save_path =folderimage+"\\\\"+unique+key+request.FILES[key].name
                imagelist.append(img_save_path)
                with open(img_save_path, 'wb+') as f:
                    for chunk in img.chunks():
                        f.write(chunk)
        #print(imageexist,imagelist[0].replace("\\\\","\\").replace("\\","\\\\"))
        jsondict={}
        imagecount=0
        #Create Json file and save to ' Folder '
        for key in request.POST:
            
            if ('subtopic'.upper() in key.upper()):
                jsondict[key]=request.POST[key]
                print("subtopic")
            elif ('topic'.upper() in key.upper()):
                jsondict[key]=request.POST[key]
                print("topic")
            elif ('para'.upper() in key.upper()):
                jsondict[key]=request.POST[key]
                print("para")
            elif ('code'.upper() in key.upper()):
                jsondict[key]=request.POST[key]
            elif ('picture'.upper() in key.upper()):
                if(request.POST[key]=="pict"):
                    print("#####################################################")
                    jsondict[key.replace("picture","image")]=imagelist[imagecount].replace("\\\\","\\").replace("home\\","")
                    imagecount+=1
            elif ('capsulename'.upper() in key.upper()):
                jsondict[key]=request.POST["capsulename"]
                print("capsulename")
            elif ('desc'.upper() in key.upper()):
                jsondict[key]=request.POST["desc"]
                print("desc")
        print(jsondict)
        jstr = json.dumps(jsondict, indent=4)
        print(jstr)

        articlepath=folder+"\\"+x+".json"

        with open(articlepath, "w") as outfile:
            outfile.write(jstr)

        #Make Userwork Object
        userarticle=user_work(id=x,email=cpeoples(email=request.POST["email"]),articletopicname=request.POST["capsulename"],articlepath=articlepath,articleimagespath=folderimage)
        userarticle.save()
        #Make Capinitials object
        cap=capinitials(articleid=userarticle,fname=cpeoples.objects.filter(email=request.POST["email"])[0].getfname(),articename=request.POST["capsulename"])
        cap.save()


        user=cpeoples.objects.filter(email=request.POST["email"])
        userworks=user_work.objects.filter(email=request.POST["email"])

        
        template=loader.get_template('home/loggeduser.html')
        infos={'user':user[0].getfname(),'email':user[0].getemail(),"userworks":userworks}
        return HttpResponse(template.render(infos,request))


def topic(request):
# connecting to database

                            
    template=loader.get_template('home/topic.html')
    infos={
    }

    return HttpResponse(template.render(infos,request))




    








