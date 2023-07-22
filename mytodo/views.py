import random
import requests
from django.shortcuts import render
from .models import Todo

def fetch_todos(request, n):
    todos = []
    for _ in range(n):
        todo_id = random.randint(1, 100)
        response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{todo_id}')
        if response.ok:
            data = response.json()
            todos.append(data)
    return todos

def display_todos(request):
    if request.method == 'POST':
        n = int(request.POST['n'])
        todos = fetch_todos(request, n)
        # Sort the todos based on 'completed' and 'title'
        todos.sort(key=lambda x: (x['completed'], x['title']))
        return render(request, 'todo.html', {'todos': todos})
    return render(request, 'todo.html')