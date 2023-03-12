from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from _news.models import Article,Journalist
from _news.api.serializers import ArticleSerializer,JournalistSerializer

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class ArticleListCreateApiView(APIView):
    def get(self, request):
        articles = Article.objects.filter(is_active=True)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JournalistListCreateApiView(APIView):
    def get(self, request):
        journalists = Journalist.objects.all()
        serializer = JournalistSerializer(journalists, many=True, context={'request': request})
        return Response(serializer.data)
    def post(self, request):
        serializer = JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailApiView(APIView):
    def get_object(self, pk):
        article_instance = get_object_or_404(Article, pk=pk)
        return article_instance
    
    def get(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = self.get_object(pk=pk)
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        article = self.get_object(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JournalistDetailApiView(APIView):
    def get_object(self, pk):
        journalist_instance = get_object_or_404(Journalist, pk=pk)
        return journalist_instance
    
    def get(self, request, pk):
        journalist = self.get_object(pk=pk)
        serializer = JournalistSerializer(journalist)
        return Response(serializer.data)
    
    def put(self, request, pk):
        journalist = self.get_object(pk=pk)
        serializer = JournalistSerializer(journalist,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        journalist = self.get_object(pk=pk)
        journalist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



    # FUNCTION BASED VIEWS
# @api_view(['GET','PUT','DELETE'])
# def article_detail_api_view(request, pk):
#     try:
#         article_instance = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(
#             {
#                 'errors':{
#                     'code':404,
#                     'message':f'Böyle {pk} numaralı bir makale yok'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
    
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article_instance)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article_instance,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         article_instance.delete()
#         return Response(
#             {
#                 'errors':{
#                     'code':204,
#                     'message':f'Böyle {pk} numaralı makale silindi'
#                 }
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )
    
# @api_view(['GET','PUT','DELETE'])
# def journalist_detail_api_view(request, pk):
#     try:
#         journalist_instance = Journalist.objects.get(pk=pk)
#     except Journalist.DoesNotExist:
#         return Response(
#             {
#                 'errors':{
#                     'code':404,
#                     'message':f'Böyle {pk} numaralı bir yazar yok'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
    
#     if request.method == 'GET':
#         serializer = JournalistSerializer(journalist_instance)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = JournalistSerializer(journalist_instance,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         journalist_instance.delete()
#         return Response(
#             {
#                 'errors':{
#                     'code':204,
#                     'message':f'Böyle {pk} numaralı yazar silindi'
#                 }
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )
    

# @api_view(['GET','POST'])
# def article_list_create_api_view(request):

#     if request.method == 'GET':
#         articles = Article.objects.filter(is_active=True)
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET','POST'])
# def journalist_list_create_api_view(request):

#     if request.method == 'GET':
#         journalists = Journalist.objects.all()
#         serializer = JournalistSerializer(journalists, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = JournalistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


        