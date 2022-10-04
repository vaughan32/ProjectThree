from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.db.models.signals import post_save

class User(AbstractUser):
    is_orgarnizer = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    
    def __str__(self):
        return f' User {self.first_name} {self.last_name}'


class UserProfile(models.Model):
    user_profile = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'Profile {self.user_profile.first_name} {self.user_profile.last_name}'
    
class UserAgent(models.Model):
    user_agent = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_agent = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return f'Agent {self.user_agent.first_name} {self.user_agent.last_name}'

class UserCategory(models.Model):
    category_name = models.CharField(max_length=150)
    category_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return f'Category {self.category_name}'


class UserLead(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField(default=20)
    email = models.EmailField(max_length=150)
    description = models.TextField()
    agent_lead = models.ForeignKey(UserAgent,null=True,blank=True,on_delete=models.SET_NULL)
    profile_lead = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    category_lead = models.ForeignKey(UserCategory, related_name='UserLead',null=True,blank=True,on_delete=models.SET_NULL)
    date_joined = models.DateTimeField(default=timezone.now)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return f'Lead {self.first_name} {self.last_name}'


#  Signals
def create_user(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user_profile = instance)


post_save.connect(create_user,sender=User)

 