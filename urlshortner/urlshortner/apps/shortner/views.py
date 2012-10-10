from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import random
from models import Ushort

RNG = int('ffff',16)   #range of value to be used                                

def index(request,templt='form.html'):
    return render_to_response(templt,context_instance=RequestContext(request))

def search_assign(request,templt='output.html'):
    if request.method=='POST':
        data = request.POST.copy()
        longu = data.get('lurl')
        contxt = {}
        try:
           isthere = Ushort.objects.get(longurl=longu)
           contxt['shortu'] = isthere
           return render_to_response(templt,contxt,context_instance=RequestContext(request))
        except:
           newobj = Ushort()
           newobj.longurl = longu
           newobj.shorturl = hex(random.randrange(0,RNG,3))[2:]
           newobj.save()
           contxt['shortu'] = newobj
           return render_to_response(templt,contxt,context_instance=RequestContext(request))
    return render_to_response('shortt.html',{},context_instance=RequestContext(request))

def goto(request, shortt):
    isthere = get_object_or_404(Ushort,shorturl=shortt)
    yas = isthere.longurl
    return HttpResponseRedirect(yas)
    
    
    
    
    
    
    
