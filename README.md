
# Todo




## Installation

Install requirements with pip

```bash
  pip install -r requirements.txt
```

Run the server

```bash
    python manage.py runserver
```
    



## API Reference

#### Create Task

```http
  POST task/create/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | **Required**. Task Title |
| `description` | `string` | **Required**. Task Description |

#### Update Task

```http
  PUT task/update/<id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. Task Title |
| `description`      | `string` | **Required**. Task Description |
| `status`      | `string` | **Required**. Task Status |

#### Create Todo

```http
  POST todo/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title`   | `string` | **Required**. Task Title |
| `description` | `string` | **Required**. Task Description |

#### Get Todo

```http
  Get todo/
```

#### Update Todo

```http
  PUT task/update/<id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. Task Title |
| `description`      | `string` | **Required**. Task Description |
| `is_deleted`      | `bool` | **Required**. Soft delete |

#### Delete Todo

```http
  DELETE task/update/<id>/
```




## Another Simple Way to do CRUD in DRF

Using viewset in DRF

```bash
class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
```



    
