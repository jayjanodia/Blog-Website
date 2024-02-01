# General organization of the project

## Views

### Core

- Index
- Info

### Users

- Register
- Login
- Logout
- Account
- User Posts

### Blog Posts

- Create
- Read
- Update
- Delete

## Models

### Users

- id
- profile image
- email
- username
- password (hashed)
- posts

### Blogs

- id
- user_id
- date
- title
- description

## Tree Structure

```shell
.
├── README.md
├── app.py
└── website
    ├── __init__.py
    ├── __pycache__
    │   └── __init__.cpython-311.pyc
    ├── blog_posts
    │   ├── __init__.py
    │   ├── forms.py
    │   └── views.py
    ├── core
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-311.pyc
    │   │   └── views.cpython-311.pyc
    │   └── views.py
    ├── error_pages
    │   ├── __pycache__
    │   │   └── handlers.cpython-311.pyc
    │   └── handlers.py
    ├── models.py
    ├── static
    ├── templates
    │   ├── about.html
    │   ├── base.html
    │   ├── error_pages
    │   │   ├── 403.html
    │   │   └── 404.html
    │   └── index.html
    └── users
        ├── __init__.py
        ├── forms.py
        └── views.py
```
