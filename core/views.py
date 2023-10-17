from django.shortcuts import render
from django.views.generic import TemplateView, FormView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.urls import reverse

class IndexPage(TemplateView):
    template_name = 'core/index-page.html'
    
@method_decorator(login_required, name='dispatch')
class ProfileDetail(TemplateView):
    template_name = 'accounts/profile-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = UserProfile.objects.get(user=self.request.user)
        return context
    
@method_decorator(login_required, name='dispatch')
class EditProfile(UpdateView):
    model = UserProfile
    template_name = "accounts/edit-profile.html"
    form_class = UserProfileForm
    
    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
    
    def form_valid(self, form):
        if form.is_valid():
            f = form.save(commit=False)
            user_data = self.request.POST
            first_name = user_data.get('first_name')
            last_name = user_data.get('last_name')
            User.objects.filter(pk=self.request.user.pk).update(first_name=first_name, last_name=last_name)
            f.save()
        
        return super(EditProfile, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('core:profile_detail')
    