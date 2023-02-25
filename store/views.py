from django.shortcuts import render

# Create your views here.

#############################################
# Start views Store
#############################################


def store(request):
    context = {


    }
    return render(request, 'store/store.html', context)


#############################################
# Start views Cart
#############################################


def cart(request):
    context = {


    }
    return render(request, 'store/cart.html', context)

#############################################
# Start views Checkout
#############################################


def checkout(request):
    context = {


    }
    return render(request, 'store/checkout.html', context)
