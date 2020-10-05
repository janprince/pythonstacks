from django.shortcuts import render


# Index view
def index(request):
    context = {}
    return render(request, 'blog/index.html', context)



def detail(request):
    pass