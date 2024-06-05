from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('get_all_post/', get_post, name='get_post'),
    path('create_post/', createPost, name='create_post'),
    path('delete_post/', deletePost, name='deletePost'),
    path('get_post/', getPost, name='getPost'),
    path('update_post/', updatePost, name='update_post'),
    
    # ============ API AUTHENTICATION URL -======
    path('signup/', signup),
    path('login/', login),
    path('test/', testView),
    path('logout/', logout),
]
