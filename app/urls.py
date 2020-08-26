from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("indexpage/",views.indexpage,name="rp"),
    path("register/",views.RegisterUser,name="registeruser"),
    path("login/",views.Login,name="login"),
    path("loginuser/",views.LoginUser,name="loginuser"),
    path("about/",views.About,name="about"),
    path("service_man/",views.Serviceman,name="serviceman"),
    path("service/",views.Service,name="service"),
    path("bookpage/",views.BookPage,name="bookpage"),
    path("insert/",views.Insert,name="insert"),
    path("alldata/",views.AllData,name="alldata"),
    path("accept/<int:pk>",views.Accept,name="accept"),
    path("conform/",views.Conform,name="conform")
]  
