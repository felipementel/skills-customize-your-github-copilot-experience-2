# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework by defining routes, handling request data, and returning JSON responses. You will practice web framework fundamentals, HTTP methods, and Python type hints.

## 📝 Tasks

### 🛠️	Create a Basic FastAPI App

#### Description
Set up a FastAPI application and define a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import `FastAPI` and create an `app` instance.
- Define a `GET /` route that returns a JSON welcome message. Example:
  ```json
  {"message": "Welcome to the FastAPI assignment!"}
  ```
- Run the app using `uvicorn` with the command:
  ```
  uvicorn starter-code:app --reload
  ```

### 🛠️	Build a Items CRUD Endpoints

#### Description
Implement a simple in-memory list of items with endpoints to create, read, and delete entries.

#### Requirements
Completed program should:

- Define a `GET /items` endpoint that returns all items as a JSON list.
- Define a `POST /items` endpoint that accepts a JSON body with a `name` field and adds the item to the list. Example request body:
  ```json
  {"name": "Notebook"}
  ```
- Define a `DELETE /items/{item_id}` endpoint that removes an item by its index and returns the deleted item.
- Return appropriate error responses (e.g., `404`) when an item is not found.

### 🛠️	Add Input Validation with Pydantic

#### Description
Use a Pydantic model to validate incoming request data for the `POST /items` endpoint.

#### Requirements
Completed program should:

- Define a `Pydantic` `BaseModel` called `Item` with a required `name` field (string) and an optional `description` field (string, default `None`).
- Update the `POST /items` endpoint to accept and validate an `Item` model.
- Return the created item in the response. Example response:
  ```json
  {"name": "Notebook", "description": null}
  ```
- Reject requests with missing or invalid fields automatically via Pydantic validation.
