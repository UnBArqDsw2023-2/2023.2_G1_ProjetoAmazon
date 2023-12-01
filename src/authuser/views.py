from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic.edit import CreateView

from authuser.models import User
from authuser.forms import UserRegistrationForm

@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'registration/profile.html', {'user': user})


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    form_class = UserRegistrationForm
    success_message = 'Your account was created successfully'

