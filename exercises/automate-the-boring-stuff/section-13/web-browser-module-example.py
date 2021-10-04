import webbrowser
import sys
import pyperclip

# ["web-browser-module-example.py", "4343", "Integrity Center", "Point"] ->
# 4343 Integrity Center Point
sys.argv

# Check if command line arguments were passed

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/4343+Integrity+Center+Point,+Colorado+Springs,+CO+80917
# https://www.google.com/maps/place/ADDRESS
webbrowser.open("https://www.google.com/maps/place/" + address)
