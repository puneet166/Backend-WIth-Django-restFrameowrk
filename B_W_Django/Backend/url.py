from django.urls import path
from Backend import views
from django.contrib import admin
from django.contrib.auth import views as auth_views 
urlpatterns=[
    path('detail/<int:pk>/',views.User_upadte),

    path('detail',views.User_detail),
    path('user_details',views.User_Auth_detail),
    

    #path('api/lead/', views.regCreate.as_view() ),
    #path('books/<int:pk>/', views.regDetail.as_view()),


]