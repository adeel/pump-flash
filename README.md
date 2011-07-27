# pump-flash

`pump-flash` is a [Pump](http://adeel.github.com/pump) middleware for adding flash message support via sessions.  It requires you to be using the [`pump.middleware.session`](https://github.com/adeel/pump/blob/master/pump/middleware/session.py) middleware already.

## Installation

To install, type

	$ pip install pump-flash

or to grab it from GitHub:

	$ git clone git://github.com/adeel/pump-flash.git
	$ cd pump-flash
	$ python setup.py install

## Usage

Just wrap your app with `pump_flash.wrap_flash`.

Before your app is called, the middleware adds a `flash` key to the request that contains the current flash dict.  Then your app is called, and the session is updated to the new value of `request["flash"]`.  Note that `request["flash"]` is actually a dict-like object whose values disappear after the first access.