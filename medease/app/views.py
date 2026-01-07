from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Medicine, Cart, Address
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Medicine,LabTest
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
         # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken! Please choose another.')
            return render(request, 'register.html')

        # Create new user
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully! You can now log in.')
        return redirect('login')

    return render(request, 'register.html')


def loginusr(request):
      if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
      return render(request, 'login.html')


def logoutusr(request):
    logout(request)
    return redirect('login') 



def address(request): 
    if request.method == "POST":
        request.session['address_added'] = True
        return redirect('home')
    return render(request, 'address.html')



def global_search(request):
    query = request.GET.get('q')

    if not query:
        return redirect('home')

    # Check if any medicine matches
    if Medicine.objects.filter(name__icontains=query).exists():
        return redirect(f"/healthcare/?q={query}")

    # Check if any lab test matches
    if LabTest.objects.filter(name__icontains=query).exists():
        return redirect(f"/lab-tests/?q={query}")

    # Default: redirect to healthcare
    return redirect(f"/healthcare/?q={query}")


# Medicine Listing
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})

# Medicine Details & Add to Cart
@login_required
def medicine_detail(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item, created = Cart.objects.get_or_create(user=request.user, medicine=medicine)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
        return redirect('cart')
    
    return render(request, 'medicine_detail.html', {'medicine': medicine})



def lab_tests(request):
    tests = LabTest.objects.all()
    return render(request, 'lab_tests.html', {'lab_tests': tests})



def lab_test_detail(request, id):
    lab_test = get_object_or_404(LabTest, id=id)
    return render(request, 'lab_test_detail.html', {'lab_test': lab_test})



# Cart Page
@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    
    # Update quantity or remove item if needed (optional)
    if request.method == 'POST':
        for item in cart_items:
            qty = request.POST.get(f'quantity_{item.id}')
            if qty:
                qty = int(qty)
                if qty <= 0:
                    item.delete()
                else:
                    item.quantity = qty
                    item.save()
        return redirect('cart')
    
    # Prepare row totals
    cart_with_totals = []
    total = 0
    for item in cart_items:
        row_total = item.medicine.price * item.quantity
        cart_with_totals.append({
            'item': item,
            'row_total': row_total
        })
        total += row_total

    return render(request, 'cart.html', {'cart_items': cart_with_totals, 'total': total})

# Doctor Page
def doctor(request):
    return render(request, 'doctor.html')

# Lab Tests Page
def lab_tests(request):
    query = request.GET.get('q')

    if query:
        tests = LabTest.objects.filter(name__icontains=query)
    else:
        tests = LabTest.objects.all()

    return render(request, 'lab_tests.html', {'lab_tests': tests})


def address_upload_page(request):
    # Page with Add Address & Upload buttons
    return render(request, 'prescription.html')

def healthcare(request):
    query = request.GET.get('q')

    if query:
        medicines = Medicine.objects.filter(name__icontains=query)
    else:
        medicines = Medicine.objects.all()

    return render(request, 'healthcare.html', {'medicines': medicines})



def add_address(request):
    return HttpResponse("Add Address Page")



def offer_page(request):
    offer = {
        "title": "Scratch & Get Flat ₹100",
        "description": "Get flat ₹100 cashback on your first-ever medicine purchase using MobiKwik wallet.",
        "details": [
            "Valid on first transaction only",
            "Minimum order value ₹499",
            "Offer applicable via MobiKwik payments",
            "Cashback credited within 24 hours"
        ]
    }
    return render(request, 'offer.html', {"offer": offer})