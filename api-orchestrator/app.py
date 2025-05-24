from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Permite requisições de qualquer origem (desenvolvimento)

# URLs dos microsserviços (ajuste para seu ambiente/dockers)
STUDENT_SERVICE_URL = "http://0.0.0.0:5001"
USER_SERVICE_URL = "http://0.0.0.0:5002"
GRADE_SERVICE_URL = "http://0.0.0.0:5003"


### ========== [1] CADASTRO COMPLETO ==========
@app.route('/student-saga/register', methods=['POST'])
def register_student_saga():
    try:
        # --- CAPTURA DADOS DO FORM ---
        student_data = {
            "name": request.form.get("student_name"),
            "birthdate": request.form.get("student_birthdate")
        }

        user_data = {
            "username": request.form.get("user_username"),
            "email": request.form.get("user_email")
        }

        grade_data = {
            "subject": request.form.get("grade_subject"),
            "value": request.form.get("grade_value")
        }

        # === 1. CADASTRAR ESTUDANTE ===
        student_resp = requests.post(f"{STUDENT_SERVICE_URL}/student", data=student_data)
        student_resp.raise_for_status()
        student_id = student_resp.json().get("id") or student_resp.json().get("student", {}).get("id")

        # === 2. CADASTRAR USUÁRIO ===
        user_data["student_id"] = student_id
        user_resp = requests.post(f"{USER_SERVICE_URL}/user", data=user_data)
        user_resp.raise_for_status()

        # === 3. CADASTRAR NOTA ===
        grade_data["student_id"] = student_id
        grade_resp = requests.post(f"{GRADE_SERVICE_URL}/grade", data=grade_data)
        grade_resp.raise_for_status()

        return jsonify({"message": "Estudante, usuário e nota cadastrados com sucesso."}), 201

    except Exception as e:
        # ROLLBACK EM CASO DE FALHA
        if 'student_id' in locals():
            try: requests.delete(f"{USER_SERVICE_URL}/user", params={"student_id": student_id})
            except: pass
            try: requests.delete(f"{GRADE_SERVICE_URL}/grade", params={"student_id": student_id})
            except: pass
            try: requests.delete(f"{STUDENT_SERVICE_URL}/student", params={"id": student_id})
            except: pass

        return jsonify({
            "error": "Erro ao cadastrar. Rollback executado.",
            "detail": str(e)
        }), 500


### ========== [2] DELETAR ESTUDANTE + AUDITORIA ==========
@app.route('/student-saga/delete', methods=['DELETE'])
def delete_student_saga():
    student_id = request.form.get("student_id")

    user_audit = {
        "username": request.form.get("user_username"),
        "email": request.form.get("user_email"),
        "student_id": student_id
    }

    grade_audit = {
        "subject": request.form.get("grade_subject"),
        "value": request.form.get("grade_value"),
        "student_id": student_id
    }

    try:
        # 1. Deleta estudante
        del_resp = requests.delete(f"{STUDENT_SERVICE_URL}/student", params={"id": student_id})
        del_resp.raise_for_status()
        

        # 2. Deleta nota
        grade_del_resp = requests.delete(f"{GRADE_SERVICE_URL}/grade", params={"student_id": student_id})
        grade_del_resp.raise_for_status()

        # 3. Deleta usuário
        user_del_resp = requests.delete(f"{USER_SERVICE_URL}/user", params={"student_id": student_id})
        user_del_resp.raise_for_status()

        return jsonify({"message": "Estudante e dados relacionados deletados com sucesso."}), 200

    except Exception as e:
        # Se algum delete falhar, tenta restaurar o estudante e registrar auditoria
        try: requests.post(f"{STUDENT_SERVICE_URL}/student", data={"id": student_id})
        except: pass
        try: requests.post(f"{GRADE_SERVICE_URL}/grade", data=grade_audit)
        except: pass
        try: requests.post(f"{USER_SERVICE_URL}/user", data=user_audit)
        except: pass

        return jsonify({
            "error": "Erro ao deletar dados. Rollback executado com auditoria.",
            "detail": str(e)
        }), 500

    try:
        student_id = request.form.get("student_id")

        user_audit = {
            "username": request.form.get("user_username"),
            "email": request.form.get("user_email"),
            "student_id": student_id
        }

        grade_audit = {
            "subject": request.form.get("grade_subject"),
            "value": request.form.get("grade_value"),
            "student_id": student_id
        }

        # === 1. DELETA ESTUDANTE ===
        del_resp = requests.delete(f"{STUDENT_SERVICE_URL}/student", params={"id": student_id})
        del_resp.raise_for_status()

        # === 2. REGISTRA NOTA AUDITIVA ===
        grade_resp = requests.post(f"{GRADE_SERVICE_URL}/grade", data=grade_audit)
        grade_resp.raise_for_status()

        # === 3. REGISTRA USUÁRIO AUDITIVO ===
        user_resp = requests.post(f"{USER_SERVICE_URL}/user", data=user_audit)
        user_resp.raise_for_status()

        return jsonify({"message": "Estudante deletado e auditoria registrada."}), 200

    except Exception as e:
        try: requests.post(f"{STUDENT_SERVICE_URL}/student", data={"id": student_id})
        except: pass
        try: requests.delete(f"{GRADE_SERVICE_URL}/grade", params={"student_id": student_id})
        except: pass
        try: requests.delete(f"{USER_SERVICE_URL}/user", params={"student_id": student_id})
        except: pass

        return jsonify({
            "error": "Erro ao deletar/registrar auditoria. Rollback executado.",
            "detail": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)
