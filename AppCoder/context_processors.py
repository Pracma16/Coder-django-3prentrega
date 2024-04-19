from .models import Avatar

def avatar_context(request):
    avatar = None
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user).first()
    return {'avatar': avatar}
