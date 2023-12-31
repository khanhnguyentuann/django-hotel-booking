# Hotel Management

Welcome to the Hotel Management project! This is a Django web application that allows users to manage room booking for a hotel.

## Installation

Before starting, make sure you have Python, pip, and virtualenv installed on your machine.

### Clone the project

First, clone the repository to your local machine:

```bash
git clone https://github.com/khanhnguyentuann/hotel_management.git

## Setup Virtual Environment

### Navigate to the project directory:

```bash
cd hotel_management

Then create a virtual environment and activate it:

On Windows:

python -m venv env
env\Scripts\activate
On Unix or MacOS:

python3 -m venv env
source env/bin/activate

## Database Migration
Make sure you are in the project root (where manage.py is), then run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate

## Create Admin User
In order to access the admin site, create a superuser:

```bash
python manage.py createsuperuser

You'll be asked to enter a username, email (optional), and password.

## Running the Server

Finally, you're ready to start the server:

```bash
python manage.py runserver