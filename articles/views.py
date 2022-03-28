from rest_framework import  generics,mixins
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.

class ArticleMixinView(mixins.ListModelMixin,
mixins.RetrieveModelMixin,
mixins.CreateModelMixin,
mixins.UpdateModelMixin,
mixins.DestroyModelMixin,
generics.GenericAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'article_id'

    def get(self,request,*args,**kwargs):
        print(args,kwargs)
        pk = kwargs.get('article_id')
        if pk is not None:
            return self.retrieve(request,*args,**kwargs) 
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def update(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

article_mixin_view = ArticleMixinView.as_view()