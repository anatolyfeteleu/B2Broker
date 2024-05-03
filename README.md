# README
---

## 1. First Steps
1. Create a file (name it as follows `.env`) in the root directory based on `.env.sample`
2. Create and run MySQL container  
```
  docker run --name local-mysql -e MYSQL_ROOT_PASSWORD=mysql -d -p 3306:3306 mysql
```
3. Create database `local` in MySQL
4. Apply migrations `./manage.py migrate`
5. Run local server `./manage.py runserver`  

_Optional:_  
6. Create superuser `./manage.py createsuperuser`

## 2. Endpoints
- `GET  api/core/wallet/`
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/core/wallet/' \
  -H 'accept: application/json'
```

- `GET api/core/transactions/`
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/core/transactions/' \
  -H 'accept: application/json'
```

## 3. Project Structure
```
.
├── README.md
├── apps
│   ├── __init__.py
│   └── core
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── filters.py
│       ├── migrations
│       │   ├── 0001_initial.py
│       │   ├── __init__.py
│       ├── models.py
│       ├── serializers.py
│       ├── tests
│       │   ├── __init__.py
│       │   ├── factories.py
│       │   ├── fixtures.py
│       │   └── test_api.py
│       ├── urls.py
│       └── views.py
├── conftest.py
├── manage.py
├── poetry.lock
├── project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings
│   │   ├── __init__.py
│   ├── urls
│   │   ├── __init__.py
│   │   └── api.py
│   └── wsgi.py
├── pyproject.toml
└── pytest.ini
```
