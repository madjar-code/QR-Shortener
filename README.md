﻿# QR-Shortener

# About
My project is to shorten links and generate QR-codes.The API allows you to shorten a single link, shorten multiple links from an excel spreadsheet, generate images from shortened links, track progress


# Installations
1. Clone the repository.
```
git clone https://github.com/madjar-code/QR-Shortener
```

2. Create a virtual enviroment:
```
python -m venv venv
```

3. Install all dependencies while in a virtual environment:
```
pip install -r requerements.txt
```

4. After run migrations for each of the applications
```
py manage.py makemigrations some_app_name
```

5. And now:
```
py manage.py migrate
```

6. Now you can start the server and get RESTful API documentation to the localhost:8000/swagger/
