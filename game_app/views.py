from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    # set gold to 0 at start of session
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        # activities need to be appended to a list to track history
        request.session['activities'] = []
    # pass activities through context
    context = {
        'activities': request.session['activities']
    }
    return render(request,'index.html', context)


def process_money(request):
    if request.method == 'POST':
        # setup gold, activities, and location
        myGold = request.session['gold']
        activities = request.session['activities']
        location = request.POST['location'] # locations do not change  so POST is needed to grab whatever info comes from that location

        #create earnings for locations
        if location == 'farm':
            goldEarned = round(random.random() * 10 + 10)

        elif location == 'cave':
            goldEarned = round(random.random() * 5 + 5)

        elif location == 'house':
            goldEarned = round(random.random() * 3 + 2)

        else:
            winOrLose = round(random.random())
            if winOrLose == 1:
                goldEarned = round(random.random() * 50)
            else:
                goldEarned = (round(random.random() * 50)) * -1



    myGold += goldEarned
    request.session['gold'] = myGold
    time = datetime.now()
    time_str = time.strftime("%d/%m/%Y %I:%M %p")
    
    if goldEarned >= 0:
        str = f"Earned {goldEarned} gold from the {location} {time_str}"
    else:
        goldEarned *= -1
        str = f"Lost {goldEarned} gold from the {location} {time_str}"

    activities.append(str)
    request.session['activities'] = activities
    
    
    
    return redirect('/')