# Gotofritz Fund Manager

A simple [Django](https://www.djangoproject.com/) application to manage funds imported from a CSV file.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Tasks](#tasks)
- [License](#license)

## Description

This app consists of a single page at the root, which in local mode would be accessed at <http://127.0.0.1:8000/>. There you will be able to:

- view a list of funds
- filter the list of fund by Strategy
- replace the list with a new one by uploading a csv file with fields in the format `Name,Strategy,AUM (USD),Inception Date`. Uploading is open without needing to authenticate.

The application offers an (unsecured) API endpoint for querying to funds

- <http://127.0.0.1:8000/api/funds/> will return a list of funds
- <http://127.0.0.1:8000/api/funds/?strategy=__STRATEGY__> will filter the list by strategy, which can be one of "Arbitrage", "Global Macro", or "Long/Short Equity" (NOTE: in a real life scenario the strings would be replaced with shorter tokens)
- <http://127.0.0.1:8000/api/fund/X/> will return detail of a single fund with id X

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

The project includes a set of tasks for the [Task](https://taskfile.dev/) task runner tool. They are defined in the [Taskfile](Taskfile.yml) and cover linting, testing, code formatting, and more. They are not a hard requirements, but they provide some useful shortcuts. See the Task documentation for [installation instructions](https://taskfile.dev/installation/)

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

One of the tasks is a sample unit test suite, just as illustration

```
task test
```

## Other assets

There is a scripts folder with some test csv data and a quick script to generate more.

## License

This project is licensed under the [MIT License](LICENSE).
