"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from library.users import views
from .users.views import UserViewSet, GetAuthToken
from .books.views import BookViewSet, AuthorViewSet, EditorialViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework_extensions.routers import NestedRouterMixin
from rest_framework_nested import routers
from django.conf.urls import url 

router = routers.SimpleRouter()
router.register(r'authors', AuthorViewSet)

authors_router = routers.NestedSimpleRouter(router, r'authors', lookup='author')
authors_router.register(r'books', BookViewSet, basename='author-books')


router.register('books', BookViewSet)
router.register('editorials', EditorialViewSet)

# authors_router.register('authors', AuthorViewSet)

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', GetAuthToken.as_view()),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'^', include(authors_router.urls)),
]
