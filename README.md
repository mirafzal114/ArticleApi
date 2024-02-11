# Article API

This API provides endpoints for managing articles, tags, and comments.

## Installation

1. Clone the repository:

```git clone https://github.com/mirafzal114/ArticleApi
  cd ArticleApi
```

2. Install the dependencies:
```pip install -r requirements.txt
```
3. Apply migrations:
```
python manage.py migrate
```

3. Run the development server:

```
python manage.py runserver
```


## Usage

### Endpoints

- **GET /articles/**: Retrieve a list of all articles.
- **POST /articles/**: Create a new article.
- **GET /articles/{id}/**: Retrieve a specific article by ID.
- **PUT /articles/{id}/**: Update a specific article by ID.
- **DELETE /articles/{id}/**: Delete a specific article by ID.
- **GET /tags/**: Retrieve a list of all tags.
- **POST /tags/**: Create a new tag.
- **GET /comments/**: Retrieve a list of all comments.
- **POST /comments/**: Create a new comment.

### Authentication

This API uses token-based authentication. To access protected endpoints, include an `Authorization` header with a token obtained by authenticating with the API.

### Example Requests

1. Get a list of all articles:

```http
GET /articles/

```

#Create a new article:
```JSON
POST /articles/
Content-Type: application/json

{
    "title": "New Article",
    "content": "This is the content of the new article.",
    "author": 1,
    "tags": [1, 2]
}

```

Retrieve a specific article:
```
GET /articles/1/

```

Update a specific article:
```
Update a specific article:
```
```JSON
PUT /articles/1/
Content-Type: application/json

{
    "title": "Updated Article Title",
    "content": "This is the updated content of the article."
}

```
