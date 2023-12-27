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
<code>django-admin startproject 프로젝트명</code>
- 하나의 프로젝트는 여러 개의 앱(app)으로 구성
### 2. 새 앱 생성
<code>python manage.py startapp 앱명</code>
- 프로젝트 경로(manage.py가 있는 위치)에서 위 명령어를 실행해야 함
