# Steps to run project 

| No | Command | Description |
| --- | --- | --- |
| 1. | `python` | Open Python REPL |
| 2. | `import socket` | Import socket package |
| 3. | `socket.gethostname()` | Get your hostname |
| 4. | | Change `kamil-KLV-WX9` to `your hostname` in `geotravel/settings/__init__.py` file |
| 5. | `python -m venv venv` or `python3 -m venv venv` | Create virtual environment for project |
| 6. | `source venv/bin/activate` for windows: `venv/Scripts/activate` | For activating venv |
| 7. | `pip install -r requirements.txt` or `pip3 install -r requirements.txt` | Install dependencies |
| 8. | `python manage.py make migrations && python manage.py migrate` | Creating local `db.sqlite3` db |
| 9. | `python manage.py runserver 8000` | Running web server |

---
# For seeing coverage:

1. Go to [here](https://kamilraliyev.github.io/geo-travel-source/index.html)
2. Search for `tours`

---
# For running tests:

## Step 1. Installation dependencies and virtual environment
| No | Command | Description |
| --- | --- | --- |
| 1. | `python` | Open Python REPL |
| 2. | `import socket` | Import socket package |
| 3. | `socket.gethostname()` | Get your hostname |
| 4. | | Change `kamil-KLV-WX9` to `your hostname` in `geotravel/settings/__init__.py` file |
| 5. | `python -m venv venv` or `python3 -m venv venv` | Create virtual environment for project |
| 6. | `source venv/bin/activate` for windows: `venv/Scripts/activate` | For activating venv |
| 7. | `pip install -r requirements.txt` or `pip3 install -r requirements.txt` | Install dependencies |

## Step 2. Running Tests
1. Close all `terminals` and `vscode` in order to dependency installation finish
2. Open `terminal` and activate virtual environment.
3. Run command:
    - `python manage.py test tours -v 2` - for testing.
    - `coverage run --branch --omit="*/venv/*," manage.py test -v 2 && coverage html -d docs` - testing & covarage report