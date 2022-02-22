# YOUTUBE SEARCH API
## Problem Statement
Use the Youtube search API to get all the videos with query "Apple" and store it in a database. Make an endpoint to query the DB based on the video name. [Bonus: Implement fuzzy search]


## Implementation Checks
- Use the Youtube search API to get all the videos with query "Apple" ✔
- Store it in a database ✔
- Make an endpoint to query the DB based on the video name ✔
- Bonus: Implement fuzzy search ✔ 

## Table of contents
- [Preview](#preview)
    - [Search](#search)
    - [I'm Feeling Lucky](#im-feeling-lucky)
- [Requirements](#requirements)
- [Setting-up and Installation](#setting-up-and-installation)
    - [Cloning Repositary](#cloning-repositary)
    - [Setting-up a virtual environment](#virtual-environment)
    - [Installing Dependancies](#installing-dependancies)
    - [Setting-up Environment variables](#environment-variables)
    - [Migrating changes](#migrate-changes-in-database)
    - [Running the server](#run-the-server)
- [License](#license)




## Preview
### Search
Lists all the results where the keyword enter matches

![YoutubeAPI-search](assets/search.gif)

### I'm Feeling Lucky
Redirects to the first search result

![YoutubeAPI-im_feeling_lucky](assets/im_feeling_lucky.gif)

### Fuzzy Search
Getting results similar to search if exact match is not found.

![YoutubeAPI-fuzzy_search](assets/fuzzy_search.gif)



## Requirements
- [Python version 3+](https://www.python.org/downloads/)
- [PostgreSQL version 14](https://www.postgresql.org/download/)

> NOTE: If you do not wish to use PostgreSQL you can use [`version 1.0`](https://github.com/Dhruv9449/IEEE-recruitment/releases/tag/1.0v) without the **fuzzy search** functionality.  


## Setting up and Installation

### Cloning Repositary 
Clone this repositary by running in your terminal-
```
git clone "https://www.github.com/Dhruv9449/IEEE-recruitment"
```



### Virtual environment
After cloning the repositary install `virtualenv` set up a virtual environment using the following commands -  
```sh
pip install virualenv
virtualenv venv
``` 
Activate it -  
Windows
```psh
C:\Users\Username\dir> .\venv\Scripts\activate
```
Linux
```sh
user@hostname:~$ source venv/bin/activate
```
Refer to the [official virtualenv documentation](https://virtualenv.pypa.io/en/latest/) for any further help

> NOTE: Make sure you are in the `IEEE-recruitment/` folder while running this command



### Installing dependancies
To install all the dependancies for this project run the following command in your terminal - 
```sh
pip install -r requirements.txt
```



### Environment Variables 
You will need create a `.env` as shown in `.env.example` inside the `YoutubeSearch/` folder with 
- `Django Secret key` - can be anything you want. Create a unique one.
- `Youtube API key` - Your Youtube API key which will be required for getting youtube's data. You can get one from [Google's official website](https://console.developers.google.com/home/). For more info on the API you can refer [Google APIs github](https://github.com/googleapis/google-api-python-client). 
- `DB name` - Name of your database.
- `DB user` - PostgreSQL Username .
- `DB password` - Database password.
- `DB host` - Database host.
  
`.env` format
```
SECRET_KEY=<Your Django key>
YOUTUBE_API_KEY=<Your youtube API key>
DB_NAME=<postgres database name>
DB_USER=<postgres username>
DB_PASSWORD=<postgres database password>
DB_HOST=<postgres database hostname>
```



### Migrate Changes in database
Before you can get the server up and running you will have to migrate the changes made in the database. Run the following command -   
Windows
```psh
C:\Users\Username\dir> python manage.py migrate
```
Linux
```sh
user@hostname:~$ python3 manage.py migrate
```
> NOTE: Make sure you are in the `IEEE-recruitment/` folder while running this command



### Run the server!
We're all set the run the server now! Type the following command in your terminal -  
```
./manage.py runserver
```
or  
Windows
```psh
C:\Users\Username\dir> python manage.py runserver
```
Linux  
```sh
user@hostname:~$ python3 manage.py runserver
```
And then type `localhost:8000` or `127.0.0.1:8000` in your browser's search bar and voila!

> NOTE: Make sure you are in the `IEEE-recruitment/` folder while running this command



## License 
Copyright © 2022 Dhruv9449  
[MIT License](LICENSE)

<br>
<br>
<p align="center">
Developed by <a href="https://github.com/Dhruv9449" target=_blank>Dhruv Shah</a>
</p>
</p>