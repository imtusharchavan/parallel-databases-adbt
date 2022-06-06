# Parallel Databases

This is lab practical of Advanced Database Technology for implementing Parallel Databases.

## Getting Started

To run this project:

1. Clone the repository or Download ZIP.
2. Install Dependencies with `pip install -r requirements.txt`,
3. Create a new [postgresql](https://www.postgresql.org/download/) database and Configure the `SQLALCHEMY_DATABASE_URI` inside `app.py` file in both websites by providing the credentials of your newly created database.

### Website A

* Run `flask run` or `python app.py`.

It runs the app in development mode. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) to view it in the browser.

### Website B

As your `Website-A` will be running on port:`5000` you will need to run this `Website-B` on a different port like `8000`.

Run:

1.`export FLASK_RUN_PORT=8000`
2. `flask run`

It runs the app in development mode. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to view it in the browser.

                    You have successfully connected two websites to a single database!