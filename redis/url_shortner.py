#!/usr/bin/env python3
"""Script the take Original URL and Shortnes URLs and Store them and tracks click counts
and other analytics in Redis"""
import redis
import string
import random
from flask import Flask, request, redirect, jsonify


"""Initialize Flask and Redis"""
app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)


def generate_short_id(length=6):
    """Generate a random short ID"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Endpoint to shorten URL"""
    original_url = request.json.get('url')
    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    short_id = generate_short_id()

    """Check if the short ID is unique"""
    while r.get(f"url:{short_id}"):
        short_id = generate_short_id()

    r.setex(f"url:{short_id}", 2592000, original_url)  # 30 days in seconds

    r.set(f"visits:{short_id}", 0)

    return jsonify({"short_url": request.host_url + short_id})


@app.route('/<short_id>')
def redirect_url(short_id):
    """Endpoint to redirect to the original URL"""
    original_url = r.get(f"url:{short_id}")

    if original_url:
        r.incr(f"visits:{short_id}")
        return redirect(original_url.decode('utf-8'))
    else:
        return jsonify({"error": "URL not found"}), 404


@app.route('/analytics/<short_id>', methods=['GET'])
def analytics(short_id):
    """Analytics endpoint"""
    visits = r.get(f"visits:{short_id}")
    if visits is not None:
        return jsonify({"visits": int(visits.decode('utf-8'))})
    else:
        return jsonify({"error": "URL not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
