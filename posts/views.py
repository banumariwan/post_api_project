from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post



class PostListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all().values('id', 'title', 'content', 'created_at')
        return Response(list(posts))