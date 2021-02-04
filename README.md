# Data analysis :
- Project: Hackathon -- _Hacking Educational Planning - IIPE-UNESCO x Latitudes_
- Description: Challenge #3 - Testing the use of inspection report textual data and modeling it in the form of thematic mapping to contribute to the improvement of the quality of education.
- Data Source: [Department of Education, Ireland](https://www.education.ie/en/Publications/Inspection-Reports-Publications/Whole-School-Evaluation-Reports-List?pageNumber=1)
- Type of analysis: Text mining, NLP, geospatial representation of text
- Links:
  - http://www.iiep.unesco.org/en/hacking-edplanning
  - https://www.eventbrite.fr/e/billets-hacking-educational-planning-iipe-unesco-x-latitudes-130771975499

# The approach

1. Scrape the PDF reports
2. Extract text from PDF
3. Use LDA to extract topics
4. Vizualize on a map

## Startup the project

### The initial setup.
Clone repo

```bash
mkdir ~/code/alexisgourdol
cd ~/code/alexisgourdol
git clone git@github.com:alexisgourdol/IIPE-hackathon.git
```

### Create virtualenv and install the project

Using `pyenv`
https://github.com/pyenv/pyenv#homebrew-on-macos

If you're on Windows, consider using @kirankotari's pyenv-win fork.
(pyenv does not work on windows outside the Windows Subsystem for Linux)

```bash
pyenv virtualenv IIPE # create a new virtualenv for our project
pyenv virtualenvs           # list all virtualenvs
pyenv activate IIPE   # enable our new virtualenv
pip install --upgrade pip   # install and upgrade pip
pip list                    # list all installed packages
```

### Install `requirements.txt` :

```bash
pip install -r https://raw.githubusercontent.com/alexisgourdol/IIPE-hackathon/master/requirements.txt
pip list
```

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
