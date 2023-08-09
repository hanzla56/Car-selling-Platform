from django.shortcuts import render , redirect # added manually
from .models import * 
from .forms import New_ad
from django.contrib.auth.decorators import login_required
# Create your views here.
# def home_page(request):
#     ads = Car.objects.all()
#     data = {'ads' : ads}
#     return render(request , 'Car_Platform/home.html' , context=data)

def home_page(request):
    ads = Car.objects.all()
    
    # Get the selected car model from query parameters
    car_model_id = request.GET.get('car_model')
    if car_model_id:
        ads = ads.filter(car_make_id=car_model_id)
    
    # Handle sorting based on selected options
    selected_options = request.GET.getlist('sort-option')
    sort_mapping = {
        'year_asc': 'date',
        
        'price_asc': 'price',
        'price_desc': '-price',
        'date_asc': 'date',
        'date_desc': '-date',
    }
    sort_criteria = [sort_mapping[option] for option in selected_options]
    ads = ads.order_by(*sort_criteria)

    car_models = Car_make.objects.all()

    context = {
        'ads': ads,
        'car_models': car_models,
    }
    return render(request, 'Car_Platform/home.html', context)

@login_required
def car_detail(request , ad_id):
    car = Car.objects.get(id=ad_id)
    context = {'car':car}
    return render(request , 'Car_Platform/detail_page.html' , context)


@login_required
def new_ad(request):
    if request.method == 'POST':
        ad_form = New_ad(request.POST , request.FILES)

        if ad_form.is_valid():
          ad_form.save()
          return redirect( 'Car_Platform:home_page')

    else:
        ad_form = New_ad()    

    context = {'ad_form' : ad_form}
    return render(request , 'Car_Platform/new_ad.html' , context)        

