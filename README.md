# feature-request-app

The purpose of this app is to create and view data on feature requests

###Layout of App###
![alt tag](https://github.com/sudouser2010/feature-request-app/blob/master/layout.png)

###Demo of App###
http://216.158.228.203:8100

###How to deploy with Docker###
1. Get codebase with git clone <br>
git clone https://github.com/sudouser2010/feature-request-app.git

2. cd into the project <br>
cd feature-request-app

3. Build image from docker file <br>
sudo docker build -t feature-request-app .

4. Create a container from image <br>
sudo docker run -it -p 8100:8100 feature-request-app
