
from django.http import HttpResponse , Http404
from django.shortcuts import render , get_object_or_404


from models import Stock

#from django.template import loader




# Create your views here.
def fn_index(request):
    
    all_stocks = Stock.objects.all()
    
    
    context = {
        'all_stocks' : all_stocks,
    }
    
    #template = loader.get_template('music/index.html')
    #return HttpResponse(template.render(context,request))
    #return HttpResponse("Welcome Company Page")
    
    return render(request,'company/index.html',context)


