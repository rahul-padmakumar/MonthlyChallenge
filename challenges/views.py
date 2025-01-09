from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges_dict = {
    "jan": "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "December"
}

def monthly_challenge_view_int(request, month):
    month_list = list(monthly_challenges_dict.keys())
    if month < len(month_list):
        month_name = month_list[month - 1]
        redirect_path = reverse("monthlychallenge", args=[month_name])
        return HttpResponseRedirect(redirect_path)
    else: 
        return HttpResponseNotFound("Not supported number")
    

def monthly_challenge(request, month):
    month_name = monthly_challenges_dict[month]
    response = render_to_string("challenges/challenge.html")
    return HttpResponse(response)
    
    


def month_list(request):
    data = list(map(_map_month, list(monthly_challenges_dict.keys())))
    raw_response = "".join(data)
    respone = f"<ul>{raw_response}</ul>"
    return HttpResponse(respone)


def _map_month(value): 
    path = reverse("monthlychallenge", args=[value])
    return_value = f"<li><a href={path}>{monthly_challenges_dict[value]}</a></li>"
    return return_value