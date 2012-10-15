# mxit_ga - Google Analytics for Mxit

Python module to perform Google Analytics tracking for Mxit web applications.

Only tracking of page view events is currently supported.

## Installation

Clone the Git repository for the module. After the repository has been cloned it can be installed from the command line:

	python setup.py install

## Usage

### General

The tracker is instantiated with the Google Analytics tracking ID for the application and then used to track page view events. A basic example is given below: 

	from mxit_ga import MxitGa
	
	# instantiate tracker	
	ga = MxitGa(google_analytics_tracking_id)
	
	# track page view event
	ga.track_page(headers, remote_addr, host, path, query_string)

Where the following variables are defined:

* `google_analytics_tracking_id` - the Google Analytics tracking ID for the application. The tracking ID can either be of the form *UA-12345678-1* or *MO-12345678-1*.
* `headers` - a dictionary-like object containing the HTTP headers for the request.
* `remote_addr` - the IP address of the remote client.
* `host` - the hostname of the application server.
* `path` - the path to the requested page resource (this may already include the query string).
* `query_string` - the query string component of the URL (optional).

### Flask Web Framework

A decorator can be developed to easily track page views when using the [Flask](http://flask.pocoo.org) micro web framework for Python:

    from flask import request
    from functools import wraps
    from mxit_ga import MxitGa
	
    def track_page(f):
        """
        Decorator for tracking page views.
        """
        @wraps(f)
        def decorated_function(*args, **kwargs):
            ga = MxitGa('UA-12345678-1')
            ga.track_page(request.headers, request.remote_addr, request.host, request.path, request.query_string)
            return f(*args, **kwargs)
        return decorated_function

The decorator can then be used to track page views for any route, as follows:

	from flask import Flask, render_template

	app = Flask(__name__) # instantiate application

    @app.route('/')
    @track_page
    def index():
        """Index page"""
        return render_template('index.html')
