from itertools import chain
from members.models import Profile
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank
from django.core import serializers
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.template.loader import render_to_string
from simpleblog.owner import   OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,RedirectView
from simpleblog.models import Post
from .forms import *
from .models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse


def posts_of_following_profiles(request):
    # get the logged in profile
    curr_profile = Profile.objects.get(user=request.user)
    # import ipdb ; ipdb.set_trace()
    # check who we are following 
    users = [user for user in curr_profile.following.all()]
    # intial variables
    posts = []
    qs = None

    #  get the posts of people who we are following
    for user in users:
        profile = Profile.objects.get(user=user)
        
        profile_posts = profile.user.blog_posts.all()
        
        posts.append(profile_posts)

    my_posts = curr_profile.profiles_posts()
    posts.append(my_posts)

    # sort and chain the queryset and unpack the post list 
    if len(posts) > 0:
        qs = sorted(chain(*posts),reverse=True,key=lambda obj: obj.publish)

    return render(request,'blog/main.html',{'profile':curr_profile,'posts':qs})

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    paginate_by = 3

    # to grap another context and pass it the template
    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        l_posts= Post.objects.all().reverse()[0:3]
        
        # l_comments= Comment.objects.filter(active=True)[:5]

        context = super(HomeView, self).get_context_data(*args,**kwargs)

        posts = Post.objects.all()
        paginator = Paginator(posts, self.paginate_by)
        
        # post = get_object_or_404(Post, id=id)
        # total_likes = post.total_likes()
        
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        context['cat_menu'] = cat_menu
        context['l_posts'] = l_posts
        # context['l_comments'] = l_comments
        return context


# def home(request):
#     posts = Post.objects.all()
# # the query and number of elements per page
#     paginator = Paginator(posts, 3)
# # what is currently page i'm in
#     page = request.GET.get('page')
#     try:
# # to go over all pages except the first and last
#         posts = paginator.page(page)
# # means it's first page
#     except PageNotAnInteger:
#         posts = paginator.page(1)
# # i'm in the last page
#     except EmptyPage:
#
#         posts = paginator.page(paginator.num_page)
#     context = {
#         'title': 'الصفحة الرئيسية',
#         'posts': posts,
#         'page': page,
#     }
#     return render(request, 'blog/index.html', context)

class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context

# class PostCreateView(OwnerCreateView):
#     model = Post
#     fields = ['title', 'text']

# class ArticleUpdateView(OwnerUpdateView):
#     model = Post
#     fields = ['title', 'text']

# class PostDeleteView(OwnerDeleteView):
#     model = Post
def post_single(request, post):
    
    post = get_object_or_404(Post, slug=post, status='published')

    all_comments = post.comments.filter(status=True)
    page = request.Get.get('page',1)
    paginator = paginator(all_comments,1)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        # if user change the page to name
        comments = paginator.page(1)
    except EmptyPage:
        # if user type page = 10 and the max one is 2 
        comments = paginator.page(paginator.num_pages)

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()
    return render(request, 'single.html', {'post': post, 'user_comment':  user_comment, 'all_comments': all_comments, 'comments':comments,'comment_form': comment_form})

def post_detail(request, id):
    template_name = 'blog/article_details.html'
    post = get_object_or_404(Post, id=id)
    all_comments = post.comments.filter(status=True)
    
    
    # page = request.GET.get('page',1)
    # paginator = Paginator(all_comments,2)
    # try:
    #     comments = paginator.page(page)
    # except PageNotAnInteger:
    #     # if user change the page to name
    #     comments = paginator.page(1)
    # except EmptyPage:
    #     # if user type page = 10 and the max one is 2 
    #     comments = paginator.page(paginator.num_pages)



    # total_likes = post.total_likes()
    
    # if total_likes > 0 :
    #     total_likes = total_likes
    # else:
    #     total_likes = 0

    # liked = False
    # if post.likes.filter(id=request.user.id).exists():
    #     liked= True

    # new_comment = None
    # Comment posted
    # if request.method == 'POST':
    #     comment_form = NewCommentForm(data=request.POST)
    #     if comment_form.is_valid():

    #         # Create Comment object but don't save to database yet
    #         new_comment = comment_form.save(commit=False)
    #         # Assign the current post to the comment
    #         new_comment.post = post
    #         # Save the comment to the database
    #         new_comment.save()
    #         return HttpResponseRedirect('/'+post.id)
    # else:
    comment_form = NewCommentForm()

    return render(request, template_name, {'post': post,
                                          'all_comments': all_comments, 
                                        #    'new_comment': new_comment,
                                        #    'total_likes' : total_likes,'liked':liked,
                                           'comment_form': comment_form,
                                           })

def add_comment(request):
    if request.method == 'POST':
  
        if request.POST.get('action') == 'delete':
            id = request.POST.get('nodeid')
            print(id)
            c = Comment.objects.get(id=id)
            c.delete()
            return JsonResponse({'remove': id})
        else:
            comment_form = NewCommentForm(request.POST)
            print(comment_form)
            if comment_form.is_valid():
                user_comment = comment_form.save(commit=False)
                result = comment_form.cleaned_data.get('content')
                user = request.user.username
                user_comment.author = request.user
                user_comment.save()
                return JsonResponse({'result': result, 'user': user})

# class ArticleDetailView(DetailView):
#     model = Post
#     template_name = 'article_details.html'
#
#     def get_context_data(self,*args, **kwargs):
#         # check before save data from comment form
#         post = get_object_or_404(Post,id=id)
#         comments = Comment.objects.filter(active=True)
#         new_comment = None
#
#         if self.request.method == 'POST':
#             comment_form = CommentForm(data=self.request.POST)
#
#             if comment_form.is_valid():
#             # don't save until the relation being set
#
#                 new_comment = comment_form.save(commit=False)
#             #     to connect the comment to related post
#
#                 new_comment.post = post
#                 new_comment.save()
#         else:
#             comment_form = CommentForm()
#
#         context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
#         context['comments'] = comments
#         context['comment_form'] = comment_form
#         return context
def latest_posts(request):
    l_posts= Post.objects.all()[0:5]
    
    template_name = 'blog/latest_posts.html'

    return render(request, template_name, l_posts)




@login_required
def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        profile = User.objects.get(profile=user.id)
        # print(f'\n {profile} \n')
        # import ipdb ; ipdb.set_trace()
        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'

            post_obj.save()
            like.save()

        # data = {
        #     'value': like.value,
        #     'likes': post_obj.liked.all().count()
        # }

        # return JsonResponse(data, safe=False)
    return redirect(reverse_lazy('home'))



@login_required(login_url='accounts:login')
def favourite_add(request,id):
    post = get_object_or_404(Post, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove()
    else:
        post.favourites.add(request.user)
    # return the user to the same page they was on 
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required(login_url='accounts:login') 
def user_favourites(request):
    # import ipdb ; ipdb.set_trace()
    # author = Post.blog_posts.author
    
    user_favourites= Post.objects.filter(liked=request.user).values()

    # user_favourites= Post.objects.all()
    return render(request,'blog/user_favourites.html',{'user_favourites':user_favourites}) 





class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
# which fields we want to appear in the page
    # fields = ('first_field','second_field')


# class AddCategoryView(CreateView):
#     model = Category
#     template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    # should now allow editing the author
    # fields = '__all__'
    form_class = UpdateForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    # must be explicitly configure
    success_url = reverse_lazy('home')


def post_search(request):
    form = PostSearchForm()
    q=''
    results = []
    category = ''
    query = Q()

    # if request.POST.get('action') =='post':
    #     search_string = str(request.POST.get('searchString'))
    #     # print(search_string)
    #     if search_string is not None:
    #         # return only three matched items from the database
    #         search_string = Post.objects.filter(title__contains=search_string)[:3]
    #         data = serializers.serialize('json',list(search_string),fields=('pk','title'))
    #         return JsonResponse({'search_string':data},safe=False)
            
    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            # once the form checked the data is avaliable via the cleaned mthod
            q = form.cleaned_data['q']
            # category = form.cleaned_data['category']
            # if category is not None:
            #     query &= Q(category=category)

            if q is not None:
                query &= Q(title__contains=q)

            # vector = SearchVector('title',weight='A') + \
            #     SearchVector('content',weight='B')
            # query = SearchQuery(q)

            # results = Post.objects.annotate(rank=SearchRank(vector,query,cover_density=True)).order_by('-rank')

            # print(f'\n{results}\n')
            # # results = Post.objects.annotate(search=SearchVector('title','content'),).filter(search=SearchQuery(q))
            # # results = Post.objects.filter(title__search=q)
            results = Post.objects.filter(query)


    return render(request,'blog/search.html',{'form':form,'q':q,'results':results}) 


# def post_search(request):
#     form = PostSearchForm()
#     q = ''
#     results = []

#     if 'q' in request.GET:
#         form = PostSearchForm(request.GET)
#         if form.is_valid():
#             q = form.cleaned_data['q']

#             vector = SearchVector('title', weight='A') + \
#                 SearchVector('content', weight='B')
#             query = SearchQuery(q)

#             results = Post.objects.annotate(
#                 rank=SearchRank(vector, query, cover_density=True)).order_by('-rank')

#     return render(request, 'blog/search.html',
#                   {'form': form,
#                    'q': q,
#                    'results': results})