from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer


class CommentListCreateView(generics.ListCreateAPIView):
	serializer_class = CommentSerializer
	permission_classes = (permissions.IsAuthenticated,)

	def get_queryset(self):
		return Comment.objects.filter(post_id=self.kwargs['post_pk'])

	def perform_create(self, serializer):
		serializer.save(author=self.request.user, post_id=self.kwargs['post_pk'])


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = (permissions.IsAuthenticated,)
