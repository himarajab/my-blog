from django.views.generic import ListView,DetailView
from .models import Profile
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .token import account_activation_token
from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# before we login or register we want to reverse lazy to where we want to redirect
from django.shortcuts import render, redirect
from .forms import UserCreationForm, UserLoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from simpleblog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json


def follow_unfollow_profile(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)
        if obj.user in my_profile.following.all():
             my_profile.following.remove(obj.user)
        else:
             my_profile.following.add(obj.user)
        
        # stay in the same page
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profile-list')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.email = form.cleaned_data['email']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.is_active = False
            new_user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Account'

            message  = render_to_string('registration/account_activation_email.html',
            {
                'user':new_user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token':account_activation_token.make_token(new_user),
            })

            new_user.email_user(subject=subject,message=message)
            return HttpResponse('registered succesfully and activation sent')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {
        'title': 'register',
        'form': form,
    })

# @unauthenticated_user
# def registerPage(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, 'Account was created for ' + username)

#             return redirect('login')

#     context = {'form': form}
#     return render(request, 'accounts/register.html', context)



def my_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        # to remove very weired space in the user name
        username2 = username.strip()

        password = request.POST['password']
        user = authenticate(request, username=username2, password=password)
        # import ipdb ; ipdb.set_trace()
        if user is not None:
            login(request, user)
            return redirect('accounts:profile')
        else:
            messages.error(
                request, 'wrong username/password')

    return render(request, 'registration/login.html', {    })

# @unauthenticated_user
# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Username OR password is incorrect')

#     context = {}

#     return render(request, 'accounts/login.html', context)

def logout_user(request):
    logout(request)
    # return redirect('home')
    return render(request, 'registration/logout.html', {
        'title': ' Sign Out'
    })





# add admin user to admin group and remove them from customer group (default)
#  in django admin
# @admin_only
@login_required(login_url='accounts:login')
def profile(request):
    # model.objects() , filter means and to the returned queryset
    posts = Post.objects.filter(author=request.user)
    post_list = Post.objects.filter(author=request.user)
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)
    return render(request, 'registration/profile.html', {
        'title': ' Profile',
        'posts': posts,
        'page': page,
        'post_list': post_list,
    })

    # order_count = orders.count()
    # # display all products then we will filter them
    # myFilter = OrderFilter(request.GET, queryset=orders)
    # orders = myFilter.qs

    # context = {'customer': customer, 'orders': orders, 'order_count': order_count,
    #            'myFilter': myFilter}

# @allowed_users(allowed_roles=['customer','admin'])
@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        # instance : the data which we used to  filled the form with
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            # files cause we have image field
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'Profile Updated ')
            return redirect('accounts:profile')
    # if there's no edit to the data just show it
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'update your profile',
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'registration/profile_update.html', context)


def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None

    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.save()
        login(request,user)
        return redirect('accounts:profile')
    else:
        return render(request,'registration/activation_invalid.html')


class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profiles' #object_list default
    template_name='profiles/main.html'

    def get_queryset(self):    
        all_users = Profile.objects.all().exclude(user=self.request.user)
        print(f'\n{all_users}\n')

        return all_users



class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/detail.html"

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user = self.request.user)
        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False
        
        context['follow'] = follow
        return context