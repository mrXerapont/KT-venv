#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Snd
from .forms import SndForm

from .serializers import SndSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView




class SndCreateView(CreateView):
    template_name = 'sender/create.html'
    form_class = SndForm
    success_url = reverse_lazy('index')


#class SndListCreate(generics.ListCreateAPIView):
class SndAPICreateView(CreateAPIView, ListAPIView):
    queryset = Snd.objects.all()
    serializer_class = SndSerializer

class SingleSndAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Snd.objects.all()
    serializer_class = SndSerializer
    
#    def get(self, request, *args, **kwargs):
#        return self.list(request, *args, **kwargs)
#    
#    def post(self, request, *args, **kwargs):
#        return self.create(request, *args, **kwargs)


def edit(request, pk):
    post = get_object_or_404(Snd, pk=pk)
    if request.method == "POST":        
        form = SndForm(request.POST, instance=post)
        #if request.POST.get('delete'):
         #   
          #  post.delete()
        if form.is_valid():
            post = form.save(commit=False)
            print(post)
            post.save()
            snds = Snd.objects.all()
            context = {'snds': snds}
            return render(request, 'sender/index.html', context)
    else:                
        form = SndForm(instance=post)
    return render(request, 'sender/edit.html', {'form': form})

def delete(request, pk):
    snd = get_object_or_404(Snd, pk=pk)
    snd.delete()
    snds = Snd.objects.all()
    context = {'snds': snds}
    return render(request, 'sender/index.html', context)    




def index(request):
    #s = 'Список заданий\r\n\r\n\r\n'    
   # template = loader.get_template('sender/index.html')
    snds = Snd.objects.all()
    context = {'snds': snds}
    
    #for snd in Snd.objects.order_by('dtime'):
     #   s += snd.description + '\r\n' + snd.mailto + '\r\n' + snd.text + '\r\n' + str(snd.dtime) + '\r\n\r\n'
    #return HttpResponse(s, content_type='text/plain; charset=utf-8')
   # return HttpResponse(template.render(context, request))
    return render(request, 'sender/index.html', context)
