# ToDoList_with_Django
장고를 활용한 ToDoList 페이지 제작 (백엔드 학습)

## Development Environment
- Apple Mac M1

## Learning Notes
### 0. 가상환경 구축
1. <code>python -m venv 가상환경명</code>
2. <code>source 가상환경명/bin/activate</code>
3. <code>python -m pip install --upgrade pip</code>
4. <code>pip install django</code>
### 1. 새 프로젝트 생성
- <code>django-admin startproject 프로젝트명</code>
- 하나의 프로젝트는 여러 개의 앱(app)으로 구성
### 2. 새 앱 생성(새 앱 생성할 때마다 INSTALLED_APPS에 꼭 추가해야 함)
- <code>python manage.py startapp 앱명</code>
- 프로젝트 경로(manage.py가 있는 위치)에서 위 명령어를 실행해야 함
- 프로젝트 경로 내부에 프로젝트명과 동일한 경로(e.g. ToDoList/ToDolist/)의 settings.py 파일의 INSTALLED_APPS 부분에 새로 생성한 앱을 추가
- <code>INSTALLED_APPS = ['my_to_do_app']</code>
### 3. 프로젝트 실행
- <code>python manage.py runserver</code>
- Access the site: http://127.0.0.1:8000/
### 4. 라우팅(URL 지정)
- URL을 지정하려면 urls.py 파일 수정해야 함(아래 코드 추가)
- <code>from django.urls import path, include</code>
- <code>path("", include("my_to_do_app.urls"))</code>
- 다음으로 my_to_do_app 앱 디렉터리 경로에 urls.py라는 새 파일을 만들고 다음과 같은 코드 추가
  <pre>
  from django.urls import path
  from . import views
    
  urlpatterns = [
    path("", views.index),
  ]
  </pre>
### 5. views.py 파일 수정
- 아래와 같이 views.py 파일에 index() 함수의 요청이 왔을 경우 "my_to_do_app first page."를 반환하는 index() 함수 만들기
  <pre>
  from django.shortcuts import render
  from django.http import HttpResponse # HttpResponse: 인자로 받은 문자열을 User에게 보여 주도록 하는 함수
  
  # Create your views here.
  def index(request):
      return HttpResponse("my_to_do_app first page.")
  </pre>
### 6. HTML 템플릿 사용
- 저자 GitHub의 index.html 파일 코드 복사
  - https://github.com/doorBW/ToDoList-with-Django/blob/master/ToDoList/my_to_do_app/templates/my_to_do_app/index.html
1) my_to_do_app 앱 경로에 templates 디렉터리를 생성
2) templates 안에 앱과 이름이 동일한 my_to_do_app 디렉터리 생성
3) my_to_do_app/templates/my_to_do_app에 index.html을 만들어 위에서 복사한 코드 붙여넣기
4) views.py의 index() 함수를 다음과 같이 수정
  <pre>
  from django.shortcuts import render
  
  def index(request):
      return render(request, "my_to_do_app/index.html")
  </pre>
- html 파일을 사용자에게 보여 주려면 render() 함수를 사용
- render() 함수에서 request 전달하는 이유: request가 user나 session과 같은 중요한 값들을 전달하기 때문
### 7. 모델(models.py) 다루기
1) models.py에 모델(≈DB에서의 테이블) 만들기
2) 모델(≈테이블)의 형태 정의하기
  <pre>
  from django.db import models
    
  # Create your models here.
  class Todo(models.Model):
      content = models.CharField(max_length = 255)
  </pre>
3) <code>python manage.py makemigrations</code>
4) <code>python manage.py migrate</code>
- 3)에서는 mirgration이라는 초안을 만들고 4)를 통해 실제 테이블 생성
- <img width="519" alt="스크린샷 2023-12-27 오후 5 18 24" src="https://github.com/PSLeon24/ToDoList_with_Django/assets/59058869/aa468e5b-1b3c-4b71-81a0-09774ca501a5">
- 1)<code>python manage.py dbshell</code> 2)<code>.tables</code> 3)<code>select * from my_to_do_app_todo;</code>를 순서대로 입력하여 테이블이 정상적인지 확인
- 모델의 데이터 형태에 대해 학습할 때 참고할 만한 자료
  - https://docs.djangoproject.com/en/2.2/ref/models/fields/#fields-types
  - https://github.com/dkyou7/TIL/blob/master/%ED%8C%8C%EC%9D%B4%EC%8D%AC/Django/5.%20%5BDjango%5D%20Model%20%ED%95%84%EB%93%9C%ED%83%80%EC%9E%85%20%EC%A0%95%EB%A6%AC.md
### 8. /createTodo 라우팅을 통해 데이터베이스에 데이터 저장하기(Create)
1) my_to_do_app 앱 내부 디렉터리에 urls.py 파일을 아래와 같이 수정 추가
<pre>
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("createTodo/", views.createTodo, name="createTodo"),
]
</pre>
- 이때, 각 path(경로)에 name을 준 것은 요청을 처리하고 페이지를 리다이렉트할 때 URL이 아닌 name으로 리다이렉트하기 위함
2) views.py 파일을 아래와 같이 수정
<pre>
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse # 페이지 되돌아가기 위해서
from .models import *

# Create your views here.
def index(request):
    return render(request, "my_to_do_app/index.html")
    
def createTodo(request):
    user_input_str = request.POST["todoContent"] # POST 값으로 요청된 값중에 name이 todoContent인 값을 변수에 할당
    new_todo = Todo(content=user_input_str) # 모델로부터 Todo 객체를 만듦(content 값은 위에서 만든 변수값을 통해 할당)
    new_todo.save() # 모델에 실제 데이터 저장(CRUD 중에서 Create 부분)
    return HttpResponseRedirect(reverse("index"))
</pre>
### 9. 데이터베이스에 기록된 데이터들을 보여주기(Read)
- views.py 파일의 index() 함수 부분을 아래와 같이 수정하기
<pre>
def index(request):
    todos = Todo.objects.all() # 모델로부터 전체 데이터를 가져옴(CRUD 중에서 Read 부분)
    content = {"todos": todos} # 템플릿에 전달할 데이터 정의
    return render(request, "my_to_do_app/index.html", content)
</pre>
1) Todo 모델의 objects에 접근하여 all() 함수를 통해 전체 데이터를 가져와 todos에 할당시킨다.
2) content라는 딕셔너리를 만들어 todos라는 key에 앞서 만든 todos를 value로 할당시킨다.
3) render() 함수에 content를 인자로 추가한다.
4) 저장된 데이터를 출력할 수 있도록 index.html을 수정한다.
  - {% %}: html 파일 내부에서 파이썬 문법을 사용할 수 있도록 하는 템플릿 태그
  - {{ }}: 위의 템플릿 태그와 유사하지만 사용자에게 직접 보여주는 값을 사용할 때 사용함
- <img width="800" alt="스크린샷 2023-12-29 오전 10 48 55" src="https://github.com/PSLeon24/ToDoList_with_Django/assets/59058869/e610795d-1110-4504-bf80-4256e8409ada">
### 10. 특정 Todo 완료 처리 - 특정 Todo 삭제(Delete)
1) index.html 파일에서 완료를 누르면 todo.id 값이 전달될 수 있도록 hidden 타입으로 todoNum이라는 name을 갖는 input 태그 추가
2) urls.py 파일에 <code>path("deleteTodo/", views.doneTodo, name="doneTodo")</code> 추가하기
3) views.py 파일에 다음과 같은 doneTodo() 함수 추가
<pre>
def doneTodo(request):
    done_todo_id = request.GET["todoNum"]
    todo = Todo.objects.get(id=done_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse("index"))
</pre>
- Logic
  1. GET 요청을 통해 전달된 todoNum 데이터를 done_todo_id 변수에 할당시킨다.
  2. Todo 모델의 objects에 접근하고 get() 함수를 통해서 id가 done_todo_id와 일치하는 값을 todo 변수에 할당시킨다.
  3. todo 변수에 담긴 데이터 자체에서 delete() 함수를 호출하여 해당 데이터를 삭제한다.
----
## 용어 정리
1) CRUD(Create, Read, Update, Delete)
  - Create: 데이터를 만드는 기능 (INSERT), POST 방식
  - Read: 데이터를 읽도록 하는 기능 (SELECT)
  - Update: 데이터를 갱신(수정)하도록 하는 기능(e.g., 웹 페이지의 글 수정 기능) (UPDATE)
  - Delete: 데이터베이스에서 특정 데이터를 삭제하는 기능(데이터베이스에서 유일하게 특정 데이터를 구별할 수 있는 기본키(PK) 값을 알아야 함) (DELETE), GET 방식
2) MVC(Model, View, Controller) 패턴
  - MVC 패턴: 사용자에게 보이는 UI(View)와 내부적으로 계산되는 비즈니스 로직(Controller)를 분리하여 개발하는 디자인 패턴
    - 화면과 로직의 결합의 느슨해지고 응집이 높아져 좋은 설계와 구현이 가능해짐(유지보수에 용이)
  - Model: 데이터에 대한 부분들로 일종의 Database ~ 장고의 models.py 파일
  - View: 사용자에게 보여지는 화면을 담당하는 일종의 UI ~ templates 디렉터리 내부의 html 파일들
  - Controller: 모델과 뷰 사이에서 Agent 역할을 하며 비즈니스 로직을 담당 ~ 장고의 views.py 파일
3) MTV(Model, Template, View) 패턴 - MVC와 매우 유사, 사실 django는 MVC보다는 MTV가 맞음
4) GET/POST

|GET|POST|
|--|--|
|주소 값에 전달되는 값이 표시됨|주소 값에 전달되는 값이 표시되지 않음|
|데이터가 보이므로 보안에 취약|데이터가 보이지 않으므로 보안에 우수|
|데이터가 주소 값에 표시되므로 길이 제한(256bytes)|데이터를 body안에 포함시켜 서버에 전달하므로 데이터 길이 제한이 없으며 복잡한 형태의 데이터도 전송 가능|
