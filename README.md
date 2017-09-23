# mos-polytech [![Build Status](https://travis-ci.org/mos-polytech/homework-template.svg?branch=master)](https://travis-ci.org/mos-polytech/homework-template)

Year: 2017

![mos-polytech](https://raw.githubusercontent.com/mos-polytech/2017/master/media/logo.jpg)


## Purpose

This package contains an example homework for our students.


## How to submit a homework

1. Create a fork of this repository
2. Create a new brunch named `feature-homework-${NUMBER}` (this number should equal to the homework's number)
3. Register on [`travis`](https://travis-ci.org/)
4. [Enable](https://docs.travis-ci.com/user/getting-started/) your repo on `travis`
5. Create pull request to *your* `master` branch from *your* `feature-homework-${NUMBER}` branch
6. Make sure a `travis` build passes
7. Then post a link to our [`gitter`](https://gitter.im/sobolevn/mos-polytech) channel
8. Your homework will be reviewed


## Requirements

You will need:

- `python` version `3.6`
- `editorconfig` plugin for your editor


## Running tests locally

If you ever wish to run our tests locally you will need:

- `pipenv` installed and configured

Then execute:

- `pipenv install -d`
- `pipenv shell`
- `pytest`

You are all done.
