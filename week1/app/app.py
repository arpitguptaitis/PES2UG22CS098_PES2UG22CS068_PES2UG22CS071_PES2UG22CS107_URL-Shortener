import os
import redis
from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)
redis_client = redis.Redis(
    host=os.environ['REDIS_HOST'],
    port=6379,
    password=os.environ.get('REDIS_PASSWORD'),
    decode_responses=True
)

@app.route('/')
def index():
    return jsonify({"status": "URL Shortener API is running"})

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    short_id = os.urandom(6).hex()
    redis_client.set(short_id, url)
    return jsonify({"short_url": f"/{short_id}"})

@app.route('/<id>')
def redirect_url(id):
    url = redis_client.get(id)
    if url:
        return redirect(url)
    return render_template('redirect.html', error="URL not found"), 404

if __name__ == '__main__':
    redis_client.ping()
    app.run(host='0.0.0.0', port=5000)