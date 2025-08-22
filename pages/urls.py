from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', views.home, name='home'),
  path('contact/', views.contact, name='contact'),
  path('about/', views.about, name='about'),
  path('blog/', views.blog, name='blog'),
  path('blog/createpost/', views.create_post, name='create_post'),
  path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
  path('blog/<slug:slug>/edit/', views.edit_post, name='edit_post'),
  path('blog/<slug:slug>/delete/', views.delete_post, name='delete_post'),
  path('register/', views.register, name='register'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]

urlpatterns += [
  path('login/', auth_views.LoginView.as_view(), name='login'),
]