from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def calculate(operation, numbers):
    if not numbers:
        return "Error: No numbers provided"

    result = numbers[0]

    try:
        if operation == 'add':
            result = sum(numbers)
        elif operation == 'subtract':
            for num in numbers[1:]:
                result -= num
        elif operation == 'multiply':
            result = 1
            for num in numbers:
                result *= num
        elif operation == 'divide':
            for num in numbers[1:]:
                if num == 0:
                    return "Error: Division by zero"
                result /= num
        else:
            return "Error: Invalid operation"
        return round(result, 2)
    except Exception as e:
        return f"Error: {str(e)}"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def perform_calculation():
    data = request.json
    numbers = list(map(float, data.get('numbers', [])))
    operation = data.get('operation')
    result = calculate(operation, numbers)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
