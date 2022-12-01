from .models import Blog
from .serializers import *
from rest_framework import viewsets
from .permissions import *
from rest_framework.permissions import *
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
import django_filters
from rest_framework_simplejwt.authentication import JWTAuthentication
import logging
logger = logging.getLogger('user')

# Viewset을 활용한 게시판 기능.
# Blog의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    
    

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
class BlogView(ListCreateAPIView):
    authentication_classes=[JWTAuthentication]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # 필터 기능 추가
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['user']
    def perform_create(self, serializer):
        # 현재 요청한 유저를 작성자로 설정
        serializer.save(user=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = BlogSerializer(queryset, many=True)
        logger.info(request.user)
        return Response(serializer.data)

    def create(self, request):
        serializer = BlogSerializer(data=request.data) #Request의 data를 UserSerializer로 변환
 
        if serializer.is_valid():
            serializer.save() #UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            logger.info(request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED) #client에게 JSON response 전달
        else:
            logger.info(request.user)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    authentication_classes=[JWTAuthentication]
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1  # 조회수 1 증가
        instance.save()
        serializer = self.get_serializer(instance)
        logger.info(request.user)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.save()
        serializer = self.get_serializer(instance)
        logger.info(request.user)
        
        return Response(serializer.data)

    def destory(self, request, *args, **kwargs):
        blog = self.get_object()
        logger.info(request.user)
        blog.delete()

        return Response({"message": "글이 삭제 되었습니다."})

class BlogStatisticsView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [AllowAny]
    def get(self, request):
        male_cnt = Blog.objects.filter(user__gender="M").count()
        female_cnt = Blog.objects.filter(user__gender="F").count()
        logger.info(request.user)
        return Response({"Male":male_cnt, "Female": female_cnt}, status=status.HTTP_200_OK)

    # def post(self, request):
    #     user = request.GET.get('user')
    #     user_board = Blog.objects.filter(user__email=user).count()
    #     return Response({f"{user} 의 게시물 개수": user_board}, SAFE_METHODS=status.HTTP_200_OK)