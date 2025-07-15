basic-dynamic-website-on-docker
Basic Dynamic Website on Docker
🏗️ A Simple Yet Powerful Dockerized Web App
Welcome to Basic Dynamic Website on Docker, a minimal yet scalable web application running in Docker containers. Designed for developers looking to containerize their projects with ease and flexibility.

📌 Features
✅ Fully Dockerized Setup – Run the entire web app using docker-compose.
✅ Reverse Proxy with Nginx – Handles routing smoothly.
✅ Modular Architecture – Separate services for frontend, backend, and proxy.
✅ Dynamic Content Handling – Backend API serving real-time updates.

📂 Folder Structure
/project-root ├── frontend/ # Frontend container with static HTML/CSS ├── backend/ # API handling dynamic content ├── proxy/ # Reverse proxy setup using Nginx ├── docker-compose.yml # Multi-container setup ├── README.md # Project documentation

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/Prasadpb77/basic-dynamic-website-on-docker.git
cd basic-dynamic-website-on-docker

```sh
docker-compose up -d --build