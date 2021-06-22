from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrraper_func(request, *args, **kwrgs):
        if request.user.is_authenticated:
          return redirect('home')
        else:
          return view_func(request, *args, **kwrgs)
    return wrraper_func    

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwrgs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:    
               return view_func(request, *args, **kwrgs) 
            else:
                return HttpResponse('You are not authorized to view this page')   
        return wrapper_func
    return decorator           

def admin_only(view_func):
    def wrapper_function(request, *args, **kwrgs):
        group = None
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user-page')    

        if group == 'admin':
            return view_func(request, *args, **kwrgs) 
    return wrapper_function               

