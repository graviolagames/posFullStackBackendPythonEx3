from django.shortcuts import render
from django.views import View
from .models import Avatar

# Create your views here.
class AvatarView(View):
    def get(self, request):
        avatars = Avatar.objects.all()
        return render(request, 'avatar/avatar_list.html', {'avatars': avatars})
