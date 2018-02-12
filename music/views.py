
from django.http import HttpResponse , Http404
from django.shortcuts import render , get_object_or_404


from models import Album

#from django.template import loader




# Create your views here.

def fn_index(request):
    
    all_albums = Album.objects.all()
    
    
    context = {
        'all_albums' : all_albums,
    }
    
    #template = loader.get_template('music/index.html')
    #return HttpResponse(template.render(context,request))
    
    return render(request,'music/index.html',context)





def fn_detail(request,album_id):
    
    '''
    try:
        album = Album.objects.get(pk=album_id)
        context = { 'album' : album, }
            
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    
    return HttpResponse("<h2>Details for Album : " + str(album_id) +"</h2>")
    '''
    
    album = get_object_or_404(Album, pk = album_id)
    context = { 'album' : album, }
    
    return render(request,'music/detail.html',context)

