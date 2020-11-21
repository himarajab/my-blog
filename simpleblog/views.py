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
    page = request.GET.get('page',1)
    paginator = Paginator(all_comments,2)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        # if user change the page to name
        comments = paginator.page(1)
    except EmptyPage:
        # if user type page = 10 and the max one is 2 
        comments = paginator.page(paginator.num_pages)

    user_comment = None


    # total_likes = post.total_likes()
    
    # if total_likes > 0 :
    #     total_likes = total_likes
    # else:
    #     total_likes = 0

    # liked = False
    # if post.likes.filter(id=request.user.id).exists():
    #     liked= True

    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = NewCommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            comment_form = NewCommentForm()

    else:
        comment_form = NewCommentForm()

    return render(request, template_name, {'post': post,
                                           'user_comment':  user_comment, 'all_comments': all_comments, 'comments':comments,
                                           'new_comment': new_comment,
                                        #    'total_likes' : total_likes,'liked':liked,
                                           'comment_form': comment_form,
                                           })

                   


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

