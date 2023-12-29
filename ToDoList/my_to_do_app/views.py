from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.
def index(request):
    todos = Todo.objects.all()  # 모델로부터 전체 데이터를 가져옴(CRUD 중에서 Read 부분)
    content = {"todos": todos}  # 템플릿에 전달할 데이터 정의
    return render(request, "my_to_do_app/index.html", content)


def createTodo(request):
    user_input_str = request.POST[
        "todoContent"
    ]  # POST 값으로 요청된 값중에 name이 todoContent인 값을 변수에 할당
    new_todo = Todo(
        content=user_input_str
    )  # 모델로부터 Todo 객체를 만듦(content 값은 위에서 만든 변수값을 통해 할당)
    new_todo.save()  # 모델에 실제 데이터 저장(CRUD 중에서 Create 부분)
    return HttpResponseRedirect(reverse("index"))


def doneTodo(request):
    done_todo_id = request.GET["todoNum"]
    todo = Todo.objects.get(id=done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse("index"))
