from django.db import models

# Create your models here.

class User(models.Model):
    email=models.EmailField(max_length=30,unique=True)

    password=models.CharField(max_length=30,blank=False)
    otp = models.IntegerField(default = 686)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    country = models.CharField(max_length = 30,blank=True)
    phone = models.IntegerField(blank=False)
    overview=models.CharField(max_length=300,blank=True)
    role=models.CharField(max_length=20,blank=False)

    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    following = models.IntegerField(default=0,blank=True)
    followers = models.IntegerField(default=0,blank=True)

class Freelancer(models.Model):
    user_id=models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=30,blank=False)
    profile_pic=models.FileField(upload_to='WW_app/images/',default='images/mypic.png')

class Company(models.Model):
    user_id=models.ForeignKey(User, on_delete = models.CASCADE)

    name = models.CharField(max_length=30,blank=False)
    address = models.CharField(max_length=300,blank=True)
    website = models.CharField(max_length=30,blank=True)
    profile_pic=models.FileField(upload_to='WW_app/images/',default='images/mypic.png')

    year_est=models.IntegerField(default=2000)
    employees=models.IntegerField(default=1)
    ratings = models.CharField(max_length=30,blank=True)

class Chat_send(models.Model):
    sender=models.ForeignKey(User, on_delete = models.CASCADE)
    sf_id=models.ForeignKey(Freelancer, on_delete = models.CASCADE)
    message=models.CharField(max_length=300,blank=False)
    created_at= models.DateTimeField(auto_now_add=True)
    timediff=models.CharField(blank=True, max_length=30)

class Chat_recieve(models.Model):
    reciever=models.ForeignKey(User, on_delete = models.CASCADE)
    rf_id=models.ForeignKey(Freelancer, on_delete = models.CASCADE)
    chat_id=models.ForeignKey(Chat_send, on_delete = models.CASCADE)


"""
class Reviews(models.Model):
    user_id=models.ForeignKey(User, on_delete = models.CASCADE)
    company_id=models.ForeignKey(Company,on_delete=models.CASCADE)
    review=models.CharField(max_length=300,blank=False)

"""
class Forum_Q(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    f_id=models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    
    question=models.CharField(max_length=90,blank=False)
    tags=models.CharField(max_length=100,blank=False)
    description=models.CharField(max_length=500,blank=False)
    created_at= models.DateTimeField(auto_now_add=True)
    timediff=models.CharField(blank=True, max_length=30)

class Post_Job(models.Model):
    user_id=models.ForeignKey(User, on_delete = models.CASCADE)  
    company_id=models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title=models.CharField(max_length=50,blank=False)   # Developer/Content Writer/Photographer etc.  """
    job_country=models.CharField(max_length=30,blank=False)
    job_skills=models.CharField(max_length=150,blank=False) # pHp/Java/Node.JS etc.
    job_price=models.IntegerField(blank=False)    # Expected Pay per hour (ex. 15$/hr) """
    job_type=models.CharField(max_length=20,blank=False)    # Part Time/Full Time/ Internship etc."""   
    job_description=models.CharField(max_length=500,blank=False)    # Brief description of Job"""

    t_likes=models.IntegerField(default=0)
    t_comments=models.IntegerField(default=0)
    t_views=models.IntegerField(default=0)

class Post_Project(models.Model):
    user_id=models.ForeignKey(User, on_delete = models.CASCADE)    
    freelancer_id=models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    project_title=models.CharField(max_length=50,blank=False)   # Developer/Content Writer/Photographer etc.  """
    project_country=models.CharField(max_length=30,blank=False)
    project_skills=models.CharField(max_length=150,blank=False) # pHp/Java/Node.JS etc.
    project_initial_price=models.IntegerField(blank=False)    # Expected Pay per hour (ex. 15$/hr) """
    project_final_price=models.IntegerField(blank=False)    # Expected Pay per hour (ex. 15$/hr) """
    project_description=models.CharField(max_length=500,blank=False)    # Brief description of Job"""

    t_likes=models.IntegerField(default=0)
    t_comments=models.IntegerField(default=0)
    t_views=models.IntegerField(default=0)


class Likes(models.Model):
    user_id=models.ForeignKey(User, on_delete = models.CASCADE)
    post_job_id=models.ForeignKey(Post_Job, on_delete = models.CASCADE)
    post_project_id=models.ForeignKey(Post_Project, on_delete = models.CASCADE)


class Comments(models.Model):
    user_id=models.ForeignKey(User, on_delete = models.CASCADE)
    comment=models.CharField(max_length=135,blank=False)
    post_job_id=models.ForeignKey(Post_Job, on_delete = models.CASCADE)
    post_project_id=models.ForeignKey(Post_Project, on_delete = models.CASCADE)
    

class Views(models.Model):
    user_id=models.ForeignKey(User, on_delete = models.CASCADE)
    post_job_id=models.ForeignKey(Post_Job, on_delete = models.CASCADE)
    post_project_id=models.ForeignKey(Post_Project, on_delete = models.CASCADE)
    

"""
class User(models.Model):
    
    email = models.EmailField(unique=True,blank=False)
    pwd = models.CharField(max_length=30,blank=False)

class Company(models.Model):
    comp_name = models.CharField(max_length=30,blank=False)
    comp_country = models.CharField(max_length=30,blank=False)
    comp_email = models.EmailField(unique=True,blank=False)
    comp_pwd = models.CharField(max_length=30,blank=False)
"""