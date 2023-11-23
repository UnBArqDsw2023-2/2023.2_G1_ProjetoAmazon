from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from authuser.models import User

@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    return render(request, 'registration/profile.html', {'user': user})
