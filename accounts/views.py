from django.shortcuts import render
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CustomUserCreationForm, CreateBlogForm
from django.urls import reverse_lazy
from .models import Blog, Category, CustomUser

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


# class CategoryListView(ListView):
#     # model = Category
#     model = Category, CustomUser  Cannot use multiple views like that, we'll have to make context dictionary
#     template_name ='home.html'
#     fields = "__all__"


def CategoryListView(request):
    categories = Category.objects.all()
    users = request.user

    context = {
        'categories': categories,
        'users' : users,
    }
    return render(request, 'index.html', context)



# class BlogListView(ListView):
#     model = Blog
#     template_name = 'blog_list.html'

def BlogListView(request, cats):
    blogs = Blog.objects.filter(category_id=cats)

    context={
        'blogs':blogs,
        'cats':cats
    }
    return render(request,'blog_list.html',context)




class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_new.html'
    # We specify it in forms.py
    # fields = '__all__'
    form_class = CreateBlogForm
    
    
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        # Get the current user's name
        current_user_name = self.request.user.id

        # Construct the success URL with the user's name as argument
        success_url = reverse_lazy('userbloglist', args=[current_user_name])
        return success_url



class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'




# class UserBlogListView(ListView):
#     model = Blog
#     template_name = 'user_blog_list.html'
def UserBlogListView(request, name):
    name_blogs = Blog.objects.filter(author_id=name)
    username = request.user

    context={
        'name_blogs':name_blogs,
        'username':username
    }
    return render(request, 'user_blog_list.html', context)




class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url=reverse_lazy('home')
   


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog_update.html'
    fields = "__all__"
    
    # def get_success_url(self):
    #     return reverse_lazy('home')
    success_url = reverse_lazy('home')

