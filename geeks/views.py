from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse



class Index(View):
    template_name = 'geeks/index.html'
    my_input ='test' 
    var2 =1
    # form_class = PostForm
    # which fields we want to appear in the page
    # fields = ('first_field','second_field')
    def get(self,request,*args, **kwargs):
        print(f'dir{dir(self)}')
        print(f'vars is {vars(self)}')
        result = 12341
        expected = None
        
        context = locals()
        context['my_input'] = self.my_input
        context['expected'] = expected
        # return JsonResponse(dir(self),safe=False)
        # this line return dict wich will raise error cause it want the returned value to be http response
        # return context
        return render(request,self.template_name ,context)


    def post(self,request,*args, **kwargs):
        print(f'dir{dir(self)}')
        print(f'vars is {vars(self)}')
        entered_val = request.POST.get('entered_val')
        # form = self.form_class(request.POST)
        # if form.is_valid():
        result = None
        expected = None

        context = locals()
        context['entered_val'] = entered_val
        # context['expected'] = expected

        return render(request,self.template_name ,context)
        # return render(request,'geeks/index.html',{})



# def setcookie(request):
#     html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
#     if request.COOKIES.get('visits'):
#         html.set_cookie('dataflair', 'Welcome Back')
#         value = int(request.COOKIES.get('visits'))
#         html.set_cookie('visits', value + 1)
#         print(html)
#     else:
#         value = 1
#         text = "Welcome for the first time"
#         html.set_cookie('visits', value)
#         html.set_cookie('dataflair', text)
#     return html


# def showcookie(request):
#     if request.COOKIES.get('visits') is not None:
#         value = request.COOKIES.get('visits')
#         text = request.COOKIES.get('dataflair')
#         html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
#         html.set_cookie('visits', int(value) + 1)
#         return html
#     else:
#         return redirect('/setcookie')


# def delete_co(request):
#     if request.COOKIES.get('visits'):
#         response = HttpResponse("<h1>dataflair<br>Cookie deleted</h1>")
#         response.delete_cookie("visits")
#     else:
#         response = HttpResponse("<h1>dataflair</h1>need to create cookie before deleting")
#     return response



