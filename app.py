from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "application": "Student Grade Calculator",
        "status": "Running",
        "version": "1.0.0",
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

    # Note: Grade calculation will be added in Push 2 as required by the scenario
    response_data = {
        "total": total,
        "average": average
    }
    
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
