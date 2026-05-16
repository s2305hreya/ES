1. Install Docker Desktop

2. Fix WSL (If Needed)
Open PowerShell as Administrator and run:

wsl --update

Restart computer.

3. Open Docker Desktop

4. Create Project Folder

5. Open Folder in VS Code

6. Create index.html

7. Create Dockerfile

8. Open VS Code Terminal

9. Build Docker Image

Run:

docker build -t mydockerapp .

10. Run Docker Container

Run:

docker run -d -p 8080:80 --name mycontainer mydockerapp

11. Check Running Container

Run:

docker ps

12. Open Website

Open browser and go to:

http://localhost:8080

13.  Useful Docker Commands

Stop Container
docker stop mycontainer

Start Container
docker start mycontainer

Remove Container
docker rm mycontainer

View Docker Images
docker images

View All Containers
docker ps -a



