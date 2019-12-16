# data test

## Description
Data test has two simple applications, one which transfers the data from the csv into the database. 
The other application displays the data from the database.

This data is first cleaned before its loaded into the database.

### Built with
Python 3.6, Flask micro-framework and SQLite database.

### Installation
Create and activate a virtual environment.

In the virtual environment, clone the repository.
<pre>
git clone https://github.com/peterwade153/data-test.git
</pre>

Install required dependencies.
<pre>
pip install -r requirements.txt
</pre>

### To run the application that transfers data into the database
<pre>
python seed_data.py
</pre>

### To run the web application
<pre>
python app.py
</pre>

To access the application, in the browser head over to http://localhost:5000/

Design decision are included in the `design decison` file.
