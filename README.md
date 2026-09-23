##CloudWatch Dashboard

A self-build Azure Infrastructure monitoring dashboard, created hands-on while preparing for AZ-104.

## What it Does

Displays live Azure resource groups from a real subscription using Service Principal authentication and the Azure Resource Manager API - no hardcoded data.

## Tech Stack

- **Backend:** Python, Flask, Jinja2
- **Cloud:** Azure (Service Principal auth, RBAC, Resource Manager SDK)
- **Infrastructure as Code:** Terraform
- **Containerization:** Docker
- **CI/CD:** Github Actions (Automated build + push to docker hub on every commit)
- **Version Control:** Git/GitHub


## Architecture

1. Flask app authenticates to azure via a aervice principal (client ID, secret, Tenant ID)
2. Queries live resource groups using the Azure SDK
3. Renders results in a styled HTML dashboard
4. Containerized with Docker for portable deployment
5. Infrastructure provisioned via Terraform (Infrastructure as code)
6. Github actions automatically builds and pushes the Docker Image on every push to main

##Running Locally

\`\`\`bash
git clone https://github.com/HarshitSaxena12/cloudwatch-project.git
cd cloudwatch-project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
\`\`\`

Create a \`.env\` file with your Azure credentials:
\`\`\`
AZURE_TENANT_ID=your-tenant-id
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
AZURE_SUBSCRIPTION_ID=your-subscription-id
\`\`\`

Run it:
\`\`\`bash
python3 app.py
\`\`\`

## Running With Docker

\`\`\`bash
docker build -t cloudwatch-dashboard .
docker run -p 5000:5000 --env-file .env cloudwatch-dashboard
\`\`\`

## Provisioning Infrastructure With Terraform

\`\`\`bash
cd terraform
terraform init
terraform plan
terraform apply
\`\`\`

## What I Learned Building This

- Azure Service Principal authentication and least-privilege RBAC design (Reader vs Contributor)
- Writing and debugging a Dockerfile from scratch
- Infrastructure as Code with Terraform, including provider registration and permission scoping
- Building a GitHub Actions CI/CD pipeline with secrets management
- Real-world Python environment management (venv, requirements.txt) 
