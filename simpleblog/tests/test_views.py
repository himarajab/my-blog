import pytest
from mixer.backend.django import mixer
from simpleblog.models import Post
from django.urls import reverse, reverse_lazy
from django.test import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from simpleblog.views import post_detail


@pytest.mark.django_db
def test_view(client):
    url = reverse_lazy('home')
    response = client.get(url)
    post = mixer.blend(Post, id=1)
    print(post)
    # import ipdb ; ipdb.set_trace()
    # print(response['posts'])
    # print(dir(response))
    assert response.status_code == 200
    # assert(len(response.context_data['post_list'])== 1)


@pytest.fixture(scope='module')
def factory():
    return RequestFactory()


@pytest.fixture
def post(db):

    return mixer.blend(Post)


def test_product_detail_authenticated(factory, post):
    path = reverse('article-details', kwargs={'id': 1})
    request = factory.get(path)
    request.user = mixer.blend(User)

    response = post_detail(request, id=1)
    assert response.status_code == 200


# from django.urls import reverse

# from mixer.backend.django import mixer
# from django.test import TestCase
# import pytest

# @pytest.fixture(scope='module')
# def factory():
#     return RequestFactory()

# @pytest.fixture
# def product(db):
#     return mixer.blend('products.Product')

# def test_product_detail_authenticated(factory, product):
#     path = reverse('detail', kwargs={'pk': 1})
#     request = factory.get(path)
#     request.user = mixer.blend(User)

#     response = product_detail(request, pk=1)
#     assert response.status_code == 200

# def test_product_detail_unauthenticated(factory, product):
#     path = reverse('detail', kwargs={'pk': 1})
#     request = factory.get(path)
#     request.user = AnonymousUser()

#     response = product_detail(request, pk=1)
#     assert 'accounts/login' in response.url


# from django.contrib.auth import get_user_model
# from django.test import TestCase

# from rest_framework.test import APIClient

# from .models import Tweet
# # Create your tests here.
# User = get_user_model()

# class TweetTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='cfe',password='somepassword')
#         Tweet.objects.create(content="my first tweet",
#             user=self.user)
#         Tweet.objects.create(content="my first tweet",
#             user=self.user)
#         Tweet.objects.create(content="my first tweet",
#             user=self.userb)
#         self.currentCount = Tweet.objects.all().count()

#     def test_tweet_created(self):
#         tweet_obj = Tweet.objects.create(content="my second tweet",
#             user=self.user)
#         self.assertEqual(tweet_obj.id, 4)
#         self.assertEqual(tweet_obj.user, self.user)

#     def get_client(self):
#         client = APIClient()
#         client.login(username=self.user.username, password='somepassword')
#         return client

#     def test_tweet_list(self):
#         client = self.get_client()
#         response = client.get("/api/tweets/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.json()), 1)

#     def test_tweet_list(self):
#         client = self.get_client()
#         response = client.get("/api/tweets/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.json()), 3)

#     def test_tweets_related_name(self):
#         user = self.user
#         self.assertEqual(user.tweets.count(), 2)

#     def test_action_like(self):
#         client = self.get_client()
#         response = client.post("/api/tweets/action/",
#             {"id": 1, "action": "like"})
#         like_count = response.json().get("likes")
#         user = self.user
#         my_like_instances_count = user.tweetlike_set.count()
#         my_related_likes = user.tweet_user.count()
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(like_count, 1)
#         self.assertEqual(my_like_instances_count, 1)
#         self.assertEqual(my_like_instances_count, my_related_likes)

#     def test_action_unlike(self):
#         client = self.get_client()
#         response = client.post("/api/tweets/action/",
#             {"id": 2, "action": "like"})
#         self.assertEqual(response.status_code, 200)
#         response = client.post("/api/tweets/action/",
#             {"id": 2, "action": "unlike"})
#         self.assertEqual(response.status_code, 200)
#         like_count = response.json().get("likes")
#         self.assertEqual(like_count, 0)

#     def test_action_retweet(self):
#         client = self.get_client()
#         response = client.post("/api/tweets/action/",
#             {"id": 2, "action": "retweet"})
#         self.assertEqual(response.status_code, 201)
#         data = response.json()
#         new_tweet_id = data.get("id")
#         self.assertNotEqual(2, new_tweet_id)
#         self.assertEqual(self.currentCount + 1, new_tweet_id)

#     def test_tweet_create_api_view(self):
#         request_data = {"content": "This is my test tweet"}
#         client = self.get_client()
#         response = client.post("/api/tweets/create/", request_data)
#         self.assertEqual(response.status_code, 201)
#         response_data = response.json()
#         new_tweet_id = response_data.get("id")
#         self.assertEqual(self.currentCount + 1, new_tweet_id)

#     def test_tweet_detail_api_view(self):
#         client = self.get_client()
#         response = client.get("/api/tweets/1/")
#         self.assertEqual(response.status_code, 200)
#         data = response.json()
#         _id = data.get("id")
#         self.assertEqual(_id, 1)

#     def test_tweet_delete_api_view(self):
#         client = self.get_client()
#         response = client.delete("/api/tweets/1/delete/")
#         self.assertEqual(response.status_code, 200)
#         client = self.get_client()
#         response = client.delete("/api/tweets/1/delete/")
#         self.assertEqual(response.status_code, 404)
#         response_incorrect_owner = client.delete("/api/tweets/3/delete/")
#         self.assertEqual(response_incorrect_owner.status_code, 401)
