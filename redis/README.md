## Learn Redis with project URL Shortener
# URL Shortener API

A simple URL shortener API built with Python, Flask, and Redis. This API allows users to shorten URLs, redirect to original URLs, and track the number of times a shortened URL has been accessed.

## Features

- **Shorten URLs**: Generate a unique shortened URL.
- **Redirect to Original URL**: Use the shortened URL to be redirected to the original URL.
- **Track Analytics**: Get the number of visits for a shortened URL.
- **Expiration**: Shortened URLs automatically expire after a set duration.

## Prerequisites

- Python 3.x
- Redis server (ensure Redis is running on `localhost:6379`)
- Flask and Redis Python libraries

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/url-shortener.git
    cd url-shortener
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Start the Redis server** (if not already running):
    ```bash
    redis-server
    ```

4. **Run the Flask server**:
    ```bash
    python app.py
    ```

## API Endpoints

### 1. Shorten a URL
- **Endpoint**: `/shorten`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "url": "https://www.example.com"
  }
