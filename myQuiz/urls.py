from django.urls import path,reverse_lazy
from django.conf.urls import url,include
from django.contrib.auth.urls import views as auth_views
from myQuiz import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name='index'), 
    url(r'register',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'), 
    path('logout', views.user_logout, name='logout'),
    path('main',views.main,name="main"),
    path('start',views.startPage,name="startPage"),


    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
        name="password_reset_complete"),
]