from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        'name': 'manish',
        'age': 22,
        'email': 'manish@example.com'
    },
    2: {
        'name': 'manish',
        'age': 22,
        'email': 'manish@example.com'
    },
    3: {
        'name': 'manish',
        'age': 22,
        'email': 'manish@example.com'
    }
}


@app.get('/')
def index():
    return {'page': 'homepage'}


@app.get('/student-detail/{student_id}')
def student_detail(student_id: int = Path(None, description='Enter student ID', gt=0, le=3)):
    return students[student_id]
