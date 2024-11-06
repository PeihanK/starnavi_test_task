from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import RegisterUserView, LoginView, LogoutView
from posts.views import PostListCreateView, PostDetailView
from comments.views import CommentListCreateView, CommentDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterUserView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/logout/', LogoutView.as_view()),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/posts/', PostListCreateView.as_view()),
    path('api/posts/<int:pk>/', PostDetailView.as_view()),
    path('api/posts/<int:post_pk>/comments/', CommentListCreateView.as_view()),
    path('api/comments/<int:pk>/', CommentDetailView.as_view()),
]
