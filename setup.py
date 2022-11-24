from distutils.core import setup
import py2exe
setup(
    windows = [
        {
            "script": "Pi Machine Remastered.py",
            "icon_resources": [(1, "favicon.ico")]
        }
    ],
) 