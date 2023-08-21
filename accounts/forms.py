from .models import CustomUser, Blog, Category
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age','mobile_number',)


class CustomUserChangeForm(UserChangeForm):
    model = CustomUser
    fields = fields = UserCreationForm.Meta.fields 

# choice_list = [('meera bai', 'meera bai'), ('ram kripalu', 'ram kripalu')]
choice_list = Category.objects.all().values_list('name','name')


# form_class = CreateBlogForm in respective view
class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"

        widgets= {
            # To show a dropdown for category, else we were getting input test fields
            'category' : forms.Select(choices=choice_list)
        }
