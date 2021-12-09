# 引入path
from . import views
from django.urls import path

# 正在部署的应用的名称
app_name = 'userprofile'

urlpatterns = [
    # path函数将url映射到视图
    #查看文章列表，设置为默认页面
    # 用户登录
    path('login/', views.user_login, name='login'),
    # 用户退出
    path('logout/', views.user_logout, name='logout'),
    # 用户注册
    path('register/', views.user_register, name='register'),
]