from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User,AnonymousUser
from simpleblog.views import HomeView
import pytest
# from django.test import TestCase
#
# @pytest.fixture
# def factory():
#     return RequestFactory()
# #
# @pytest.fixture(scope='module')
# # to be able to access the database
# def post(db):
#     return mixer.blend('app.model')
#
# def test_view_name_authenticated(factory,object):
#     mixer.blend
#     path = reverse('template_name',kwargs={'pk':2})
#     request = factory.get(path)
#     # to create a new user instance
#     request.user = mixer.blend(User)
#
#     response = view_name(request,pk=1)
#     assert 'accounts/login' in response.url
#
#
# def test_view_name_unauthenticated(factory,object):
#     mixer.blend
#     path = reverse('template_name',kwargs={'pk':1})
#     request = factory.get(path)
#     # to create a new user instance
#     request.user = AnonymouseUser()
#
#     response = view_name(request,pk=1)
#     assert response.status_code = 200


# @pytest.mark.django_db
# def test_view(client):
#     url = reverse('home')
#     response = client.get(url)
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_user_detail(client, django_user_model):
#    user = django_user_model.objects.create(
#        username='someone', password='password'
#    )
#    url = reverse('user-detail-view', kwargs={'pk': user.pk})
#    response = client.get(url)
#    assert response.status_code == 200
#    assert 'someone' in response.content

