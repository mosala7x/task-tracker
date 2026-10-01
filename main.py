from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# 1. إنشاء تطبيق FastAPI
app = FastAPI()

# 2. تفعيل CORS حتى تتمكن الواجهة من التواصل مع السيرفر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. قاعدة البيانات المؤقتة
tasks = [
    {"id": 1, "title": "تعلم أساسيات Git"},
    {"id": 2, "title": "بناء REST API"}
]

# 4. تحديد شكل البيانات المفحوصة القادمة من الـ Frontend
class TaskCreate(BaseModel):
    title: str

# 5. مسار جلب المهام (GET)
@app.get("/api/tasks")
def get_tasks():
    return tasks

# 6. مسار إضافة مهمة جديدة (POST)
@app.post("/api/tasks")
def add_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title
    }
    tasks.append(new_task)
    return new_task