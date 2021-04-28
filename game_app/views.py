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
            # earn gold
            goldEarned = round(random.random() * 10 + 10)
            # add gold earned to mygold and save it
            myGold += goldEarned
            request.session = myGold
            #create str
            str = f"Earned {goldEarned} from {location}"
            # save str to sessions
            activities.append(str)
            request.session['activities'] = activities
    return redirect('/')