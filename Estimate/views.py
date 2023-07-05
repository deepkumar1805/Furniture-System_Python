from django.shortcuts import render,redirect
from .forms import EstimateForm
from .models import Estimate
from django.db.models import Q 
from django.views.generic import ListView
# Create your views here.


def EstimateForms(request):
    data = EstimateForm(request.GET)
    return render(request,"Estimate.html",{'data':data})

def EstimateView(request):
    if request.method == "GET":
        apr_type = request.GET['apartment_type']
        bedroomes_type = request.GET['bedroomes_type']
        modular_kitchen = request.GET['modular_kitchen']
        Carpet_area_in_sqft = request.GET['Carpet_area_in_sqft']

        if apr_type == "2bhk" and bedroomes_type == "Master Room" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft)* 14
        elif apr_type == "2bhk" and bedroomes_type == "Home Office Study" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 26
        elif apr_type == "2bhk" and bedroomes_type == "Parents" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 50
        elif apr_type == "2bhk" and bedroomes_type == "Kids Bedroom" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 72
        elif apr_type == "2bhk" and bedroomes_type == "Kids Room 1" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 76
        elif apr_type == "2bhk" and bedroomes_type == "Kids Room 2" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 80
        elif apr_type == "2bhk" and bedroomes_type == "Guest Bedroom" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 86    
        elif apr_type == "2bhk" and bedroomes_type == "Master Room" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft)* 14
        elif apr_type == "2bhk" and bedroomes_type == "Home Office Study" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 26
        elif apr_type == "2bhk" and bedroomes_type == "Parents" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 50
        elif apr_type == "2bhk" and bedroomes_type == "Kids Bedroom" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 72
        elif apr_type == "2bhk" and bedroomes_type == "Kids Room 1" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 76
        elif apr_type == "2bhk" and bedroomes_type == "Kids Room 2" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 80
        elif apr_type == "2bhk" and bedroomes_type == "Guest Bedroom" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 86    


        elif apr_type == "3bhk" and bedroomes_type == "Master Room" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft)* 14
        elif apr_type == "3bhk" and bedroomes_type == "Home Office Study" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 26
        elif apr_type == "3bhk" and bedroomes_type == "Parents" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 50
        elif apr_type == "3bhk" and bedroomes_type == "Kids Bedroom" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 72
        elif apr_type == "3bhk" and bedroomes_type == "Kids Room 1" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 76
        elif apr_type == "3bhk" and bedroomes_type == "Kids Room 2" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 80
        elif apr_type == "3bhk" and bedroomes_type == "Guest Bedroom" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 86    
        elif apr_type == "3bhk" and bedroomes_type == "Master Room" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft)* 14
        elif apr_type == "3bhk" and bedroomes_type == "Home Office Study" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 26
        elif apr_type == "3bhk" and bedroomes_type == "Parents" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 50
        elif apr_type == "3bhk" and bedroomes_type == "Kids Bedroom" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 72
        elif apr_type == "3bhk" and bedroomes_type == "Kids Room 1" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 76
        elif apr_type == "3bhk" and bedroomes_type == "Kids Room 2" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 80
        elif apr_type == "3bhk" and bedroomes_type == "Guest Bedroom" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 86

        elif apr_type == "3.5bhk" and bedroomes_type == "Master Room" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft)* 14
        elif apr_type == "3.5bhk" and bedroomes_type == "Home Office Study" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 26
        elif apr_type == "3.5bhk" and bedroomes_type == "Parents" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 50
        elif apr_type == "3.5bhk" and bedroomes_type == "Kids Bedroom" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 72
        elif apr_type == "3.5bhk" and bedroomes_type == "Kids Room 1" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 76
        elif apr_type == "3.5bhk" and bedroomes_type == "Kids Room 2" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 80
        elif apr_type == "3.5bhk" and bedroomes_type == "Guest Bedroom" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 86    
        elif apr_type == "3.5bhk" and bedroomes_type == "Master Room" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft)* 14
        elif apr_type == "3.5bhk" and bedroomes_type == "Home Office Study" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 26
        elif apr_type == "3.5bhk" and bedroomes_type == "Parents" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 50
        elif apr_type == "3.5bhk" and bedroomes_type == "Kids Bedroom" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 72
        elif apr_type == "3.5bhk" and bedroomes_type == "Kids Room 1" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 76
        elif apr_type == "3.5bhk" and bedroomes_type == "Kids Room 2" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 80
        elif apr_type == "3.5bhk" and bedroomes_type == "Guest Bedroom" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 86        

        elif apr_type == "4bhk" and bedroomes_type == "Master Room" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft)* 14
        elif apr_type == "4bhk" and bedroomes_type == "Home Office Study" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 26
        elif apr_type == "4bhk" and bedroomes_type == "Parents" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 50
        elif apr_type == "4bhk" and bedroomes_type == "Kids Bedroom" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 72
        elif apr_type == "4bhk" and bedroomes_type == "Kids Room 1" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 76
        elif apr_type == "4bhk" and bedroomes_type == "Kids Room 2" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 80
        elif apr_type == "4bhk" and bedroomes_type == "Guest Bedroom" and modular_kitchen == "Yes":
            context = int(Carpet_area_in_sqft) * 86    
        elif apr_type == "4bhk" and bedroomes_type == "Master Room" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft)* 14
        elif apr_type == "4bhk" and bedroomes_type == "Home Office Study" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 26
        elif apr_type == "4bhk" and bedroomes_type == "Parents" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 50
        elif apr_type == "4bhk" and bedroomes_type == "Kids Bedroom" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 72
        elif apr_type == "4bhk" and bedroomes_type == "Kids Room 1" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 76
        elif apr_type == "4bhk" and bedroomes_type == "Kids Room 2" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 80
        elif apr_type == "4bhk" and bedroomes_type == "Guest Bedroom" and modular_kitchen == "No":
            context = int(Carpet_area_in_sqft) * 86    

    return render(request,"Estimateviews.html",{'context':context})