from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "application": "Student Grade Calculator",
        "status": "Running",
        "version": "2.0.0",
        "instructions": "Send a GET request to /calculate with marks comma-separated, e.g., /calculate?marks=80,90,85"
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/calculate', methods=['GET'])
def calculate():
    marks_param = request.args.get('marks', '')
    if not marks_param:
        return jsonify({"error": "Please provide marks parameter, e.g. ?marks=80,90,85"}), 400
    
    try:
        marks_list = [float(x.strip()) for x in marks_param.split(',') if x.strip()]
        if not marks_list:
            raise ValueError()
    except ValueError:
        return jsonify({"error": "Invalid marks format. Must be a list of numbers."}), 400

    total = sum(marks_list)
    average = total / len(marks_list)

    # Added Push 2 Logic: Grade calculation evaluation matrix
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    response_data = {
        "total": total,
        "average": average,
        "grade": grade
    }
    
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
