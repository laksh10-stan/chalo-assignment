import subprocess
import os

def run_ansible_playbook():
    try:
        os.chdir('../ansible/')
        result = subprocess.run(['ansible-playbook', '-i', 'inventory', 'playbooks/common.yml'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
