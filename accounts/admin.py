from django.contrib import admin
from .models import CustomUser, Blog, Category
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['email','username', 'age','mobile_number'] #which fields will be displyed in the listview of users
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('age','mobile_number',)}),
        )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('age','mobile_number',)}),
        )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Blog)
admin.site.register(Category)
