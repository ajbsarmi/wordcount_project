from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'name':'Arden'})

def eggs1(request):
    return HttpResponse('<h1>Hi, Eggs!!!</h1>')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # Increase
            worddictionary[word] += 1
        else: 
            # Add to the dictionary
            worddictionary[word] = 1

    sortedWords = sorted(worddictionary.items(),key=operator.itemgetter(1), reverse=True)

    return  render(request,'count.html', {'fulltext':fulltext,'count':len(wordlist),'sortedWords':sortedWords})

def about(request):
    return render(request, 'about.html')
