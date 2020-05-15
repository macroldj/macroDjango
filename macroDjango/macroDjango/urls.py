"""macroDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.static import serve
from .settings import MEDIA_ROOT, STATIC_ROOT
from django.conf.urls import url
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from users.api.views import UserViewset
from users.views import ProvinceView, CityView, CountyView, IndexView, RegisterView, ActiveView, LoginView, LogoutView, \
    ForgetPwdView, ResetView, NewPwdView, CheckView, UserInfoView, SettingInfoView, ModifyContactView, \
    DeleteContactView, DefaultContactView, MyCommentsView, MyCollectView, HomePageView

router = DefaultRouter()
router.register(r'users', UserViewset, basename="users")

urlpatterns = [

    # 工具
    re_path(r'^captcha/', include('captcha.urls')),
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),

    # 获取省市区信息
    path('province/', ProvinceView.as_view(), name='province'),
    path('city_<int:pid>/', CityView.as_view(), name='city'),
    path('county_<int:pid>/', CountyView.as_view(), name='county'),

    # 网站页面
    # 主页
    path('', IndexView.as_view(), name='index'),
    # 新闻资讯
    path('news/', include(('news.urls', 'news'))),
    # 旅游页面
    path('scenicspots/', include(('scenicspots.urls', 'scenicspots')), name='scenicspots'),
    # 商城相关
    path('shop/', include(('shop.urls', 'shop')), name='shop'),
    # 游记相关
    path('diarys/', include(('diarys.urls', 'diarys')), name='diarys'),

    # 用户相关
    path('register/', RegisterView.as_view(), name='register'),
    # 激活
    path('active/<slug:active_code>', ActiveView.as_view(), name='active'),
    # 登陆
    path('login/', LoginView.as_view(), name='login'),
    # 登出
    path('logout/', LogoutView.as_view(), name='logout'),
    # 忘记密码
    path('forget_pwd', ForgetPwdView.as_view(), name='forget_pwd'),
    # 找回密码页面
    path('find/<slug:find_code>', ResetView.as_view(), name='find'),
    # 修改密码
    path('new_pwd/', NewPwdView.as_view(), name='new_pwd'),
    # 签到页面
    path('check/', CheckView.as_view(), name='check'),
    # 设置页面
    path('userinfo/<slug:info_type>', UserInfoView.as_view(), name='userinfo'),
    # 信息修改
    path('setting/<slug:setting_type>', SettingInfoView.as_view(), name='setting'),
    # 联系人信息修改
    path('modify_contact/<int:contact_id>', ModifyContactView.as_view(), name='modify_contact'),
    # 联系人信息删除
    path('delete_contact/<int:contact_id>', DeleteContactView.as_view(), name='delete_contact'),
    # 设置默认联系人
    path('default_contact/<int:contact_id>', DefaultContactView.as_view(), name='default_contact'),
    # 我的评论
    path('mycomments', MyCommentsView.as_view(), name='mycomments'),
    # 我的收藏
    path('mycollect', MyCollectView.as_view(), name='mycollect'),
    # 我的主页
    path('homepage', HomePageView.as_view(), name='homepage'),

    # 其余操作相关
    path('operation/', include(('operation.urls', 'operation')), name='operation'),

    # 支付相关
    path('pay/', include(('pay.urls', 'pay')), name='pay'),

    # 用户上传文件路径
    re_path(r'media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # static文件路径
    re_path(r'static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),

    # api
    # 用户模块api
    path("api/", include("users.api.urls")),
    # 游记模块api
    path("api/", include("diarys.api.urls")),
    # 新闻模块api
    path("api/", include("news.api.urls")),
    # 旅游模块
    path("api/", include("scenicspots.api.urls")),
    # 商店模块
    path("api/", include("shop.api.urls")),

    # 下面是测试的
    path("api_auth/", include("rest_framework.urls", namespace='rest_framework')),
    # rest自带的token认证模式
    url(r"^api_token_auth/", views.obtain_auth_token),
    # jwt
    url(r"^jwt_auth/", obtain_jwt_token),
    url(r'apis/', include(router.urls), name='apis'),
]