from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import random
from models import Ushort

RNG = int('ffff',16)   #range of short url to be used                                

def index(request,templt='form.html'):
    """
    this is the function which is called on the base url
    """
    return render_to_response(templt,context_instance=RequestContext(request))

def search_assign(request,templt='output.html'):
    """
    this is the main function  which assigns short urls .
    it is called when the valid long url is post by the user ,
    this function checks if the long url is already shortned, 
    if not it just creates a short url, store it and returns
    it to the user
    """ 
    if request.method=='POST':
        data = request.POST.copy()
        longu = data.get('lurl')
        contxt = {}
        try:
           #here it checks if the long url is already shortned
           isthere = Ushort.objects.get(longurl=longu)
           contxt['shortu'] = isthere
           return render_to_response(templt,contxt,context_instance=RequestContext(request))
        except:
           #here the code makes and assigns shortned url  
           newobj = Ushort()
           newobj.longurl = longu
           newobj.shorturl = hex(random.randrange(0,RNG,3))[2:]
           newobj.save()
           contxt['shortu'] = newobj
           return render_to_response(templt,contxt,context_instance=RequestContext(request))
    return render_to_response('shortt.html',{},context_instance=RequestContext(request))

def goto(request, shortt):
    """this function redirects the  valid short urls to desired urls
     and wrong ones to 404 
    """
    isthere = get_object_or_404(Ushort,shorturl=shortt)
    yas = isthere.longurl
    return HttpResponseRedirect(yas)
    
    
    
    
    
    
    
