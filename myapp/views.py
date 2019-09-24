from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView,View
from django.views.generic import TemplateView
from django.utils import timezone
from .models import requestModel
from .forms import requestForm
# Create your views here.
def delivery_request(request):
    if request.method == 'POST':
        form_delivery = requestForm(request.POST)
        if form_delivery.is_valid():
            form_delivery.save()
            note = "Thanks for your request!! Wait a few minutes!! Car is on the way!!"
            new_form_delivery = requestForm()
        else:
            note = "failed.Try again!!"
        return render(request, 'delivery_form.html', {'deliveryform': new_form_delivery, 'note': note})
    else:
        form_delivery = requestForm()
        return render(request, 'delivery_form.html', {'deliveryform': form_delivery})

# def see(request,my_id):
#     obj= requestModel.objects.filter(id=my_id)
#     context={
#      'object':obj
#     }
#     return render(request,'delivery_detail_view.html',context)

def see(request,my_id):
	obj=get_object_or_404(requestModel,id=my_id)
	context={
	  "object":obj
	}
	return render(request,"delivery_detail_view.html",context)

def send(request, request_id, **kwargs):
    # import pdb;pdb.set_trace()
    model = get_object_or_404(requestModel, id=request_id)
    context = {
        'request':model
    }
    return render(request, 'driver_see.html', context)

