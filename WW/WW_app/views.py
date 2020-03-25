from django.shortcuts import render
from .models import *

from django.core.mail import send_mail
from random import randint

from datetime import datetime, timedelta, timezone
from django import template
from django.utils.timesince import timesince
# Create your views here.

def logic_index(request):
    uid=User.objects.get(email=request.session['email'])
    
    if uid.role=="freelancer":
        fid=Freelancer.objects.get(user_id=uid)
        frole="F"
        data=Post_Job.objects.all().prefetch_related('user_id')

        context={
            "uid":uid,
            "session_id":fid,
            "data":data,
            "frole":frole,
        }     
        #print("-------------------------->",context.session_id.profile_pic.url)
    else:
        cid=Company.objects.get(user_id=uid)
        crole="C"
        data=Post_Project.objects.all().prefetch_related('user_id')
        
        context={
            "uid":uid,
            "session_id":cid,
            "data":data,
            "crole":crole,
        }
    

    return {'context':context}

def home(request):
    if "email" not in request.session:
        return render(request,"WW_app/sign-in.html")
    else:
        return render(request,"WW_app/Base_index.html",logic_index(request))

def fpwd(request):
    return render(request,"WW_app/fpwd.html")

def sendotp(request):
    if "email" in request.POST:
        email=request.POST['email']

        uid=User.objects.get(email=email)
        if uid:
            otp=randint(1111,9999)
            uid.otp=otp
            uid.save()
            e_subject="Password reset otp"
            msg=str(otp)
            send_mail(e_subject,msg,"anjali.20.learn@gmail.com",[email])
            return render(request,"WW_app/otp.html",{'email':email})
        else:
            e_msg="user does not exist"
            return render(request,"WW_app/fpwd.html",{'e_msg':e_msg})
    else:
        e_msg="user does not exist"
        return render(request,"WW_app/fpwd.html",{'e_msg':e_msg})

def reset_password(request):
    email=request.POST['email']
    otp=request.POST['otp']
    newpass=request.POST['new_pwd1']
    repass=request.POST['new_pwd2']

    uid=User.objects.get(email=email)
    
    if str(uid.otp)==str(otp) and newpass==repass:
        uid.password=newpass
        uid.save()
        s_msg="successfully password changed"
        return render(request,"WW_app/sign-in.html",{'s_msg':s_msg})
    else:
        e_msg="invalid otp or password"
        return render(request,"WW_app/fpwd.html",{'e_msg':e_msg})

    

def index(request):
    if "email" not in request.session:
        return render(request,"WW_app/sign-in.html")
    else:
        return render(request,"WW_app/Base_index.html",logic_index(request))

def signup(request):
    role=request.POST['role']
    name=request.POST['name']
    country=request.POST['country']
    email=request.POST['email']
    phone=request.POST['phone']
    pwd=request.POST['pwd']
    r_pwd=request.POST['r_pwd']
    
    if pwd==r_pwd:
        uid=User.objects.create(email=email,password=pwd,country=country,phone=phone,role=role)
        if role=="freelancer":    
            fid=Freelancer.objects.create(user_id=uid,name=name)
        
        if role=="company":
            cid=Company.objects.create(user_id=uid,name=name)
        s_msg="Account Created Successfully!"
        e_subject="workwise : Confirmation mail"
        send_mail(e_subject,s_msg,"anjali.20.learn@gmail.com",[email])
        return render(request,"WW_app/sign-in.html",{'s_msg':s_msg})
    else:
        e_msg="OOPS!! Passwords did not match."
        return render(request,"WW_app/sign-in.html",{'e_msg':e_msg})

def login(request):
    if "email" not in request.session:
        try:
            email=request.POST['email']
            pwd=request.POST['pwd']
            """
            if "remember" in request.POST:
                request.session['r_email']=email
                request.session['r_password']=pwd
                print("---------------------->",request.session.r_email)
            """
            uid=User.objects.get(email=email)
            if uid:
                if uid.password==pwd:
                    request.session['id']=uid.id
                    request.session['email']=uid.email
                    request.session['role']=uid.role
                    if uid.role=="freelancer":
                        fid=Freelancer.objects.get(user_id=uid)
                        request.session['username']=fid.name.split()[0]
                        frole="freelancer"
                        data=Post_Job.objects.all().prefetch_related('user_id')
                        context={
                            'session_id':fid,
                            'uid':uid,
                            'frole':frole,  
                            'data':data,
                            }
                        return render(request,"WW_app/Base_index.html",{'context':context})
                    else:
                        cid=Company.objects.get(user_id=uid)
                        request.session['username']=cid.name.split()[0]
                        crole="company"
                        data=Post_Project.objects.all().prefetch_related('user_id')
                        context={
                            'session_id':cid,
                            'uid':uid,
                            'crole':crole,
                            'data':data,
                            }
                        return render(request,"WW_app/Base_index.html",{'context':context})
                else:
                    e_msg="Invalid Username or Password."
                    return render(request,"WW_app/sign-in.html",{'e_msg':e_msg})
            else:
                return render(request,"WW_app/Base_index.html")
        except:
            e_msg="User does not exist"
            return render(request,"WW_app/sign-in.html",{'e_msg':e_msg})

    else:
        return render(request,"WW_app/Base_index.html",logic_index(request))

def post_project(request):
    project_title=request.POST['project_title']
    project_country=request.POST['project_country']
    project_skills=request.POST['project_skills']
    project_initial_price=request.POST['project_initial_price']
    project_final_price=request.POST['project_final_price']
    project_description=request.POST['project_description']

    uid=User.objects.get(id=request.session['id'])
    fid=Freelancer.objects.get(user_id=uid.id)
    
    try:
        uid=Post_Project.objects.create(project_title=project_title,freelancer_id=fid,project_country=project_country,project_description=project_description,project_final_price=project_final_price,project_initial_price=project_initial_price,project_skills=project_skills,user_id=uid)
        s_msg="Project Posted Successfully!"
        return render(request,"WW_app/Base_index.html",{'s_msg':s_msg})
    except:
        e_msg="Please enter all details!"
        return render(request,"WW_app/Base_index.html",{'e_msg':e_msg})

def post_job(request):
    job_title=request.POST['job_title']
    job_country=request.POST['job_country']
    job_skills=request.POST['job_skills']
    job_price=request.POST['job_price']
    job_type=request.POST['job_type']
    job_description=request.POST['job_description']

    uid=User.objects.get(id=request.session['id'])
    cid=Company.objects.get(user_id=uid.id)


    try:
        uid=Post_Job.objects.create(job_title=job_title,company_id=cid,job_country=job_country,job_description=job_description,job_type=job_type,job_price=job_price,job_skills=job_skills,user_id=uid)
        s_msg="Job Posted Successfully!"
        return render(request,"WW_app/Base_index.html",{'s_msg':s_msg})
    except:
        e_msg="Please enter all details!"
        return render(request,"WW_app/Base_index.html",{'e_msg':e_msg})


def my_profile(request):
    if "email" not in request.session:
        return render(request,"WW_app/sign-in.html")
    else:
        return render(request,"WW_app/my-profile.html",logic_index(request))



def company_profile(request,pk=None):
    if "email" not in request.session:
        return render(request,"WW_app/sign-in.html")
    else:
        print("------------------->pk ",pk)
        pid=Post_Job.objects.get(id=pk)
        print("------------------>",pid.job_title)

        uid=pid.user_id
        cid=pid.company_id

        print("------------->com id ",cid.id)
        print("------------->com id ",cid.name)
        
        #cid=Company.objects.get(user_id=uid)
        print("--->>>",cid)
        context={
            'uid':uid,
            'cid':cid,
        }
        return render(request,"WW_app/company-profile.html",{'context':context})

def company_details(request,pk=None):
    cid=Company.objects.get(id=pk)
    context={
            'cid':cid,
    }
    return render(request,"WW_app/company-profile.html",{'context':context})

def freelancer_details(request,pk=None):
    f_data=Freelancer.objects.get(id=pk)
    popup_name=f_data.name
    clicked="yes"
    chat_send=Chat_send.objects.all().prefetch_related('sender')
    context={
            'f_data':f_data,
            'popup_name':popup_name,
            'clicked':clicked,
    }
    return render(request,"WW_app/profiles.html",{'context':context})

def profiles(request):
    if "email" not in request.session:
        return render(request,"WW_app/sign-in.html")
    else:
        uid=User.objects.get(email=request.session['email'])
        f_data=Freelancer.objects.all().prefetch_related('user_id')
        context={
            'f_data':f_data,
            'uid':uid,

        }
        return render(request,"WW_app/profiles.html",{'context':context})

def follow(request):
    if 'email' not in request.session:
        return render(request,"WW_app/sign-in.html")
    else:
        email1=request.POST['email1']
        email2=request.POST['email2']
        uid1=User.objects.get(email=email1)
        uid2=User.objects.get(email=email2)
        uid=uid2

        followers=uid2.followers
        uid2.followers=followers+1
        uid2.save()
        following=uid1.following
        uid1.following=following+1
        uid1.save()
        s_msg="Following! "
        

        cid=Company.objects.get(user_id=uid2)
        context={
            'cid':cid,
            'uid':uid,
        }
        return render(request,"WW_app/company-profile.html",{'context':context})


def age(value):
    now = datetime.now()
    try:
        difference = now - value
        print("------------>",difference,"=",now,"-",value)
    except:
        return value

    if difference <= timedelta(minutes=1):
        return 'just now'
    return '%(time)s ago' % {'time': timesince(value).split(', ')[0]}


def forum(request):
    uid=User.objects.get(id=request.session['id'])
    fid=Freelancer.objects.get(user_id=uid)
    data=Forum_Q.objects.all().prefetch_related('user_id')
    now = datetime.now(timezone.utc)
    for i in reversed(data):
        difference = now - i.created_at
        if difference <= timedelta(minutes=1):
            i.timediff="Just now"
        else:
            i.timediff='%(time)s ago' % {'time': timesince(i.created_at).split(', ')[0]} 


    context={
        "uid":uid,
        "session_id":fid,
        "data":data,
    }     
    
    return render(request,"WW_app/forum.html",{'context':context})

def add_question(request):
    question=request.POST['question']
    tags=request.POST['tags']
    description=request.POST['description']
    uid=User.objects.get(id=request.session['id'])
    fid=Freelancer.objects.get(user_id=uid.id)
    data=Forum_Q.objects.all().prefetch_related('user_id')
    now = datetime.now(timezone.utc)
    for i in reversed(data):
        difference = now - i.created_at
        if difference <= timedelta(minutes=1):
            i.timediff="Just now"
        else:
            i.timediff='%(time)s ago' % {'time': timesince(i.created_at).split(', ')[0]} 
    try:
        forum_id=Forum_Q.objects.create(question=question,tags=tags,description=description,user_id=uid,f_id=fid)
        s_msg="Question Posted on Forum"
        context={
            "uid":uid,
            "session_id":fid,
            "data":data,
            's_msg':s_msg
        }     
        return render(request,"WW_app/forum.html",{'context':context})
    except:
        e_msg="Please enter all details!"
        context={
            "uid":uid,
            "session_id":fid,
            "data":data,
            'e_msg':e_msg
        }     
        return render(request,"WW_app/forum.html",{'context':context})

def companies(request):
    if "email" not in request.session:
        return render(request,"WW_app/sign-in.html")
    else:
        uid=User.objects.get(email=request.session['email'])
        c_data=Company.objects.all().prefetch_related('user_id')
        context={
            'c_data':c_data,
            'uid':uid,

        }
        return render(request,"WW_app/companies.html",{'context':context})

def messages(request,pk=None):
    if pk==0:
        return render(request,"WW_app/messages.html")
    else:
        fid=Freelancer.objects.get(id=pk)
        uid=fid.user_id
        session_id=Freelancer.objects.get(user_id=request.session['id'])
        context={
                'fid':fid,
                'uid':uid,
                'session_id':session_id
            }
        return render(request,"WW_app/messages.html",{'context':context})


def logout(request):
    if "email" in request.session:
        del request.session['username']
        del request.session['email']
        del request.session['id']
        del request.session['role']
        return render(request,"WW_app/sign-in.html")
    else:
        return render(request,"WW_app/sign-in.html")

def update_dp(request):
    email=request.POST['email']
    dp=request.FILES['dp']
    uid=User.objects.get(email=email)
    
    if uid.role=="freelancer":
        fid=Freelancer.objects.get(user_id=uid)
        fid.profile_pic=dp
        fid.save()
        return render(request,"WW_app/Base_index.html",logic_index(request))
    else:
        cid=Company.objects.get(user_id=uid)
        cid.profile_pic=dp
        cid.save()
        return render(request,"WW_app/Base_index.html",logic_index(request))
