from flask import Flask, request, redirect
import requests
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS

app = OpenAPI(__name__, info=Info(title="API Gateway", version="1.0.0"))
CORS(app)


# Tag para organização no Swagger
gateway_tag = Tag(name="Gateway", description="Roteamento para Student e Grades Services")

# URLs dos serviços
STUDENT_SERVICE_URL = "http://192.168.1.65:5001"
GRADES_SERVICE_URL = "http://192.168.1.65:5002"
AUTH_SERVICE_URL = "http://192.168.1.65:5003"
ORCHESTRATOR_URL  = "http://192.168.1.65:6000"

@app.get('/', tags=[gateway_tag])
def home():
    """Redireciona para a documentação Swagger."""
    return redirect('/openapi')


# ==================== ORQUESTRAÇÃO ====================

@app.route("/gateway/register-student", methods=["POST"])
def register_student():

    response = requests.post(f"{ORCHESTRATOR_URL}/student-saga/register", data=request.form)
    return response.content, response.status_code

@app.route("/gateway/delete-student", methods=["DELETE"])
def delete_student():

    response = requests.delete(f"{ORCHESTRATOR_URL}/student-saga/delete", params=request.args)
    return response.content, response.status_code


# ==================== STUDENT SERVICE ====================
@app.route("/student/<path:path>",methods=["GET", "POST", "PUT", "DELETE"])
def proxy_students(path):
    
    query_string = request.query_string.decode()
    url = f"{STUDENT_SERVICE_URL}/{path}"

    if query_string:
        url += f"?{query_string}"
    
  
    print("\n", path, query_string, sep="\n")
    print(f"Forwarding to: {url}")
    print(">>> Método:", request.method)
    print(">>> Headers:", dict(request.headers))
    print(">>> Query string:", request.query_string.decode())
    print(">>> Body:", request.get_data())

    response = requests.request(
        method=request.method,
          url=url, headers=request.headers, data=request.data)
    return response.content, response.status_code

# ==================== GRADE SERVICE ====================
@app.route("/grade/<path:path>",methods=["GET", "POST", "PUT", "DELETE"])
def proxy_grades(path):
    
    query_string = request.query_string.decode()

    url = f"{GRADES_SERVICE_URL}/{path}"
    
    if query_string:
        url += f"?{query_string}"
    
    print("\n", path, query_string, sep="\n")
    print(f"Forwarding to: {url}")
    print(">>> Método:", request.method)
    print(">>> Headers:", dict(request.headers))
    print(">>> Query string:", request.query_string.decode())
    print(">>> Body:", request.get_data())

    response = requests.request(method=request.method, url=url, headers=request.headers, data=request.data)
    return response.content, response.status_code

# ==================== USER SERVICE ====================
@app.route("/auth/<path:path>",methods=["GET", "POST", "PUT", "DELETE"])
def proxy_auth(path):

    query_string = request.query_string.decode()
    url = f"{AUTH_SERVICE_URL}/{path}"
    
    if query_string:
        url += f"?{query_string}"    

    print("\n", path, query_string, sep="\n")
    print(f"Forwarding to: {url}")
    print(">>> Método:", request.method)
    print(">>> Headers:", dict(request.headers))
    print(">>> Query string:", request.query_string.decode())
    print(">>> Body:", request.get_data())

    response = requests.request(method=request.method, url=url, headers=request.headers, data=request.data)
    return response.content, response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
