try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'My projects',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requrires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectename'
}  


setup(**config)