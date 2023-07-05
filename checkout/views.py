from django.shortcuts import render,redirect
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required
from .models import CheckOut
from datetime import datetime
from product.models import product
import io
# from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

# Create your views here.

@login_required(login_url='userlogin')
def CheckoutViews(request):
    
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        address = request.POST['address']
        product_qty = request.POST['product_qty']
        products_id = request.POST['products_id']
        username = request.POST['username']
        paymentid = request.POST['type']
        
        cart = request.session.get('cart', None)
        OrderPrice=0.0
        values= (list(cart.values()))
        for i in values:
            OrderPrice+=float(i['price'])*float(i['quantity'])

        data = CheckOut(first_name=fname,last_name=lname,checkout_email=email,address=address,product_qty=product_qty,products_id=products_id,username=username,Payment_status=paymentid,OrderPrice=OrderPrice)
        if data:
            if paymentid == "COD":
                data.Payment_status="Pending"
                data.Payment_type="COD"
                data.save()
                cart = request.session.get('cart', None)
                values= (list(cart.values()))
                for i in values:
                    productObj=product.objects.get(id=i['product_id'])
                    productObj.qty-=float(i['quantity'])
                    productObj.save()
                return render(request,"invoice.html",{"data":data})
            else:
                data.Payment_status="Paid" 
                data.Payment_type="Online"
                data.save()
                print("online")
                return redirect('Payment')
            
            

    return render(request,"checkout.html")



def Payment(request):
    return render(request,"Payment.html")


def invoice(request):
    data = datetime.now()
    total =0.00000
    cart = request.session.get('cart', None)
    values= (list(cart.values()))
    for i in values:
        total+=float(i['price'])*float(i['quantity'])
    context = {
        'total':total,
        'data':data
    }
    return render(request,"invoice.html",context)