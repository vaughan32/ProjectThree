from django  import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=254,help_text='Required. Input a valid email address.')
    first_name = forms.CharField(max_length=50,help_text='Required. Input a a vlid name.')
    last_name = forms.CharField(max_length=50,help_text='Required. Input a a vlid name.')
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        field_classes = {'username' :UsernameField}
