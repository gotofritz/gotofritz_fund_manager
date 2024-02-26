# Gotofritz Fund Manager

A simple [Django](https://www.djangoproject.com/) application to manage funds imported from a CSV file.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks](#tasks)
- [License](#license)

## Description

This app consists of a single page at the root, which in local mode would be accessed at <http://127.0.0.1:8000/>. The admin app is site is disabled for security reasons. There you will be able to:

- view a list of funds
- filter the list of fund by Strategy
- replace the list with a new one by uploading a csv file with fields in the format `Name,Strategy,AUM (USD),Inception Date`

## Installation

To set up the app follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/gotofritz/gotofritz_fund_manager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd gotofritz_fund_manager
   ```

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Install the test dependencies:

   If you are planning to run tests or code quality tools, you will need to install the test requirements too

   ```bash
   pip install -r requirements.txt  -r requirements-test.txt
   ```

## Tasks

The project includes a set of tasks for the [Task](https://taskfile.dev/) task runner tool. They are defined in the [Taskfile](Taskfile.yml) and cover linting, testing, code formatting, and more. They are not a hard requirements, but they provide some useful shortcuts. See the Task documentation for [isntallation instructions](https://taskfile.dev/installation/)

## Usage

The app can be run with one of the following commands:

```bash
# if you have installed Task
task run

# Linux / OS X
DJANGO_SETTINGS_MODULE=gotofritz_fund_manager.settings.local ./manage.py runserver

# Windows CMD
set DJANGO_SETTINGS_MODULE=gotofritz_fund_manager.settings.development
python manage.py runserver

# Windows PowerShell
$env:DJANGO_SETTINGS_MODULE="gotofritz_fund_manager.settings.development"
python manage.py runserver
```

The following Task command will show you a list of code quality commands you can run

```
task
```

## Other assets

There is a scripts folder with some test csv data and a quick script to generate more.

## License

This project is licensed under the [MIT License](LICENSE).
