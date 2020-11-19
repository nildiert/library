from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('editorials', EditorialViewSet)
