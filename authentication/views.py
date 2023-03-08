from django.shortcuts import render,redirect
from django.views.generic import FormView,View
from .utils import RegisterLoginPagesMixin,RedirectURLMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from authentication.forms import RegisterForm,LoginForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.shortcuts import resolve_url
from authentication.tokens import activation_token
from django.utils.http import urlsafe_base64_decode
from rest_framework import permissions
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.conf import settings
from .tokens import activation_token
from authentication.models import UserAccount
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
User = get_user_model()

def activation_email(User,request):
        current_site = get_current_site(request)
        email_subject = 'Activate your account'
        email_body = render_to_string('activate-email.html',{
            'User':User,
            'domain':current_site,
            'uid':urlsafe_base64_encode(force_bytes(User.pk)),
            'token':activation_token.make_token(User) 
        })

        
        email = EmailMessage(subject=email_subject,body=email_body,
                             from_email=settings.EMAIL_FROM_USER,to=[User.email])
        print(email)
        email.send()


class RegisterView(RegisterLoginPagesMixin,RedirectURLMixin,FormView):
    next_page  = 'hospital:doctors'
    template_name = 'authentication/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('authentication:login')
    permission_classes = (permissions.AllowAny, )

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        fname = form.cleaned_data.get('first_name')
        lname = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('patient')
        password = form.cleaned_data.get('password')
        confirm_password = form.cleaned_data.get('confirm_password')
        
        if password == confirm_password:
            
            user = User.objects.create_user(email=email,username=username,password=password)
            print(user)
            form.instance.user = user
            instance = form.save(commit=False)
            print(instance.patient)
            form.save()
            
            activation_email(user,self.request)
            messages.add_message(self.request,messages.SUCCESS,
            "We've sent you an email to verify your account")
            return redirect('authentication:login')
        else:
            raise ValidationError(self.request,'Password fields must match')
    


def activate_user(request,uidb64,token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        print('uid',uid)
        user = User.objects.get(pk=uid)
        print('User',user)
    except Exception as e:
        user=None

    if user and activation_token.check_token(user,token):
        user.email_verified=True
        user.save()

        messages.add_message(request,messages.SUCCESS,
        'Email verified,you can now login')
        return redirect('authentication:login')

    return render(request,'activate-failed.html',{'user':user})
class LoginView(RegisterLoginPagesMixin,RedirectURLMixin,FormView):
    """
    Display the login form and handle the login action.
    """
    next_page = 'hospital:doctors'
    template_name = 'authentication/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('hospital:home')
    redirect_authenticated_user = False
    extra_context = None


    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    


    def form_valid(self, form):
        uname = form.cleaned_data.get('username')
        pword = form.cleaned_data.get('password')
        usr = authenticate(self.request,username=uname,password=pword)
        print('userr',usr)
        if not usr.email_verified:
            messages.add_message(self.request,messages.ERROR,
            'Email is not verified')
            return render(self.request,'activate-email.html')
        if usr is not None:
            print('usr',usr)
            login(self.request,usr)
        else:
            return render(self.request,self.template_name,{'form':self.form_class,'error':'invalid credentials'})
        return super().form_valid(form)

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            return resolve_url(self.next_page)
        else:
            return resolve_url(settings.LOGIN_REDIRECT_URL)
    

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('hospital:home')
