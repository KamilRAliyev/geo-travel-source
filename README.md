# Steps to run project 

| No | Command | Description |
| --- | --- | --- |
| 1. | `python` | Open Python REPL |
| 2. | `import socket` | Import socket package |
| 3. | `socket.gethostname()` | Get your hostname |
| 4. | | Change `kamil-KLV-WX9` to `your hostname` in `geotravel/settings/__init__.py` file |
| 5. | `python -m venv venv` or `python3 -m venv venv` | Create virtual environment for project |
| 6. | `source venv/bin/activate` for windows: `venv/Scripts/Activate.bat` | For activating venv |
| 7. | `pip install -r requirements.txt` or `pip3 install -r requirements.txt` | Install dependencies |
| 8. | `python manage.py make migrations && python manage.py migrate` | Creating local `db.sqlite3` db |
| 9. | `python manage.py runserver 8000` | Running web server |

---
# For seeing coverage:

1. Go to [here](https://kamilraliyev.github.io/geo-travel-source/index.html)
2. Search for `tours`