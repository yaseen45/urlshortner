from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import random
from models import Ushort

RNG = int('ffff',16)   #range of short url to be used                                

def index(request,templt='form.html'):
    """render the home page of urlshortner"""
    return render_to_response(templt,context_instance=RequestContext(request))

def search_assign(request,templt='output.html'):
    """main function of urlshortner which assigns short urls.

       The user posts the long url if that url is already shortned
       then the short key is retrieved from the database which is
       returned to the user otherwise a new short url is created,
       returned and stored in the database. 

    Args:
         post copy of long url.
    Redirects:
         output.html:if the request method is POST.
         shortt.html: if requet method is other than POST.         


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
    """redirects valid short urls to corresponding long urls.

    Args:
        shortt:the key enterd by the user.
    Redirects:
        yas: longurl of the valid key,
        404: for invalid key      
    """
    isthere = get_object_or_404(Ushort,shorturl=shortt)
    yas = isthere.longurl
    return HttpResponseRedirect(yas)
    
    
    
    
    
    
    
