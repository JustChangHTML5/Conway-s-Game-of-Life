rm -rf dist build
#pyinstaller --onefile main.py
pyinstaller --onefile -w main.py
copy *.mp3 dist
copy *.gif dist