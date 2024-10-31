from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample data to represent a database
students = [
    {"id": 1, "name": "Oseen Marcelino", "grade": "L", "email": "oseen@example.com"},
    {"id": 2, "name": "Abhinav Jingra", "grade": "L", "email": "abhinav@example.com"}
]

# Helper function to find a student by ID
def find_student(student_id):
    return next((student for student in students if student["id"] == student_id), None)

# GET /students - Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# GET /students/{id} - Retrieve a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = find_student(student_id)
    if not student:
        abort(404, description="Student not found")
    return jsonify(student)

# POST /students - Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    if not request.json or not 'name' in request.json:
        abort(400, description="Invalid data")
    new_student = {
        "id": students[-1]["id"] + 1 if students else 1,
        "name": request.json["name"],
        "grade": request.json.get("grade", ""),
        "email": request.json.get("email", "")
    }
    students.append(new_student)
    return jsonify(new_student), 201

# PUT /students/{id} - Update an existing student by ID
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = find_student(student_id)
    if not student:
        abort(404, description="Student not found")
    if not request.json:
        abort(400, description="Invalid data")
    
    student["name"] = request.json.get("name", student["name"])
    student["grade"] = request.json.get("grade", student["grade"])
    student["email"] = request.json.get("email", student["email"])
    return jsonify(student)

# DELETE /students/{id} - Delete a student by ID
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = find_student(student_id)
    if not student:
        abort(404, description="Student not found")
    students.remove(student)
    return jsonify({"message": "Student deleted successfully"})

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handler for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
