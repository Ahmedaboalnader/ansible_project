from flask import Flask, jsonify, render_template_string
import os
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def home():
    app.logger.info("Home endpoint was reached")
    app_version = os.environ.get('APP_VERSION', 'unknown')
    hostname = os.uname()[1]

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ansible Deployed App</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f0f2f5;
                color: #333;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
            }
            .header {
                background-color: #2c3e50;
                color: white;
                padding: 20px 40px;
                text-align: center;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .header h1 {
                margin: 0;
                font-size: 2em;
            }
            .main-content {
                flex: 1;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            .card {
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                padding: 30px 40px;
                text-align: center;
                max-width: 600px;
            }
            .card h2 {
                margin-top: 0;
                color: #3498db;
            }
            .card p {
                font-size: 1.2em;
                line-height: 1.6;
            }
            .card .hostname {
                background-color: #ecf0f1;
                color: #7f8c8d;
                padding: 5px 10px;
                border-radius: 4px;
                font-family: "Courier New", Courier, monospace;
            }
            .footer {
                background-color: #34495e;
                color: white;
                padding: 30px 40px;
                text-align: center;
            }
            .footer h3 {
                margin-top: 0;
                color: #ecf0f1;
            }
            .footer .instructions {
                background-color: #2c3e50;
                border-radius: 8px;
                padding: 20px;
                text-align: left;
                max-width: 800px;
                margin: 0 auto;
                font-family: "Courier New", Courier, monospace;
            }
            .footer code {
                background-color: #95a5a6;
                color: #2c3e50;
                padding: 2px 5px;
                border-radius: 3px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Welcome to the Deployed Application!</h1>
        </div>
        <div class="main-content">
            <div class="card">
                <h2>Hello from the App!</h2>
                <p>This page is served from container: <span class="hostname">{{ hostname }}</span></p>
                <p>Application Version: <strong>{{ app_version }}</strong></p>
            </div>
        </div>
        <div class="footer">
            <h3>About This Project</h3>
            <div class="instructions">
                <p>This project is an example of a web application deployed using Ansible and Vagrant.</p>
                <p><strong>Initial Deployment:</strong></p>
                <p>1. Run <code>vagrant up</code> to create the VMs.</p>
                <p>2. Run <code>ansible-playbook playbooks/site.yml --ask-vault-pass</code> to provision the servers.</p>
                <p><strong>Deploying/Updating the App:</strong></p>
                <p>To deploy or update the application, run:<br><code>ansible-playbook playbooks/deploy_app.yml --ask-vault-pass</code></p>
                <p>To deploy a new version, update <code>current_version</code> in <code>group_vars/all.yml</code> and run the deploy command.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, app_version=app_version, hostname=hostname)

@app.route('/health')
def health():
    app.logger.info("Health endpoint was reached")
    return jsonify(status="ok", version=os.environ.get('APP_VERSION', 'unknown'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
