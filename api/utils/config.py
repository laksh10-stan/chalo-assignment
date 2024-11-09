import os

# AWS Config
AWS_REGION = os.getenv('AWS_REGION', 'us-west-2')
AMI_ID = os.getenv('AMI_ID', 'ami-0abcdef1234567890')  # Placeholder, update with a valid AMI

# Terraform paths
TERRAFORM_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../terraform/'))

# Ansible paths
ANSIBLE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ansible/'))

# PostgreSQL Configurations (these will be passed by API request typically)
POSTGRES_VERSION = os.getenv('POSTGRES_VERSION', '14')

# Other relevant paths or settings
