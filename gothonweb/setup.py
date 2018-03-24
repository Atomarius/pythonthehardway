try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose', 'web'],
    'packages': ['gothonweb'],
    'scripts': [],
    'name': 'Gothons From Planet Percal #25'
}

setup(**config)
