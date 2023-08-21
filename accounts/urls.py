from django.urls import path
from .views import SignUpView, CategoryListView,BlogListView,BlogCreateView,BlogDetailView, BlogUpdateView,BlogDeleteView,UserBlogListView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', CategoryListView, name='home'),
    path('<int:name>/', UserBlogListView, name='userbloglist'),
    path('<str:cats>/', BlogListView, name='bloglist'),
    path('<str:cats>/detail/<int:pk>/',BlogDetailView.as_view(), name='blogdetail' ),
   
   
    path('create/blogcreate', BlogCreateView.as_view(), name='blogcreate'),
    
    path('<int:pk>/delete/',BlogDeleteView.as_view(), name='blogdelete' ),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='blogupdate')    

]