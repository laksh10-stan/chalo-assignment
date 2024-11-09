# PostgreSQL Primary-Replica Setup API

## Overview
This API automates the setup of a PostgreSQL primary-read-replica architecture using Terraform for infrastructure provisioning and Ansible for configuration management. It dynamically generates configuration files and executes the necessary steps to provision and configure PostgreSQL replication between nodes.

## Features
- **Dynamic Infrastructure Provisioning**: Uses AWS EC2 and Security Groups via Terraform.
- **PostgreSQL Replication**: Configures a primary-read-replica architecture.
- **Custom Configuration**: Supports configuring key PostgreSQL settings like `max_connections` and `shared_buffers`.

## Endpoints

1. **POST /generate_code**: Generates the Terraform and Ansible configuration files based on the input parameters.
    - **Request Body Example**:
    ```json
    {
      "postgres_version": "14",
      "instance_type": "t3.medium",
      "num_replicas": 2,
      "max_connections": 200,
      "shared_buffers": "256MB"
    }
    ```

2. **POST /run_terraform_plan**: Runs `terraform plan` to validate the infrastructure setup.

3. **POST /apply_infrastructure**: Applies the Terraform plan to provision the infrastructure.

4. **POST /configure_postgresql**: Runs Ansible playbooks to install PostgreSQL and configure replication.

## Setup

### Prerequisites
1. Install Terraform and Ansible on your local machine.
2. Set up AWS credentials to allow Terraform access to provision EC2 instances.
    - Example: Store your credentials in `~/.aws/credentials`.

### How to Run

1. Clone this repository and navigate to the `api/` directory.
   ```bash
   git clone https://github.com/example/postgres-api.git
   cd api/
