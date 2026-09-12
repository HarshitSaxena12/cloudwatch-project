from flask import Flask, render_template



app = Flask(__name__)



@app.route('/')

def home():

    resources = [

        {"name": "Web-Server-01", "type": "Virtual Machine", "status": "Running"},

        {"name": "Storage-Prod", "type": "Storage Account", "status": "Running"},

        {"name": "DB-Backup-VM", "type": "Virtual Machine", "status": "Stopped"}

    ]

    return render_template('dashboard.html', resources=resources)



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
