from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    sentence=fulltext.split()
    wordcount={}
    for word in sentence:
        if word in wordcount:
            wordcount[word]+=1
        else:
            wordcount[word]=1
    return render(request,'count.html',{'fulltext':fulltext,'count':len(sentence),'wordcount':wordcount})
def about(request):
    return render(request,'about.html')
