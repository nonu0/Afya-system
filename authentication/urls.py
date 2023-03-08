from django.urls import path
from .views import RegisterView,LoginView,LogoutView
from . import views
app_name = 'authentication'
urlpatterns = [
    path('register',RegisterView.as_view(),name='register'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('login',LoginView.as_view(),name='login'),
    path('activate/<slug:uidb64>/<slug:token>',views.activate_user,name='activate'),

]