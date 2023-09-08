# Newser Project

Newser is a project that syncs published news from Hacker News to a database every 5 minutes using celery. It provides a web interface to list the latest news, filter by type, search by text, and includes pagination. Additionally, it offers an API for listing items, adding new items to the database, and allows updates and deletions for items created in the API.

## Getting Started

These instructions will help you get the project up and running on your local development environment.

### Prerequisites

Before you begin, make sure you have the following tools installed:

- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/downloads/) (for running management commands)

### Build the Stack

Build the Docker stack, which includes Django and PostgreSQL:

```bash
docker compose -f local.yml build
```

You can also use `production.yml` for a production-like environment.

### Initialize Git and Pre-commit

Initialize a Git repository and install the pre-commit hooks:

```bash
git init
pre-commit install
```

### Execute Management Commands

Run management commands to create and migrate the database:

```bash
docker compose -f local.yml run --rm django python manage.py makemigrations news
docker compose -f local.yml run --rm django python manage.py migrate
```

### Run the Stack

Start the development server:

```bash
docker compose -f local.yml up
```

You can access the site at [http://localhost:8000](http://localhost:8000), and the Swagger documentation for the API at [http://localhost:8000/docs](http://localhost:8000/docs).

## API Endpoints

The News API provides the following endpoints:

- `GET /api/stories/`: List all stories.
- `POST /api/stories/`: Create a new story.
- `GET /api/stories/<int:pk>/`: Retrieve a specific story.
- `PUT /api/stories/<int:pk>/`: Update a specific story (if created by the user).
- `DELETE /api/stories/<int:pk>/`: Delete a specific story (if created by the user).

## Permissions

- `IsOwnerOrReadOnly`: A custom permission class that allows owners to update and delete their own stories.

## Usage

Interact with the News API using the provided endpoints for listing, creating, updating, and deleting stories. Ensure proper authentication and permissions for user-owned actions.

## Authors

- [Obakunle Oluseye][obakunleoluseye@gmail.com]
