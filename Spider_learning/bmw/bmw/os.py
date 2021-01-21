
import os

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "images")
if not os.path.exists(path):
    os.makedirs(path)

