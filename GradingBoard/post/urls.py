"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from post import views

router = DefaultRouter()
router.register('', views.PostViewSet, basename='post') # Post
router.register(r'(?P<id>\d+)/comment', views.CommentViewSet, basename='comment') # Comments (GET List, CREATE Comment)

app_name = 'post'

urlpatterns = [
    path('', include(router.urls)),

    # Comment detail GET/PATCH/DELETE
    path('<int:id>/comment/<int:comment_id>/',
          views.CommentDetailViewSet.as_view(
            {'get': 'get', 'delete': 'delete', 'put': 'update'}
        ), name='comment-detail'),
]
