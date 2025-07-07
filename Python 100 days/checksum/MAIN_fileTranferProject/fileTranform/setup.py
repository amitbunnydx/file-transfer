

from setuptools import setup

APP = ['main.py']
DATA_FILES = [
    ('', ['generate.png', 'tomato_bg.png']),
]
OPTIONS = {
    'argv_emulation': True,
    'packages': [],
    'iconfile': 'icons_checksum.icns',  # Optional icon
    'includes': ['hashlib', 'tkinter', 'threading', 'logging', 'os', 'json', 'shutil', 'time', 'platform'],
    # 'excludes':['setuptools'],
    'plist': {
        'CFBundleName': 'Checksum Validator',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleIdentifier': 'com.example.checksumvalidator',
    }
}

setup(
    app=APP,
    name='Checksum Validator',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
