# Social Media API

## Overview

This is a RESTful API built with Django and Django REST Framework (DRF) that provides social media functionalities, including user authentication, post creation, commenting, liking, following users, and viewing a personalized feed.

## Features

- **User Authentication:** Register, login, and manage user profiles.
- **Posts Management:** Create, update, delete, and list posts.
- **Comments System:** Comment on posts and manage comments.
- **Like System:** Users can like and unlike posts.
- **Following System:** Follow and unfollow users.
- **Personalized Feed:** View posts from followed users.
- **Notifications:** Receive notifications for likes, comments, and new followers.

## Technologies Used

- Python
- Django
- Django REST Framework
<!-- - PostgreSQL (Database) -->
- Token Authentication

## Installation & Setup

### 1. Clone the Repository

```bash
 git clone https://github.com/G-alileo/social_media_api.git
 cd social_media_api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

## API Endpoints

### Authentication

| Method | Endpoint     | Description                         |
| ------ | ------------ | ----------------------------------- |
| POST   | `http://127.0.0.1:8000/accounts/register/` | Register a new user                 |
| POST   | `http://127.0.0.1:8000/accounts/login/`    | Log in and get authentication token |

### User Profile

| Method | Endpoint           | Description              |
| ------ | ------------------ | ------------------------ |
| GET    | `http://127.0.0.1:8000/accounts/profile/`        | Get current user profile |
| PUT    | `http://127.0.0.1:8000/accounts/profile/`        | Update user profile      |

### Posts

| Method | Endpoint       | Description                 |
| ------ | -------------- | --------------------------- |
| GET    | `http://127.0.0.1:8000/api/posts/`      | List all posts              |
| POST   | `http://127.0.0.1:8000/api/posts/`      | Create a new post           |
| GET    | `http://127.0.0.1:8000/api/posts/{id}/` | Retrieve a post             |
| PUT    | `http://127.0.0.1:8000/api/posts/{id}/` | Update a post (author only) |
| DELETE | `http://127.0.0.1:8000/api/posts/{id}/` | Delete a post (author only) |

### Comments

| Method | Endpoint                | Description                    |
| ------ | ----------------------- | ------------------------------ |
| GET    | `http://127.0.0.1:8000/api/comments/` | List comments for a post       |
| POST   | `http://127.0.0.1:8000/api/comments/` | Add a comment to a post   // pass post id in the post field in the body to add comment to that specific post     |
| PUT    | `http://127.0.0.1:8000/api/comments/{id}/`       | Edit a comment (author only)   |
| DELETE | `http://127.0.0.1:8000/api/comments/{id}/`       | Delete a comment (author only) |

### Likes

| Method | Endpoint              | Description   |
| ------ | --------------------- | ------------- |
| POST   | `http://127.0.0.1:8000/api/{id}/like/`   | Like a post   |
| POST   | `http://127.0.0.1:8000/api/{id}/unlike/` | Unlike a post |

### Following System

| Method | Endpoint               | Description     |
| ------ | ---------------------- | --------------- |
| POST   | `http://127.0.0.1:8000/accounts/follow/{user_id}/`   | Follow a user   |
| POST   | `http://127.0.0.1:8000/accounts/unfollow/{user_id}/` | Unfollow a user |

### Personalized Feed

| Method | Endpoint | Description                   |
| ------ | -------- | ----------------------------- |
| GET    | `http://127.0.0.1:8000/api/feed/` | Get posts from followed users |

### Notifications

| Method | Endpoint          | Description           |
| ------ | ----------------- | --------------------- |
| GET    | `http://127.0.0.1:8000/notifications/` | Get all notifications |

## Use Cases

### 1. **User Registration and Authentication**

- Users can register with a unique username and password.
- Users log in to receive an authentication token.

### 2. **Post Creation and Interaction**

- Users can create posts with a title and content.
- Other users can comment on posts.
- Users can like/unlike posts.

### 3. **Following and Feed**

- Users can follow/unfollow others.
- The `/feed/` endpoint returns posts from followed users in chronological order.

### 4. **Notifications**

- Users receive notifications when someone follows them, likes their post, or comments on their post.

## License

This project is open-source and available under the MIT License.

---

**Author: Jamespeter Murithi**\
**GitHub:** G-alileo

