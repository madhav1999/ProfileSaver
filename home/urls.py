from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('home', views.HomeView.as_view(), name="home"),

    #path('authorized', views.AuthorizedView.as_view(), name="authorized.page"),
    path('login', views.LoginInterfaceView.as_view(), name="login"),
    path('logout', views.LogoutInterfaceView.as_view(), name="logout"),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('allTabs', views.forYouList.as_view(), name="allTabsY.list"),
    path('allTabs/<int:pk>/edit',
         views.forYouUpdateView.as_view(), name="forYou.update"),
    path('allTabs/new', views.forYouCreateView.as_view(), name="forYou.new"),

]
