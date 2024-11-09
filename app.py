from flask import Flask, request, jsonify
from utils.terraform import generate_terraform_files, run_terraform_plan, apply_terraform
from utils.ansible import run_ansible_playbook

app = Flask(__name__)

@app.route('/generate_code', methods=['POST'])
def generate_code():
    params = request.json
    terraform_status = generate_terraform_files(params)
    if terraform_status:
        return jsonify({'message': 'Terraform and Ansible configuration files generated successfully.'}), 200
    return jsonify({'error': 'Failed to generate code.'}), 500

@app.route('/run_terraform_plan', methods=['POST'])
def run_plan():
    plan_output = run_terraform_plan()
    return jsonify({'message': 'Terraform plan executed.', 'output': plan_output}), 200

@app.route('/apply_infrastructure', methods=['POST'])
def apply_infrastructure():
    apply_output = apply_terraform()
    return jsonify({'message': 'Infrastructure provisioned successfully.', 'output': apply_output}), 200

@app.route('/configure_postgresql', methods=['POST'])
def configure_postgresql():
    ansible_output = run_ansible_playbook()
    return jsonify({'message': 'PostgreSQL configured and replication set up successfully.', 'output': ansible_output}), 200

if __name__ == '__main__':
    app.run(debug=True)
