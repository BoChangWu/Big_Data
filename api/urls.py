from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)
urlpatterns = [
    path('token/',TokenObtainPairView.as_view(),name="obtain_pair"),
    path('token/refresh/',TokenRefreshView.as_view(),name="refresh"),
    path('token/verify/',TokenVerifyView.as_view(),name='verify'),
    path('articles/',views.article_cover),
    path('article/<int:art_id>',views.get_article),
    path('article/get_last_id',views.last_id),
    path('article/create/<int:art_id>',views.post_article),
    path('article/delete_<str:art_id>',views.delete_article),
    path('article/update_<str:art_id>',views.update_article)
    # path('article/',include('articles.urls')),
   
]