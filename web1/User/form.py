from django.forms import ModelForm
from User.models import User

class UserForm(ModelForm):
    class Meta:
        model=User
        fields="__all__"
