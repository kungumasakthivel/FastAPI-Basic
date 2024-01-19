### To run fastapi server using uvicorn server package

`uvicorn filename:fastapi_instance_name --reload`

### Basic API operation

- GET
- POST
- PUT
- DELETE

### Automatic Documentation by FastAPI

- FastAPI creates automatic documentation for particular endpoint
- This helps to know about our api endpoint function
- We can also test out api from auto generated docs
- `path_name/docs` to open fastapi auto generated **docs**

### Path Parameters

- In path parameter we have two inputh parameter **'path'** and '**query'**
- Path parameter is like `.com/path_name/sub_path` is path parameters in URL

### Query Parameters

- 






### Common Mistake

1. Use  **/**  in endpoint path starting character to specify any path to endpoint
2. Use decerator `@app.method_name` before writing any endpoint
