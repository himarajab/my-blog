# from django.test import RequestFactory
# from django.urls import reverse
# from django.contrib.auth.models import User,AnonymouseUser
# from simpleblog.views import HomeView
# import pytest
#
# @pytest.mark.django_db
# class TestViews:
#     def test_view_name_authenticated(self):
#         mixer.blend
#         path = reverse('template_name',kwargs={'pk':1})
#         request = RequestFactory().get(path)
#         # to create a new user instance
#         request.user = mixer.blend(User)
#
#         response = view_name(request,pk=1)
#         assert 'accounts/login' in response.url


#     def test_view_name_unauthenticated(self):
#         mixer.blend
#         path = reverse('template_name',kwargs={'pk':1})
#         request = RequestFactory().get(path)
#         # to create a new user instance
#         request.user = AnonymouseUser()
#
#         response = view_name(request,pk=1)
#         assert response.status_code = 200