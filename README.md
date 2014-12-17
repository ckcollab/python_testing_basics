python_testing_basics
=====================

An example unit test, integration test and functional test using Python


Usage
=====

Setting up the repo and virtual environment:

    $ git clone git@github.com:ckcollab/python_testing_basics.git
    $ cd python_testing_basics
    $ mkvirtualenv python_testing_basics


Installing requirements

    $ pip install -r requirements.txt
    $ # make sure you have Firefox installed
    

Running tests (from directory you cloned)

    $ nosetests types\ of\ tests/**/*.py 


Useful libraries
================

### Unit testing

[nose](https://nose.readthedocs.org/en/latest/)
A test runner, collects all of your tests and has niceties for filtering/executing tests

[py.test](http://pytest.org/latest/)
Another test runner

[webtest](http://webtest.readthedocs.org/en/latest/)
Another test runner

[mock](https://docs.python.org/3/library/unittest.mock.html)
Helps create tests where certain conditions need to be faked


### Functional testing

[selenium](http://www.seleniumhq.org/)
Runs the web browser for functional tests, provides access to information about the browser

[ghost.py](http://jeanphix.me/Ghost.py/)
A headless web driver, no browser window will appear so tests can be much faster
