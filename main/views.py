from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165912',
        'name': 'Widya Mutia Ichsan',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

# Create your views here.
