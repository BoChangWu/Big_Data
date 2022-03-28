# from crypt import methods
from django.shortcuts import render
from rest_framework.decorators import api_view
from articles.models import Article,Art,Img,Related
from articles.serializers import ArticleSerializer,ArtSerializer,ImgSerializer,RelatedSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def article_cover(request,*args,**kwargs):

    data=[]
    route_path=[]
    art = Art.objects.all()
    if art:
        for i in range(len(art)):
            data.append(ArtSerializer(art[i]).data)
            data[i]['path']='/art/'+str(i)            
    return Response({'data':data})

@api_view(['GET'])
def last_id(request,*args,**kwargs):
    instance = Art.objects.last()
    if instance:
        serial= ArtSerializer(instance).data
        data=serial['art_id']
        print(data)
    else:
        data=0
    return Response({'data': data})

@api_view(['GET'])
def get_article(request,*args,**kwargs):
    print(args,kwargs)

    art= Art.objects.all().filter(art_id=kwargs['art_id'])
    img = Img.objects.all().filter(art_id=kwargs['art_id'])
    related = Related.objects.all().filter(art_id=kwargs['art_id'])
    data = {}
    if art:
        art_data = ArtSerializer(art[0]).data
        data['title'] = art_data['title']
        data['cover'] = art_data['cover']
        data['content'] = art_data['content']
    if img:
        data['img'] = {}
        for i in range(len(img)):
            data['img']['img'+str(i+1)]=ImgSerializer(img[i]).data
    
    if related:
        data['related'] = {}
        for i in range(len(related)):
            data['related']['rel'+str(i+1)]=(RelatedSerializer(related[i]).data)
    print(data)
    return Response(data)

@api_view(['POST'])
def post_article(request,*args,**kwargs):
    
    data= request.data
    print(data)
    Art.objects.create(title=data['title'],cover=data['cover'],content=data['content'],art_id=kwargs['art_id'])
    
    for i in range(len(data['img'])):
        Img.objects.create(url=data['img'][i],art_id=kwargs['art_id'])
    
    for i in range(len(data['related'])):
        Related.objects.create(url=data['related'][i],art_id=kwargs['art_id'])
    return Response('')

@api_view(['DELETE'])
def delete_article(request,*args,**kwargs):
    Art.objects.filter(art_id=kwargs).delete()
    Img.objects.filter(art_id=kwargs).delete()
    Related.objects.filter(art_id=kwargs).delete()

@api_view(['UPDATE'])
def update_article(request,*args,**kwargs):
    data= request.data
    Art.objects.filter(art_id=kwargs).update(title=data['title'],content=data['content'],cover=data['cover'])
    Img.objects.filter(art_id=kwargs).delete()
    Related.objects.filter(art_id=kwargs).delete()
    for i in data['img_url']:
        Img.objects.create(art_id=kwargs,url=i)
    for r in data['rel_url']:
        Related.objects.create(art_id=kwargs,url=r)


        