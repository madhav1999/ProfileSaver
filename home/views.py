from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import details
from .forms import forYouForm
from django.contrib.auth.models import User


# for accessing login_required decorator function
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.views.generic.edit import DeleteView
# for login creation separately for people instead of giving admin access
from django.contrib.auth.views import LoginView, LogoutView

# for signup creation separately for people instead of showing admin interface
from django.views.generic.edit import CreateView

# user creation function is a django function
from django.contrib.auth.forms import UserCreationForm


# libraries for class based views
from django.views.generic import TemplateView
# mixin inplace of decorator function it is mixin class
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'  # for first function
    login_url = '/admin'  # for second function, mixin class concept instead of decorators

####################################################

# login class


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

# logout class


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

# signup class


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/login'


class forYouList(LoginRequiredMixin, ListView):
    model = details
    context_object_name = "details"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.fory.all()


class forYouUpdateView(UpdateView):
    model = details
    form_class = forYouForm
    success_url = '/allTabs'
    # from django.contrib.auth.models import User
    # u = User.objects.get(username=request.user)
    # u.set_password('new password')
    # u.save()

    def post(self, request, **kwargs):
        my_data = request.POST['Password']
        u = User.objects.get(username=request.user)
        u.set_password(my_data)
        u.save()
        return HttpResponseRedirect(self.success_url)


class forYouCreateView(CreateView):
    model = details
    form_class = forYouForm
    success_url = '/allTabs'

    # this definition is for in our model there is one column for user inorder to fill it automatically
    def form_valid(self, form):  # this is to tell the logged user details has to be automatically filled when we create a new rack of data in data table
        # not to save automatically as it throws error as we are not giving user details in the form
        self.object = form.save(commit=False)
        self.object.user = self.request.user  # we are requesting for user details

        u = User.objects.get(username=self.object.user)
        u.set_password(self.request.POST['Password'])
        u.save()
        self.object.save()
        return HttpResponseRedirect(self.success_url)
