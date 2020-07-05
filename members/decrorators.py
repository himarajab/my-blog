from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		# don't display view_func to authenticated user ; E.G (login,register)
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			# if u find group with that name 
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			# if user group name in allowed roles E.G admin
			# execute the view 
			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator


def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
		# this quick temporary fix needs more customization 
		# 
		if group == 'customer':
			return redirect('user-page')
		# allow only admin to view this page 
		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function