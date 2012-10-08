from django.http import HttpResponse,HttpResponseRedirect
from models import ushort
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import random

rng=int('fff',16)
def index(request,templt='form.html'):
    return render_to_response(templt,context_instance = RequestContext( request ))

def search_assign(request,templt='output.html'):
    if request.method=='POST':
        data=request.POST.copy()

        longu=data.get('lurl')
        contxt={}
        try:
           isthere=ushort.objects.get(longurl=longu)
           contxt['shortu']=isthere
           return render_to_response(templt,contxt,context_instance=RequestContext(request))
        except:
           newobj=ushort()
           newobj.longurl=longu
           newobj.shorturl=hex(random.randrange(0,rng,3))[2:]
           newobj.save()
           contxt['shortu']=newobj
           return render_to_response(templt,contxt,context_instance=RequestContext(request))

      
    return render_to_response('shortt.html',{},context_instance = RequestContext( request ))

def goto(request, shortt):
      #isthere=ushort.objects.get(shorturl=shortt)
     isthere=get_object_or_404(ushort,shorturl=shortt)
     yas=isthere.longurl
     # print yas
     return HttpResponseRedirect(yas)
    
    
    
    
    
    
    
