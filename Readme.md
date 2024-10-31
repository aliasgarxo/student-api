# Student API

A simple RESTful API for managing student data, implemented in Python using the Flask framework. This API supports basic CRUD operations (Create, Read, Update, Delete) for a `Student` entity with attributes such as ID, Name, Grade, and Email.

## Features

- **Retrieve All Students**: GET `/students`
- **Retrieve Student by ID**: GET `/students/{id}`
- **Add New Student**: POST `/students`
- **Update Student by ID**: PUT `/students/{id}`
- **Delete Student by ID**: DELETE `/students/{id}`

## Prerequisites

- **Python 3.10+**
- **Flask** (Install using requirements file)
- **Virtual Environment** (Recommended)

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/aliasgarxo/student-api.git
cd student-api 
```

### 2. Set Up Virtual Environment
It’s recommended to use a virtual environment for dependency management. Run the following commands to create and activate a virtual environment:

```bash 
python3 -m venv venv
source venv/bin/activate  # On Windows, use .\venv\Scripts\activate
```

### 3. Install Dependencies
With the virtual environment activated, install the required dependencies:

```bash 
pip install -r requirements.txt
```

### 4. Running the Service Locally
With all dependencies installed, run the following command to start the Flask development server:

```bash
python app.py
```

The server will start on `http://127.0.0.1:5000` by default.

To test the service, you can use tools like Postman, curl, or REST Client in VS Code.

### Testing the API
Using the Provided .http File in repository
The project includes a .http file with pre-configured HTTP requests for testing each endpoint. You can open this file in VS Code with the REST Client extension installed, and use it to test each CRUD operation.

Example Requests
Get All Students
```bash
GET http://127.0.0.1:5000/students
```

Get Student by ID
```bash
GET http://127.0.0.1:5000/students/1
```

Add New Student
```bash
POST http://127.0.0.1:5000/students
Content-Type: application/json

{
  "name": "Aliasgar Husain",
  "grade": "E-",
  "email": "aliasgar@example.com"
}
```

Delete Student by ID
```bash
DELETE http://127.0.0.1:5000/students/1
```

