from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework_nested import routers

from library.users import views

from .api.views import (AuthorBooksViewSet, AuthorViewSet, BookViewSet,
                        EditorialViewSet)
from .users.views import GetAuthToken, UserViewSet

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet, basename='book')
router.register('editorials', EditorialViewSet)
router.register('users', UserViewSet)

authors_router = routers.NestedSimpleRouter(router, r'authors', lookup='author')
authors_router.register(r'books', AuthorBooksViewSet, basename='author-books')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', GetAuthToken.as_view()),
    path('admin/', admin.site.urls),
    url(r'^', include(authors_router.urls)),
]
