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
    ├── blog_posts
    │   ├── __init__.py
    │   ├── forms.py
    │   └── views.py
    ├── core
    │   ├── __init__.py
    │   └── views.py
    ├── error_pages
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
