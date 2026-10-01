from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # للسماح للـ Frontend بالتواصل مع الـ API

# قائمة المهام المبدئية
tasks = [
    {"id": 1, "title": "تعلم أساسيات Git"},
    {"id": 2, "title": "بناء REST API"}
]

# 1. API لجلب المهام (GET)
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# 2. API لإضافة مهمة جديدة (POST)
@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title")
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)