from django.db.models import Count, Q
from django.db.models.functions import TruncDate
from rest_framework import generics, permissions, status
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.dateparse import parse_date


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


class CommentsDailyBreakdownView(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request, *args, **kwargs):
		start_date = request.data.get('start_date')
		end_date = request.data.get('end_date')

		if not start_date or not end_date:
			return Response({'error': 'You must specify a start and end date'})

		try:
			start_date = parse_date(start_date)
			end_date = parse_date(end_date)

		except ValueError:
			return Response({"error": "Invalid date format, expected YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

		comments = Comment.objects.filter(
			created_at__gte=start_date, created_at__lte=end_date
		)

		daily_breakdown = comments.annotate(date=TruncDate('created_at')) \
			.values('date') \
			.annotate(
			total_comments=Count('id'),
			blocked_comments=Count('id', filter=Q(is_blocked=True))
		) \
			.order_by('date')

		return Response(daily_breakdown, status=status.HTTP_200_OK)

