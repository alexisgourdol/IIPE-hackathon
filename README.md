# Data analysis
- Document here the project: Hacking Educational Planning - IIPE-UNESCO x Latitudes
- Description: Le Hacking Ed Planning est ouvert à toutes et tous. Plus précisément
si vous avez des compétences en data science, data analyse, IA, NLP, dataviz, UX/UI,
 dev (front et/ou back), gestion de projet (PM/PO), votre engagement sera pour nous
 une aide très précieuse !
- Data Source: TBD
- Type of analysis: TBD

Please document the project the better you can.

# Startup the project

### The initial setup.
Clone repo using ssh

"""
mkdir ~/code/lisbonne21
cd ~/code/lisbonne21
git clone git@github.com:lisbonne21/IIPE-data.git
"""

### Create virtualenv and install the project

Using `pyenv`
https://github.com/pyenv/pyenv#homebrew-on-macos

If you're on Windows, consider using @kirankotari's pyenv-win fork.
pyen(pyenv does not work on windows outside the Windows Subsystem for Linux)

"""
pyenv virtualenv lisbonne21 # create a new virtualenv for our project
pyenv virtualenvs           # list all virtualenvs
pyenv activate lisbonne21   # enable our new virtualenv
pip install --upgrade pip   # install and upgrade pip
pip list                    # list all installed packages

"""


### A minimal `requirements.txt` to start working quickly :

"""
pip install -r https://gist.githubusercontent.com/krokrob/53ab953bbec16c96b9938fcaebf2b199/raw/9035bbf12922840905ef1fbbabc459dc565b79a3/minimal_requirements.txt
pip list
"""

### Process / Best practices

1. Make sure your git status is clean
`git status`

2. Get latest master
`git checkout master`
`git pull origin master`


3. 1 task = 1 branch
`git checkout -b my-task`
Work on the existing files, or create new ones
`git add .`
`git commit -m "This is an informative message about my-task" `
`git push origin my-task`

4. Create a pull request
Use the website
Click on compare & pull request

5. Someone else Reviews and Approves the pull request

6. Remove unused branches locally
`git sweep`
