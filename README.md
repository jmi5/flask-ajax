# flask-ajax

This repo contains two projects:
- Working on getting this http://codehandbook.org/python-flask-jquery-ajax-post/ to work.
- Getting a public facing TIP endpoint so people can demo entering an IP and UA into a box and sending to TIP. 

### Run Instructions
- To run locally: `python app.py` and then visit the localhost address the app is running on. 
- To do Heroku things:
	- Check if there are any dynos allocated to your Heroku app: `heroku ps`
	- If not: up it by 1: `heroku ps:scale web=1`
	

### Notes
- At the beginning of the project, run `virtualenv env`.
	+ This creates the virtual environment that you will ship with your project. 
- After installing the necessary packages run `pip freeze > requirements.txt`
- Does there need to be a `setup.py` script? 
- Heroku only officially supports two runtimes: https://devcenter.heroku.com/articles/python-runtimes
- Need a Procfile

### Static Assets with Flask

Referred to: http://exploreflask.com/en/latest/static.html
