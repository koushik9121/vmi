from django.shortcuts import render
from django.http import HttpResponse
from .models import Index

# Create your views here.
def index(request):
	import sys
	print("Python version")
	print (sys.version)
	return render(request,'index.html')



def contact(request):
	return render(request,'contact.html')

def login_register(request):
	return render(request,'login-register.html')

def single_portfolio(request):
	return render(request,'single-portfolio.html')

def customer_review(request):
	return render(request,'customer-review.html')

def blog_details(request):
	return render(request,'index.html')

def shop(request):
	obj=Index.objects.get(id=1)
	if request.GET.get('vmi_opt'):
		opt=request.GET.get('vmi_opt')
		if opt=='nano':
			obj=Index.objects.get(id=2)
		elif opt=='newhondacity':
			obj=Index.objects.get(id=3)
		elif opt=='volkswagen':
			obj=Index.objects.get(id=4)
		elif opt=='hyundai':
			obj=Index.objects.get(id=5)
		elif opt=='skoda':
			obj=Index.objects.get(id=6)
		elif opt=='marutiswift':
			obj=Index.objects.get(id=7)				
		
		print('oapflsp:',opt)
	context={
		'vmi': obj.vmi_index,
		'coolant': obj.coolant_index,
		'oilfilter':obj.oilfilter_index,
		'sparkplug':obj.sparkplug_index,
		'engineoil':obj.engineoil_index,
		'airfilter':obj.airfilter_index,
		'tyre':obj.tyre_index,
		'brakefluid':obj.brakefluid_index,
		'battery':obj.battery_index,
		'fuelfilter':obj.fuelfilter_index,
	}	
		
	return render(request,'shop.html',context)
	
	

	"""
		
	clutchplate_index=models.DecimalField(decimal_places=2,max_digits=4)
    wheelalign_index=models.DecimalField(decimal_places=2,max_digits=4)
		#print('oapflsp:',opt)
		#vmi_f=model_vmi(opt)
		#print ('VMIIIIIII:',vmi_f)
		 vmi_index=models.DecimalField(decimal_places=2,max_digits=4)
    engineoil_index=models.DecimalField(decimal_places=2,max_digits=4)
    oilfilter_index=models.DecimalField(decimal_places=2,max_digits=4)
    sparkplug_index=models.DecimalField(decimal_places=2,max_digits=4)
    fuelfilter_index=models.DecimalField(decimal_places=2,max_digits=4)
    airfilter_index=models.DecimalField(decimal_places=2,max_digits=4)
    tyre_index=models.DecimalField(decimal_places=2,max_digits=4)
    brakefluid_index=models.DecimalField(decimal_places=2,max_digits=4)
    coolant_index=models.DecimalField(decimal_places=2,max_digits=4)
    battery_index=models.DecimalField(decimal_places=2,max_digits=3)
		
		return render(request,'vmi.html',{'vmi':vmi_f})"""
	
	