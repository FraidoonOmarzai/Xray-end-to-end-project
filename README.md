<h1 align=center>Xray End-To-End Project</h1>

**Implementation of computer vision project on Xray dataset, using PyTorch framework for training the model**


## Steps:

1. Git clone the repository and Define template of the project

```bash
touch template.py # create the template.py file in linux 
python3 template.py
```

2. define setup.py scripts (**The setup.py** is a module used to build and distribute Python packages. It typically contains information about the package)


3. Create environment and install dependencies

```bash
conda create -n cv-env python=3.9 -y
conda activate cv-env
pip install -r requirements.txt
```

4. define logger (**The Logging** is a means of tracking events that happen when some software runs)

5. define utils (**The utils.py** makes it easy to execute common tasks in Python scripts)


```bash
# WORKFLOWS
- update the constants
- updata the artifact_entity
- update the config_entity
- update the components
- update teh pipeline
- update the dvc.yaml
```

6. **Data Ingestion**
- Adding data from local disk to S3, define IAM user, aws configure 
- adding cloud_storage/s3_operations.py
- We will download the data from AWS S3 to our local disk and the fun for vice versa
- adding dvc to run the pipeline

7. **Data Transformation**
- we will use torchvision.transforms
- we will use dataloader and return the dataset

8. **Model Training**
- run the training pipeline

9. **Model Evaluation**

10. **Model Pusher**
- not completed yet

11. **Streamlit**
- install streamlit
- add code to app.py
- copy the save model to a new directory `model/model.pt`

12. **Adding docker images**
- adding code to docker file
- buid the docker image
```bash
docker build -t xray .
docker ps
docker images
```
- running our app using docker
```bash
docker run -p 8080:8080 xray
```
- open the browser and run
```bash
htpp://localhost:8080
```

13. **Deploying the project using CI/CD**
- first deploy the project to docker-hub and then to ec2

###############AWS Section################

**Note:** we will deploy AWS-CICD using Github-Actions

```bash
# AWS 
13.1. Login to AWS console
13.2. Create IAM user with ec2fullaccess
13.3. Create EC2 : It is virtual machine and install docker in EC2
#optinal
sudo apt-get update
sudo apt-get upgrade -y

#required
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
```

13.4.  Configure EC2 as self-hosted runner:
```bash
setting-->actions-->runner-->new self hosted runner--> choose os--> copy each command and run it on EC2 Instance Connect
```

- Setup github secrets:
```bash
# Docker secret
DOCKER_USERNAME=fraidoonjan
DOCKER_PASSWORD=...

REGISTRY=fraidoonjan
IMAGE_NAME=xrayapp

# AWS secret
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_REGION=eu-west-2
```
