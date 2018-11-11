from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    # return HttpResponse("Hello! This is Todo View Page...")
    all_todo_items=TodoItem.objects.all()
    return render(request, 'todo.html',
     {'all_items': all_todo_items})

def addTodo(request):
    #create new todoItem object
    c = request.POST['content']
    new_Item = TodoItem(content = c)
    #or new_Item = TodoItem(content = request.POST['content'])
    new_Item.save()

    #redirect browser to '/todo/'
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete=TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')