# mos-polytech [![Build Status](https://travis-ci.org/mos-polytech/homework-template.svg?branch=master)](https://travis-ci.org/mos-polytech/homework-template)

Year: 2017

![mos-polytech](https://raw.githubusercontent.com/mos-polytech/2017/master/media/logo.jpg)


## Purpose

This package contains an example homework for our students.


## How to submit a homework

We work in a single repository, if you have ever created one, stick to it. There's no need to delete or recreate it, just update it before every homework.

### New repository

1. Create a fork of this repository
2. Create a new branch named `feature-homework-${NUMBER}` (this number should equal to the homework's number)
3. Register on [`travis`](https://travis-ci.org/)
4. [Enable](https://docs.travis-ci.com/user/getting-started/) your repo on `travis`
5. Create pull request to *your* `master` branch from *your* `feature-homework-${NUMBER}` branch
6. Make sure a `travis` build passes
7. Then post a link to our [`gitter`](https://gitter.im/sobolevn/mos-polytech) channel
8. Your homework will be reviewed

### Updating existing repository

1. If your fork already exists, [sync](https://help.github.com/articles/syncing-a-fork/) it with the [this](https://github.com/mos-polytech/homework-template) repository
2. If you have any approved pull-requests for your previous homeworks, merge them into `master`

### Getting help

If you have any problem with submission see [tutorial](how-to-submit-hw.md) or ask question in [`gitter`](https://gitter.im/sobolevn/mos-polytech) channel

## Requirements

You will need:

- `python` version `3.6`
- `editorconfig` plugin for your editor


## Running tests locally

If you ever wish to run our tests locally you will need:

- `pipenv` installed and configured

Then execute:

1. `pipenv install -d`
2. `pipenv shell`
3. `python -m pytest`

You are all done.
