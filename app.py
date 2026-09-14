import os

from flask import Flask, render_template

from dotenv import load_dotenv

from azure.identity import ClientSecretCredential

from azure.mgmt.resource.resources import ResourceManagementClient



load_dotenv()



app = Flask(__name__)



credential = ClientSecretCredential(

    tenant_id=os.getenv("AZURE_TENANT_ID"),

    client_id=os.getenv("AZURE_CLIENT_ID"),

    client_secret=os.getenv("AZURE_CLIENT_SECRET")

)



resource_client = ResourceManagementClient(

    credential, os.getenv("AZURE_SUBSCRIPTION_ID")

)



@app.route('/')

def home():

    resources = []

    for item in resource_client.resource_groups.list():

        resources.append({

            "name": item.name,

            "type": "Resource Group",

            "status": "Running"

        })

    if not resources:

        resources.append({"name": "No resources found", "type": "-", "status": "Stopped"})

    return render_template('dashboard.html', resources=resources)



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
