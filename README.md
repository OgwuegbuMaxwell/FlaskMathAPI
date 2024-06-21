![Screenshot (139)](https://github.com/OgwuegbuMaxwell/FlaskMathAPI/assets/53094485/aeee352a-7b67-4133-aa8e-671825f601b6)



### **Documentation for FlaskMathAPI**

**Introduction**
FlaskMathAPI is a simple RESTful API built with Flask and Flask-RESTful, designed to perform basic mathematical operations such as addition, subtraction, multiplication, and division. This API validates input data to ensure that all necessary parameters are provided and handles operations on integers.

**Getting Started**
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

**Prerequisites**
You need to have Python installed on your system. The API has been tested with Python 3.8. Also, you will need pip to install the dependencies.

**Installing**
Clone the repository to your local machine:

`git clone https://github.com/OgwuegbuMaxwell/FlaskMathAPI.git`

**Navigate into the project directory:**
`cd FlaskMathAPI`

**Create a virtual environment:**
`python -m venv venv
`

Activate the virtual environment:

- Windows:
`venv\Scripts\activate`

- Unix or MacOS:
`source venv/bin/activate
`

**Install the required packages:**
`pip install -r requirements.txt`

**Run the application:**
`python app.py
`

The application should now be running on http://127.0.0.1:5000/.



**### API Endpoints**
The API supports the following operations:

Addition

URL: /add
Method: POST
Data Params: {"x": int, "y": int}
Success Response:
Code: 200
Content: { "Message": result, "Status Code": 200 }
Error Response:
Code: 301
Content: { "Message": "An error happened", "Status Code": 301 }
Subtraction

URL: /subtract
Method: POST
Data Params: {"x": int, "y": int}
Responses: Similar to addition.
Multiplication

URL: /multiply
Method: POST
Data Params: {"x": int, "y": int}
Responses: Similar to addition.
Division

URL: /divide
Method: POST
Data Params: {"x": int, "y": int}
Success Response:
Code: 200
Content: { "Message": result, "Status Code": 200 }
Error Response:
Code: 302
Content: { "Message": "Division by zero", "Status Code": 302 }


