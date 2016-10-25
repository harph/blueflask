# Blue Flask

Flask boilerplate to create projects with the idea of pluggable blueprints.


## Installation

```
pip install blueflask
```

## Usage

The following command allows you to create a new app:

```
blueflask newapp <APP_NAME> <OPTIONAL_DEST_DIRECTORY>
```

## Tutorial

Let's assume that we are going to start a project called *bluedemo*. Execute
on your terminal:

```
blueflask newapp bluedemo
```

This will create a directory with the name of the project and define a basic
structure for your project layout.

Next, go inside the directory of your project and install the dependencies.
If you are using *virtualenv* then, create and/or activate your environment
before executing the following command bellow install your dependencies.

```
pip install -r requirements.txt
```

Now your project is ready to run. Execute the following command to start
the server:

```
python run.py
```

Or you can run it as an executable file:

```
./run.py
```

Or you can execute one of the Flask standard ways to run the application:

```
export FLASK_APP=run.py
flask run
```

Or:

```
python -m flask run
```

Either one will start the application running on port 5000. Now you can go to
your browser and enter:
[http://localhost:5000/](http://localhost:5000/)

[http://localhost:5000/demo/](http://localhost:5000/demo/)

You can play with some URLs like: [http://localhost:5000/demo/about/?value=some_random_value](http://localhost:5000/demo/about/?value=some_random_value)

As you can see, the last two URLs have a */demo* prefix. This is defined in the *blueprints/demo/config.py* file by the *url_prefix* under the *BLUEPRINT_INIT* dictionary. You can change the value of this for whatever you want or set it to *None* if you don't want any prefix.


## Understanding Your Application

Now that you have your application running, have a look to the basic architecture defined by Blue Flask. Look inside the *app/blueprints*
directory. As you can see, there is a *main* and a *demo* directory. These directories are consider *pluggable-blueprint*, according to the Blue Flask idea. The structure of this directory is pretty simple:

+ *__init__.py:* Makes the current directory a Python package.
+ *config.py:* Blueprint specific settings and definitions.
+ *urls.py:* Routes for that blueprint.
+ *views.py* Functions or classes in charge of handing requests.

Feel free to define more modules as you need them. I.e: *models.py*,
*service.py*, *utils.py*, etc.


### Creating A New Blueprint.

To create a new blueprint, you just have to create a new directory inside
the *blueprints* directory.
