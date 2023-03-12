from django.urls import path
from _news.api import views as api_views

urlpatterns = [
    # path('articles/',api_views.article_list_create_api_view,name="article-list"),
    # path('journalists/',api_views.journalist_list_create_api_view,name="journalist-list"),

    # path('articles/<int:pk>',api_views.article_detail_api_view,name="article"),
    # path('journalists/<int:pk>',api_views.journalist_detail_api_view,name="journalist"),

    path('articles/',api_views.ArticleListCreateApiView.as_view(),name="article-list"),
    path('journalists/',api_views.JournalistListCreateApiView.as_view(),name="journalist-list"),

    path('articles/<int:pk>',api_views.ArticleDetailApiView.as_view(),name="article-detail"),
    path('journalists/<int:pk>',api_views.JournalistDetailApiView.as_view(),name="journalist-detail"),


]