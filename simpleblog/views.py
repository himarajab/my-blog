from simpleblog.owner import   OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
from simpleblog.models import Post
# from .forms import PostForm
from .forms import *
from .models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import HttpResponseRedirect,HttpResponse


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = '-post_date'
    paginate_by = 3

    # to grap another context and pass it the template
    def get_context_data(self,*args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args,**kwargs)

        posts = Post.objects.all()
        paginator = Paginator(posts, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts
        context['cat_menu'] = cat_menu
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

def category_list_view(request):
    cat_menu_list = Category.objects.all()
    return render(request,'blog/category_list.html',
                  {'cat_menu_list':cat_menu_list})


def category_view(request,cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request,'blog/categories.html',
                  {'cats':cats.title() , 'category_posts':category_posts}
                  )
# class PostCreateView(OwnerCreateView):
#     model = Post
#     fields = ['title', 'text']

# class ArticleUpdateView(OwnerUpdateView):
#     model = Post
#     fields = ['title', 'text']

# class PostDeleteView(OwnerDeleteView):
#     model = Post


def post_detail(request, id):
    template_name = 'blog/article_details.html'
    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(active=True)
    total_likes = post.total_likes()
    is_liked = False
    if post.likes.filter(id = request.user.id).exists():
        is_liked = True
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            comment_form = CommentForm()

    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'total_likes' : total_likes,
                                           'is_liked' : is_liked,})

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


# def likePost(request):
#     if request.method == 'GET':
#            post_id = request.GET['post_id']
#            likedpost = Post.objects.get(pk=post_id) #getting the liked posts
#            m = Like(post=likedpost) # Creating Like Object
#            m.save()  # saving it to store in database
#            return HttpResponse("Success!") # Sending an success response
#     else:
#            return HttpResponse("Request method is not a GET")

def like_view(request,pk):
    # grap it from the submitted form by it's name in the form
    # post = get_object_or_404(Post,request.POST.get('post_id'))
    post = get_object_or_404(Post,id = pk)
    is_liked = False
    # if user already clicked like then display dislike
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        # we say specific user like this post
        post.likes.add(request.user)
        is_liked = True
#      redirect to same page
    return HttpResponseRedirect(reverse('article-details',args =[str(pk)]))


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
