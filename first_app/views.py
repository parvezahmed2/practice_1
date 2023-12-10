from django.shortcuts import render
import datetime
# Create your views here.


def about(request):
    d ={ 'first_name': 'parvez', 'last_name': 'ahmed', 'text': "i'm jashim", 'text2': 'best Off luck', 'birthday':datetime.datetime.now(), 'text3':'', 'employe':[
        {
            'name': 'parvez',
            'salary': '2000'
         },
        {
            'name': 'fahim',
            'salary': '3000'
         },
        {
            'name': 'akram',
            'salary': '2500'
         }],
         'number': 6,
         'country': 'Bangladesh',
         'lst': ['s', 't', 'u', 'v', 'w']
    
    }
    return render(request, 'first_app/about.html', d)
def contact(request):
    return render(request, 'first_app/contact.html')