## To run fastapi server using uvicorn server package


To run fastapi file 

- Open terminal in your root folder
- Then use  `uvicorn filename:fastapi_instance_name --reload` this command will run you fastapi server
- The `filename` describes fastapi file name and `fastapi_instance_name` describes the FastAPI instance in your fastapi file

  ```python
  from fastapi import FastAPI
  app = FastAPI()
  ```
- For example if your file name is fastapi.py then to start server you should type `uvicorn fastapi:app --reload`
- If any changes happens and saved in the fastapi file `--reload` will automatically updates the changes into your server


## Basic API operation


- GET
- POST
- PUT
- DELETE


## Automatic Documentation by FastAPI


- FastAPI creates automatic documentation for particular endpoint
- This helps to know about our api endpoint function
- We can also test out api from auto generated docs
- `path_name/docs` to open fastapi auto generated **docs**


## Path Parameters


- In path parameter we have two inputh parameter **'path'** and '**query'**
- Path parameter is like `.com/path_name/sub_path` is path parameters in URL


## Query Parameters


- Query parameter is similar to path parameter
- This query is used to **pass value** into *URL*
- Query parameter is like `.com/path_name?name=some_name`
- Difference between path and query parameter is the endpoint parameter not needed in query parameter
- Always give query parameter default value as  `None`  type as default value to avoid *required parameter while testing the API in docs mode
- Enclose the parameter str within Optional because the given str parameter for that endpoint is optional in that endpoint
- We cannot place optional parameter before required parameter in endpoint function


## Combining Path & Query parameters


- Here we have both path and query parameter in endpoint function
- Path parameter value is obtained from path **URL** and query parameter value is obtained from query phase in **URL** but this query is optional
- But the purpose of this endpoint is to handle both functions
- Here both ***path and query*** parameters are required to fetch data from server


## Post Method & Request Body


- The request body contains new JSON object that contains data of new user to insert in students object
- Here we use pydantic library to verify our incoming data is in it original data type structure or not

  ```python
  from pydantic import BaseModel
  class Student(BaseModel):
      name: str
      age: int
      email: str
  ```
- Using this **BaseModel** parent class we create sub-class, so that we can verify incoming JSON data is in that particular data type or not

  ```python
  @app.post('/create-student/{student_id}')
  def create_student(student_id : int, student : Student):
      if student_id in students:
          return {'Error': 'Student Id already exists'}
      students[student_id] = student
      return students[student_id]
  ```
- In this endpoint we get JSON data in request body so we can't see data in URL we can only see new student_id were this id need to be unique which means this student_id should not be in students object.
- `student: Student` in `create_student` endpoint method say that incoming request body data should match the Student class data type structure if not then incoming JSON data can't be inserted into students object.


## Put Method


- Put method is used to update existing data in our students object, it just requires student_id and JSON data to update particular student
- But here we are not going to update entier data of particular student, but we update a specific category of student like updating only name or age or email
- So here we use another BaseModel to verify incoming JSON data is in its specific data type or not

  ```python
  class UpdateStudent(BaseModel):
      name: Optional[str] = None
      age: Optional[int] = None
      email: Optional[str] = None

  ```
- In put method endpoint we use this UpdateStudent class to verify our incoming JSON data of a particular student that already exist in students object
- In UpdateStudent class we give `None` as default data type, because while updating the existing data we no need to update every key : value pair instead we just need to update particular pair of data only

  ```python
  @app.put('/edit-details/{student_id}')
  def edit_details(student_id : int, student : UpdateStudent):
      if student_id not in students:
          return {"Student_id": "Not found in students object"}

      if student.name != None:
          students[student_id].name = student.name

      if student.age != None:
          students[student_id].age = student.age

      if student.email != None:
          students[student_id].email = student.email

      return students[student_id]
  ```
- In the above code we just try to update particular *JSON* data in which key's value needs to be updated if it have `None` data type it will not going to be update else it will update the existing value to new value


## Delete Method


- Delete method is used to delete the particular student with student_id from students object
- Here we use `app.delete('/path/{id})` to mention particular id to delete data from student object

  ```python
  @app.delete('/delete-student/{student_id}')
  def delete_student(student_id: int):
      if student_id not in students:
          return {'Error': 'Student not found'}
      del students[student_id]
      return {'Success': f'student with student id {student_id} deleted successfully'}
  ```
- This will delete the particular student data from his/her student_id

## Common Mistake


1. Use  **/**  in endpoint path starting character to specify any path to endpoint
2. Use decerator `@app.method_name` before writing any endpoint
