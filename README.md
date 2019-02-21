# Deployment

## Manual steps for windows
* Requires git, python 3+, and pip to be in system path 

`> git clone "http://github.com/JeffreyCowley/blog-post-challenge"`

`> cd blog-post-challenge`

`> python -m venv env`

`> env\Scripts\activate.bat`

`> pip install -r requirements.txt`

`> python BlogPostAPI.py`

## Manual steps for linux
* CentOS 7
* Requires git, python 3+, and pip to be in system path 

If python 3.6 is not already installed
use the next line to install python 3.6

`$ sudo yum install python36 python36-pip`

`$ git clone "http://github.com/JeffreyCowley/blog-post-challenge"`

`$ cd blog-post-challenge`

`$ pip3.6 install virtualenv`

`$ virtualenv env`

`$ source env/bin/activate`

`$ pip3.6 install -r requirements.txt`

`$ python3.6 BlogPostAPI.py &` 



# Configuraton File

`[Database]`

`file=blog.db`
* If file is not found service will fail to start

`[Logging]`

`file=log/BlogPostApp.log` 

* Path will attempt to be created, if file can't be created or is empty turns logging off

`format=%(asctime)s %(levelname)s - %(module)s - %(message)s`

* Defaults to '%(asctime)s - %(name)s - %(levelname)s - %(message)s' if not supplied 

`level=DEBUG`

* Defaults to 'WARNING' if not a valid logging level


`[API]`

`port=5051`
 * defaults to 5000