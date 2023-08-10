from django import forms
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from accounts.forms import CreateUserForm, VenueImagesForm, venueRegistrationForm
from accounts.models import Account, UpdateSubscription, VenueImages, is_verified

from django.forms import modelformset_factory
from django.views.decorators.csrf import csrf_exempt

from booking.views import is_ajax

# Create your views here.   
def registerAsUser(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        # return redirect ('home:index')
        print("authenticated")
    else:
        if request.method == 'POST':
            SubStatus = request.POST.get('SubStatus')
            userName = request.POST.get('username')

            form = CreateUserForm(request.POST)

            if form.is_valid():
                print("form is valid")
                form.save()
                print("User Registered")
                
                if SubStatus=="on":
                    status = True
                    print("User has agreed to subscribe")

                    userName = User.objects.get(username=userName)

                    saveSub = UpdateSubscription(user=userName, status=status)
                    saveSub.save()
                else:
                    print("User has not agreed to subscribe")
                    
                return redirect('accounts:success') 
            else:
                context ={
                    'form':form
                }
                return render(request, 'accounts/register.html',context)



              
        else:
            form = CreateUserForm()

    context ={
        'form':form
    }
    return render(request, 'accounts/register.html',context)

def success(request): 
    return render(request, "accounts/success.htm")

@csrf_exempt
def loginAsUser(request):
    if request.user.is_authenticated:
        return redirect ('home:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username, password=password)

            if username and password !="":
                if user is not None:
                    login(request,user)
                    return redirect('home:index')

                else:
                    print('Username or password is incorrect')
            else:
                print('Enter Username or password is incorrect')

    return render(request, "accounts/login.html")


def logoutUser(request):
    logout(request)
    return redirect('home:index')


def registerAsVenue(request):
    form = venueRegistrationForm()
    venueImagesformset = modelformset_factory(VenueImages,
                                        form=VenueImagesForm,extra=4)

    if request.method == "POST":
        form = venueRegistrationForm(request.POST, request.FILES)
        # files = request.FILES.getlist("image")
        venueImages = venueImagesformset(request.POST, request.FILES, queryset=VenueImages.objects.none())
        
        if form.is_valid() and venueImages.is_valid():
            f= form.save()
            f.user = request.user
            f.save()

            is_verified.objects.create(user=request.user, venue_account=f, verified=False)
            
            for imageForm in venueImages.cleaned_data:
                if imageForm:
                    image = imageForm['image']
                    photo = VenueImages(venue_account=f, image=image)
                    photo.save()
                else:
                    raise forms.ValidationError("Add Photos")

            return redirect("accounts:venueRegistrationSubmitted")
        else:
            return render(request,'accounts/venueregistration.html', {
        'form':form,
        'venueImages':venueImages,
        })
        
    context ={
        'form':form,
        'venueImages': venueImagesformset(queryset=VenueImages.objects.none()),
        }

    return render(request,'accounts/venueregistration.html', context)

def venueRegistrationSubmitted(request):
    return render(request, 'accounts/venueregistration_submitted.html')
        
def UserProfile(request):
    userprf = False
    try:
        userInfo = Account.objects.get(user=request.user)
        userprf = True
    except Account.DoesNotExist:
        userInfo = None

    context = {
        'userInfo':userInfo,
        'userprf':userprf,
    }
    return render(request, 'accounts/user_profile.html',context)

def AddUserInfo(request):
    if is_ajax(request=request):
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        print(dob,address,phone,gender)

        f = Account.objects.create(user=request.user, dob=dob, phone=phone, address=address, gender=gender)
        f.save()
        
        return JsonResponse("Success",safe=False)

def UpdateUserInfo(request):
    if is_ajax(request=request):
        print("Updating")
        userInfo = Account.objects.get(user=request.user)

        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        print(dob,address,phone,gender)

        updateStatus = False

        userInfo.dob=dob 
        userInfo.phone=phone
        userInfo.address=address
        userInfo.gender = gender

        userInfo.save()

        updateStatus=True

        return JsonResponse(updateStatus,safe=False)