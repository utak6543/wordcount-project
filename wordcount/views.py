from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html',{'hithere': 'its me'})
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    if len(wordlist)==0 :
        return HttpResponse("please enter words !!")
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else :
            worddictionary[word] = 1
            sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=False)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist),'worddictionary': sortedwords})
def about(request):
    return render(request,'about.html')
