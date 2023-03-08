from django.shortcuts import redirect,resolve_url
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.utils.http import url_has_allowed_host_and_scheme

class RegisterLoginPagesMixin(object):
    template_name = None
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            print('user is authenticated')
            return redirect('hospital:home')
        else:
            return super().dispatch(request,*args,**kwargs)

class RedirectURLMixin:
    next_page = None
    redirect_field_name = REDIRECT_FIELD_NAME
    success_url_allowed_hosts = set()

    def get_success_url(self):
        return self.get_redirect_url() or self.get_default_redirect_url()

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name, self.request.GET.get(self.redirect_field_name)
        )
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        print('safe url')
        return redirect_to if url_is_safe else ""


    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        if self.next_page:
            print(self.next_page)
            return resolve_url(self.next_page)
        raise ImproperlyConfigured("No URL to redirect to. Provide a next_page.")


    def get_success_url_allowed_hosts(self):
        print('success')
        return {self.request.get_host(), *self.success_url_allowed_hosts}

