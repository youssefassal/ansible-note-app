Ansible Note-Taking App Deployment
📌 Overview
This project deploys a Python Flask note-taking web application on an AWS EC2 instance running Amazon Linux, using Ansible roles for automated configuration and deployment.
The application stores notes in a sqlite database, each with a timestamp, and displays them on the web page.

🚀 Features
Automated provisioning with Ansible.

Python Flask web app.

sqlite database for note storage.

Systemd service for automatic startup.

Accessible via browser on port 80.

🛠 Requirements
Before running the playbook, make sure you have:

AWS EC2 instance (Amazon Linux, t2.micro recommended).

Security Group allowing inbound:

22 (SSH)

80 (HTTP)

SSH key pair for EC2 access.

Ansible installed on the control machine.

📂 Project Structure
bash
Copy
Edit
ansible-project/
│
├── ansible.cfg
├── hosts                 # Inventory file
├── deploy.yml            # Main playbook
├── note_app/             # Ansible role
│   ├── tasks/main.yml    # Installation & deployment tasks
│   ├── files/app.py      # Flask app
│   ├── files/requirements.txt
│   └── templates/note_app.service.j2
└── .gitignore
⚡ Deployment Steps
1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/youssefassal/ansible-note-app.git
cd ansible-note-app
2️⃣ Configure inventory
Edit the hosts file with your EC2 instance’s public IP and SSH key:

ini
Copy
Edit
[webserver]
ec2_instance ansible_host=YOUR_EC2_PUBLIC_IP ansible_user=ec2-user ansible_ssh_private_key_file=/path/to/key.pem
3️⃣ Run the playbook
bash
Copy
Edit
ansible-playbook -i hosts deploy.yml
🌐 Access the App
Open your browser and go to:

cpp
Copy
Edit
http://YOUR_EC2_PUBLIC_IP/
You will see:

A form to submit new notes.

A list of saved notes with timestamps.

