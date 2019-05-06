# Industry Sector Employment and Stock Data- Dash Visualization Testing App

[TOC]



# Installation

package require for running this app: dash, pandas, plotly

## Run app locally using Anaconda

1. To run this app locally, open Anaconda and terminal of the environments of your choice

2. cd to file folder and type:

```
python apptesting.py
```

3. Open a browser and the app will be shown at: localhost:8050

## Deploy App to Heroku:

prerequisite: python 3.0+, a Heroku account

1. Download and install Heroku Command Line Interface(CLI)

2. Open cmd and login to Heroku:

   ```
   heroku login
   ```
3. Download the files to a folder for this project.

4. initialize the folder with git and virtualenv

```
git init
virtualenv venv
```

if *'virtualenv' is not recognized as an internal or external command, operable program or batch file.*, then `pip install virtualenv`

5. install gunicorn - `pip install gunicorn`

6. create a *.gitignore* file. The content of this file:

   ```
   venv
   *.pyc
   staticfiles
   .env
   db.sqlite3
   ```

7. Create a *Procfile* file. The content of this file:

```
web: gunicorn apptesting:server
```

*apptesting* is the file name of the app - *apptesting.py* 

inside *apptesting.py*, a variable `server` is defined as `server = app.server`

8. Create a *requirements.txt* file. This file contains the required package names to run this app:

   ```
   django
   gunicorn
   django-heroku
   dash
   pandas
   plotly
   ```

9. go back to cmd, type:

      ```
      heroku create my-dash-app # change my-dash-app to a unique name
      git add . # add all files to git
      git commit -m 'Initial app boilerplate'
      git push heroku master # deploy code to heroku
      heroku ps:scale web=1  # run the app with a 1 heroku "dyno"
      
      ```

10. The cmd window will show the weblink of this app.
11. To updae the code and redeploy, after modifying apptesting.py file:

      ```
      
      git add .  # add all the changes
      git commit -m 'a description of the changes'
      git push heroku master
      ```

## Remove the app

To remove the app, login Heroku and go to:https://dashboard.heroku.com/apps

Select the app and go to setting, the delete option is at bottom

# Project Description

My first Dash app practice case and first heroku deployment. The app contains two visualizations from a proposed project. The dataset used in this project  tracks and records the number of employees across companies on daily basis from LinkedIn. The projects aims to gain real time insight into how aggressively each industrial sector is growing and exam whether the number of employees can reflect the variation on sector ETF price. 

The app contains part of the results from data exploration stage of this project. In this result, user can easily  access and visualize the average employees , average followers per company of each sector in the first plot. In addition, the daily trading volume, daily adjusted close price, volatility and daily percentage change of each sector ETF are visualized in the second plot. 

This raw dateset can be downloaded from: https://s3-us-west-2.amazonaws.com/documents.thinknum.com/dataset_dump/flikerqvnk/temp_datalab_records_linkedin_company.zip

# File descriptions

Folder ETL: contain the ETL code for raw data

.gittignore, Procfile, requirements.txt  described in installation

apptesing.py  python file that contains the code for this app

# Results

https://linkedin-data-testing.herokuapp.com/



# Licensing, Authors, Acknowledgements

Author Haochen X([jbdx6307@gamil.com](mailto:jbdx6307@gamil.com))