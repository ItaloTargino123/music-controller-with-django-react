from django.shortcuts import render

# Create your views here.
# Going to render the index template and let react take over


def index(request, *args, **kwargs):
    return render(request, "frontend/index.html")
