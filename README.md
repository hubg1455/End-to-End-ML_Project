# End-to-End-ML_Project

Creating conda environment
'''
conda create -p venv python==3.7 -y
'''
'''
conda activate venv/
'''
OR 
'''
conda activate venv
'''

'''
pip install -r requirements.txt
'''

To Add files to git
'''
git add .
'''

OR
'''
git add <file_name>
'''
'''
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file
'''
To check the git status 
'''
git status
'''
To check all version maintained by git
'''
git log
'''

To create version/commit all changes by git
'''
git commit -m "message"
'''

To send version/changes to github
'''
git push origin main
'''

To check remote url 
'''
git remote -v
'''

BUILD DOCKER IMAGE
'''
docker build -t <image_name>:<tagname> .
'''

To list docker image
'''
docker imges
'''

Run docker image
'''
docker run -p 5000:5000 -e PORT=5000 <imageid>
'''

To check running container in docker
'''
docker ps
'''

To stop docker container
'''
docker stop <container_id>
'''

'''
python setup.py install
'''

'''
pip install ipykernel
'''

'''
pip install pyYAML
'''

'''
when dataset stats gets change is called data drift
'''