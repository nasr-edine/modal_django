# Django with modal form and docker

Basic authentication system in django with modal form for update email and docker files to run the app on docker

### Prerequisites

- Git, Docker
- Python interpreter, version 3.6 or higher

## Installation

clone repository locally

```bash
git clone https://github.com/nasr-edine/ayomi_project.git
```

Move to the ayomi_project root folder with:

```bash
cd ayomi_project
```

Create a virtual environment in root folder of project

```bash
python3 -m venv venv
```

Activate virtual environment

```bash
source ./venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Make Migration

```bash
django mm
```

Migrate

```bash
django m
```

You can create a super user in command line:

```bash
django csu
```

## Usage

You can run the Django Server:

```bash
django r
```

You can also run the app with docker

```bash
docker-compose up
```

Go to your browser to view django website with locahost URL
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

You can create a user with the URL below or click on signup button
[http://127.0.0.1:8000/users/signup/](http://127.0.0.1:8000/users/signup/)

After signup, you can login with your credentials (username and password)
[http://127.0.0.1:8000/users/login/](http://127.0.0.1:8000/users/login/)
