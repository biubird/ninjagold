from django.shortcuts import render, redirect
import random
from datetime import datetime
#from time import strptime

def index(request):
    print request.method
    print ("*"*100)
    request.session['count'] = 0
    request.session['activities'] = []
    return render(request, 'ninjagold/index.html')

def process_money(request):
    print request.method
    if request.method == "POST":
        print (request.POST)
        print ('5'*50)
#        now = datetime.now()
        time = datetime.now()

#    num = {
#        'farm': random.randrange(10, 21),
#        'cave': random.randrange(5, 11),
#        'house': random.randrange(2, 6),
#        'casino': random.randrange(-50, 51)
#    }
    if request.POST['locationkey'] == 'farm':
        print 'farm'
        num = random.randrange(10, 21)
        activity = {
            'activity': "You have entered the {} and earned {} golds!".format(request.POST['locationkey'], num),
            'class': 'win',
            'date': time
            }
    elif request.POST['locationkey'] == 'cave':
        print 'cave'
        num = random.randrange(5, 11)
        activity = {
            'activity': "You have entered the {} and earned {} golds!".format(request.POST['locationkey'], num),
            'class': 'win',
            'date': time
            }
    elif request.POST['locationkey'] == 'house':
        print 'house'
        num = random.randrange(2, 6)
        activity = {
            'activity': "You have entered the {} and earned {} golds!".format(request.POST['locationkey'], num),
            'class': 'win',
            'date': time
        }
    elif request.POST['locationkey'] == 'casino':
        print 'casino'
        num = random.randrange(-50, 51)
        if num < 0:
           num = abs(num)
           activity = {
                'activity': "You have entered the {} and LOST {} golds!".format(request.POST['locationkey'], num),
                'class': 'loss',
                'date': time
            }
        else:
            activity = {
                'activity': "You have entered the {} and WON {} golds!".format(request.POST['locationkey'], num),
                'class': 'win',
                'date': time
            }
    else:
        print ("You better play again!!")
    request.session['count'] += num
    request.session['activities'].append(activity)
    return render(request, 'ninjagold/index.html')
