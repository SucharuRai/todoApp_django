from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Name


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getAll(request):
    response = []
    names = Name.objects.order_by("-pub_date")

    for name in names:
        response.append({
            'id': name.id,
            'name': name.todo_name,
            'status': name.status
        })

    return JsonResponse(response, safe=False)

@csrf_exempt
def createTodo(request):
    if request.method == 'POST':
        todo = Name()
        todo.todo_name = request.POST.get("name")
        todo.save()
        return HttpResponse("Created Todo successfully")
    
    else:
        return HttpResponse("Only POST request supported")