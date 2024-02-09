# VIPVoyage

# Steps to Execute the App

This guide provides step-by-step instructions to set up and run the Flask application detailed in the provided Python script. Follow these steps to get the application up and running on your local machine.

**Step 1:** Create and activate a virtual environment for Python to manage dependencies:

```console
python3 -m venv venv
source venv/bin/activate  # On Unix/macOS
```

**Step 2:** Install the necessary Python packages using the requirements file. Ensure you have a `requirements.txt` file or manually install the packages listed in the provided script:

```console
(venv) $ pip install Flask SQLAlchemy Flask-Session WTForms Flask-Migrate
```

**Step 3:** Initialize your database. This step involves creating the tables and structures necessary for your Flask application to interact with the database:

```console
(venv) $ flask db init
(venv) $ flask db migrate -m "Initial migration."
(venv) $ flask db upgrade
```

**Step 4:** Run the Flask application. Ensure the `FLASK_APP` environment variable is set to your main application file (`app.py` if your main file is named so):

```console
(venv) $ export FLASK_APP=app.py  
(venv) $ flask run --reload
```

This command starts a local development server and watches for changes in your source code, reloading the server automatically.

**Step 5:** Access the application in your web browser. Once the server is running, you can visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the application's home page.

**Step 6:** Explore the application's features. Use the various routes and functionalities defined within your Flask application to test its capabilities.

---

By following these steps, you'll have a Flask web application running on your local development server, ready for further development or testing.