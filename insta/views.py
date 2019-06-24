from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url=/'accounts/login')
def timelines(request):
    current_user = request.user 
    images = Image.objects.order_by('-date_uploaded')
    profiles = Profile.objects.order_by('-last_update')
    comments = Comments.objects.order_by('-time_comments')
    return render(request, 'timelines.html', {'images':images, 'profiles':profiles, 'user_profile':user_profile, 'comments':comments})
'''
Function that renders user profile
