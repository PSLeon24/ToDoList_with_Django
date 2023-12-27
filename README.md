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
- 모델의 데이터 형태에 대해 학습할 때 참고할 만한 자료: https://github.com/dkyou7/TIL/blob/master/%ED%8C%8C%EC%9D%B4%EC%8D%AC/Django/5.%20%5BDjango%5D%20Model%20%ED%95%84%EB%93%9C%ED%83%80%EC%9E%85%20%EC%A0%95%EB%A6%AC.md
