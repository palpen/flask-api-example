# Flask RESTful API example
_(This repo is part of our [Free Flask Tutorial](https://flask-tutorial.com))_

This repo shows how to create a simple RESTful API using the Flask web framework. Among the included features, you'll see how to:
* Return custom status codes and headers ⚡️
* Create resources using POST requests 📬
* Deleting resources using DELETE requests 📭
* Test the application using Flask's [test client](http://flask.pocoo.org/docs/latest/testing) 🔮

**There's a detailed video lesson on how to perform the deploy in our [Free Flask Tutorial](https://flask-tutorial.com).**

## Install guide

##### Clone the repo

```bash
$ git clone https://github.com/rmotr/flask-api-example.git
$ cd flask-api-example
```

##### Create the virtualenv
```bash
$ mkvirtualenv flask-api-example
```

##### Install dependencies
```bash
$ pip install -r requirements.txt
```

##### Run the app
```bash
$ python run_app.py
```

## Running the app

```bash
# Step 3 requires a DB created
$ sqlite3 library.db < library-schema.sql
$ python run_app.py
```


## Test

```bash
$ make test
```

## License scope

The [MIT License](LICENSE) covers Palermo Penano's original contributions identified in [LICENSING.md](LICENSING.md). Inherited upstream code and documentation, other authors' contributions, and third-party material retain their own rights and are excluded from that grant. Please read the scope notice before reusing the complete project.
