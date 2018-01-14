# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .forms import SearchParamsForm
from .models import SearchParams
import numpy as np
import csv
import os

def findonfile(name, depdate, retdate, maxmiles):
    depdatecol = -1
    retdatecol = -1
    rawdata = np.loadtxt(open('/home/jonas/Desktop/pointsearchcodes/SearchCode/datasets/'+name, "rb"), delimiter=" ", skiprows=0)
    print("run name: " + name)
    for col in range(0,np.shape(rawdata)[1]):
        currposdate = str(int(rawdata[0][col])).zfill(8)
        if currposdate == depdate:
            depdatecol = col-1
        if currposdate == retdate:
            retdatecol = col
    if ((depdatecol < 0) or (retdatecol < 0)):
        return("0")
    else:
        milesfordat = rawdata[depdatecol][retdatecol]
        namedoll = name[0:7]+'d'+name[8:]
        rawdatausd = np.loadtxt(open('/home/jonas/Desktop/pointsearchcodes/SearchCode/datasets/'+namedoll, "rb"), delimiter=" ", skiprows=0)
        dollafordat = rawdatausd[depdatecol][retdatecol]
        if ((milesfordat < float(maxmiles)) and (milesfordat > 0)):
            return ("fly " + name[0:3] + " to " + name[3:6] + " for " + str(int(milesfordat)) + " miles and $" + str(dollafordat)) + " "
    return('0')




def results(inputdata):
    return HttpResponse(inputdata)

#fields = ['origin','destination','depdate','retdate','flexdates','ariline','maxnummiles']
def searchform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchParamsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            ori = str(data['origin'])
            des = str(data['destination'])
            ddt = str(data['depdate'])
            rdt = str(data['retdate'])
            maxmiles = str(data['maxnumofmiles'])

            # ori and des are okay, need to rewrite detdate and retdate -.-
            depdate = ddt[5:7] + ddt[8:] + ddt[0:4] #raw_input('departure date (mmddyyyy):')
            retdate = rdt[5:7] + rdt[8:] + rdt[0:4] #raw_input('return date (mmddyyyy):')

            #strngres = ori + ' ' + des + ' ' + depdate + ' ' + retdate + ' ' + maxmiles
            #return HttpResponse(strngres)

            if des == 'North America':
                #algoritmo de busqueda total
                dests = []
                for (root, dirs, files) in os.walk('/home/jonas/Desktop/pythontests/datasearchalgorithm/datasets/'):
                    # SO this worked well and found the files... ugh -.-
                    counter = 0
                    for name in files:
                        if ((name[0:3] == ori[0:3]) and (name[7] == 'm')):
                            counter +=1
                            listofresults = findonfile(name, depdate, retdate, maxmiles)
                            if listofresults != '0':
                                dests.append(listofresults)
                if dests == "":
                    return HttpResponse("Sorry mate, try other dates, like Feb")
                #output1 = "Found " + str(counter) + ' ocurrencies for ' + ori[0:3] + ' to ' + dests + ' but I didnt check the cost of each yet'
                #return HttpResponse("Analysed " + str(counter) + ' possible itineraries: ' + dests)
                
                return render(request, 'findr/printresults.html', {'strlist': ["Analysed " + str(counter) + ' possible itineraries:']+dests})
                # KOWL!!! make it noice!!


            else:
                # just tryna load the file and withdraw data
                name = ori+des+'_m.csv'
                listofresults = findonfile(name, depdate, retdate, maxmiles)
                if listofresults != '0':
                    return render(request, 'findr/printresults.html', {'strlist': [listofresults]})
                else:
                    return HttpResponse("Sorry mate, try other dates, like Feb")
                    #return HttpResponse('Fly ' + name[0:6] + ': miles = ' + str(milesfordat) + ' + ' + str(dollafordat) + '$')



            
            #return HttpResponseRedirect(reverse('findr:results', args=(strngres,)))
        else:
            return HttpResponse("Oops something didnt quite work")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchParamsForm()
        return render(request, 'findr/searchform.html', {'form': form})
