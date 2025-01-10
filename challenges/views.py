from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    return render(request, "challenges/challenge.html", {"month_key": month_name,"month_code": month})
    
def month_list(request):
    data = list(monthly_challenges_dict.keys())
    return render(request, "challenges/index.html", {"months": data})