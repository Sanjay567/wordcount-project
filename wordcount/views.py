from django.http import HttpResponse
from django.shortcuts import render
import operator

#def homepage(request):
#    return HttpResponse('Hello')

def homepage(request):
    #return render(request, 'home.html', {'hithere':'how are you'}) #This is done when we use templates and dict is used
    return render( request, 'home.html' )

def count(request):
    text = request.GET['text_entered']
    words = text.split()
    worddict = {}
    for word in words:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word] = 1
    sorteddict = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render( request, 'count.html', {'fulltext':text, 'count':len(words), 'worddict':sorteddict } )

def about(request):
    return render( request, 'about.html' )
