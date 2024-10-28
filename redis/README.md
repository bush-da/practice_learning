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

## API Endpoints and Example Usage

### 1. Shorten a URL
To shorten a URL, send a `POST` request to the `/shorten` endpoint with the URL you want to shorten in the request body. 

Example usage with `curl`:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://www.example.com"}' http://127.0.0.1:5000/shorten
```
Expected Response:

```json

{
  "short_url": "http://127.0.0.1:5000/abc123"
}
```
To track the number of times a shortened URL has been accessed, send a GET request to the /analytics/<short_id> endpoint.
```bash
curl -X GET http://127.0.0.1:5000/analytics/abc123
```
Expected Response:

```json

{
  "visits": 1
}
```
