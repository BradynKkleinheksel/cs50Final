from django.http import HttpResponse
from django.shortcuts import render



# TODO havent created templates yet

data = {
    "picket": [
        {
            "id": 5,
            'title': "Jaws",
            'year': 1669,
        },
        {
            'id': 6,
            'title': 'Sharknado',
            'year': 1600,
        },
        {
            'id': 7,
            'title': 'The Meg',
            'year': 2000,
        }

    ]
}

def picket(request):
    return render(request, 'picket/picket.html', data) 

def home(request):
    return HttpResponse("___Home___Page___")