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

- Query parameter is similar to path parameter
- This query is used to **pass value** into *URL*
- Query parameter is like `.com/path_name?name=some_name`
- Difference between path and query parameter is the endpoint parameter not needed in query parameter
- Always give query parameter default value as  `None`  type as default value to avoid *required parameter while testing the API in docs mode
- Enclose the parameter str within Optional because the given str parameter for that endpoint is optional in that endpoint
- We cannot place optional parameter before required parameter in endpoint function

### Common Mistake

1. Use  **/**  in endpoint path starting character to specify any path to endpoint
2. Use decerator `@app.method_name` before writing any endpoint
