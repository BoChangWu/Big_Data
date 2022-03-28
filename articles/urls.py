from django.urls import path
from . import views

urlpatterns=[

    path('<str:article_id>',views.article_mixin_view),
    path('post',views.article_mixin_view),
    path('delete/<str:article_id>',views.article_mixin_view),
    path('update/<str:article_id>',views.article_mixin_view)
]