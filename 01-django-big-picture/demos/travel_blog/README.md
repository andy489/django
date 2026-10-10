# Django: The Big Picture

There's a commit for each module in the course, as well as a tag:

# Setup instructions

# 1. Create and activate a virtual environment

How to do this depends on your system; depending on your IDE this may not be necessary.

If you don't know how to do this: see my course [Development Environments and Package Management in Python 3](https://www.pluralsight.com/courses/python-3-development-environments-package-management)

# 2. Install dependencies

Inside the project, run `python -m pip install -r requirements.txt`.

#3 4. Move into the travel_blog folder

You want to be in the folder where the file `manage.py` is.

To get there, You probably need to run `cd travel_blog`.

But watch out: there are two of those and you want to be in the
*outer* travel_blog folder. If you end up 1 level too deep, run
`cd ..` to move up 1 level.

## 5. Run the project

The command for this is `python manage.py runserver`.

You can now view the project at http://localhost:8000

If this does not work, you are probably not in the correct folder.