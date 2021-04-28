# Language translator

Instantly translate texts, words, paragraphs from one language to another.
The objective of this project is to translate text content from one language to other language in real-time with a button click.

## Pre requisites

- [Python](https://www.python.org/downloads/) - 3.8.4 or up

### Pipfile and Pipfile.Lock

Inside the Pipfile there's all the modules name needed for the project.
Download Pipenv through the terminal window (make sure you have Python installed), just type `pip install pipenv`.

After installing pipenv all you have to do is to download the files and in the terminal window, got to the folder with these files and run `pipenv install` and automatically will install this modules.

This will create a virtual environment with the module `googletrans`.

To run this virtual environment all you must do is run `pipenv shell` and to close the virtual environment `exit`.

If any doubts here's a link to some more explanations:

- [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html)

## Run

- Download the project, open terminal window on folder with 'translator.py' and type:

```
pipenv shell
```
To activate the pipenv and then we can run:

```
python translator.py
```