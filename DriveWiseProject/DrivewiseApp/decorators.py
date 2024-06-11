

from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse
from .utils.firebase_utils import verify_firebase_token

def firebase_auth_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        firebase_token = request.session.get('firebase_token')
        
        if firebase_token:
            uid = verify_firebase_token(firebase_token)
            if uid:
                request.uid = uid
                return view_func(request, *args, **kwargs)

        return redirect(reverse('login'))
    
    return wrapped_view
