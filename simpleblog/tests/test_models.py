# from mixer.backend.django import mixer
import pytest
from django.contrib.auth.models import User

from simpleblog.models import Post

# @pytest.fixture
# def object(request,db):
#     # def ine which field it's value will change and recieve it as argument
#     return mixer.blend('app.model',quantity=request.param)
#
# # pas th name of the fixture we want to parametrize
# @pytest.mark.parametrize('object',[val],indirect=True)
# def test_product_in_stock(object):
#     asser product.in_stock == True


# @pytest.mark.django_db
# def test_model():
#     actual = Post.objects.all()
#     # print(actual)
#     # expected = '[<Post: second post|hima>]'
#
#     assert actual == 'expected'

@pytest.mark.django_db
def test_user_count(db):
    assert User.objects.count() == 2
