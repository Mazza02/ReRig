from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('login/', views.login, name="login"),
path('register/', views.register, name="register"),
path('logout/', views.logout, name="logout"),
path('account/', views.account, name="account"),
path('search/', views.search, name="search"),
path('add_post/', views.add_post, name="add_post"),
#not sure about this last line will need to figure this out
path('post/<int:id>', views.show_post, name="show_post"),
]
