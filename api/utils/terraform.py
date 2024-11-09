import subprocess
import os

def generate_terraform_files(params):
    # Create Terraform files dynamically using templates
    try:
        with open('../terraform/templates/ec2_instance.tf.j2') as f:
            ec2_template = f.read()
        with open('../terraform/main.tf', 'w') as f:
            f.write(ec2_template.format(params))
        return True
    except Exception as e:
        print(f"Error generating Terraform files: {e}")
        return False

def run_terraform_plan():
    try:
        os.chdir('../terraform/')
        result = subprocess.run(['terraform', 'plan'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

def apply_terraform():
    try:
        os.chdir('../terraform/')
        result = subprocess.run(['terraform', 'apply', '-auto-approve'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
