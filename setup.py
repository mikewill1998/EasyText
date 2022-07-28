from setuptools import setup

APP = ['EasyText.py']
OPTIONS = {
    'iconfile': 'icon.png',
    'argv_emulation': True
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)