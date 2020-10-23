from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowList, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router.register(r'follow', FollowList, basename='followers')
router.register(r'group', GroupViewSet, basename='group')


urlpatterns = [
    path('', include(router.urls)),
]
