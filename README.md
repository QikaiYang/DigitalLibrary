## Qikai's digital library
This is Qikai's digital library on books of Goodreads based on scrappers. Current version of database supoorts 3 functions.
1. Scraping data given user-specified number of books and authors (recommend less than 200 books and less than 50 authors)
2. Export scrapped data
3. Import a json file to the database
4. Send a query and return a list of books/authors 
5. Visit a simple API of my database

The database is on firebase

## How to Start
Here is a quick introduction on how to start the program.

### Step 1 - Prerequisites
To make sure this program gets executed well, here are some prerequisites that need to be followed on the machine.

#### Development Environments
```
Linux system
PyCharm
Python 3.7
```

#### Main python library
```
firbase and its dependency
beautiful soup 4 and its dependency
```

### Step 2 - Download 
You can choose to download the .zip file directly or use the command below to download the source files of the game
```
git clone https://gitlab.engr.illinois.edu/qikaiy2/sp21-cs242-assignment2.git
```

### Step 3 - Execute
Unzip the .zip file and open ~/src/Main/Main.py in studio and execute it.

## API support
My API support 4 kinds of query - PUT, GET, DELETE, POST. THe formats are as below:

1. POST - ~/books/post `OR` ~/authors/post
2. GET - ~/books `OR` ~/authors
3. DELETE - ~/books/delete `OR` ~/authors/delete
4. PUT - ~/books/put `OR` ~/authors/put
