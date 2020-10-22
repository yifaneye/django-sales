import pathlib

from setuptools import setup

CWD = pathlib.Path(__file__).parent
README = (CWD / "README.md").read_text()

setup(
    name='django-sales',
    version='0.0.1',
    description='Display different contact details based on query parameter and cookie',
    py_modules=['sales'],
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description='Display different contact details depending on query parameter',
    url='https://github.com/yifaneye/django-sales',
    author='Yifan Ai',
    author_email='yifanai@aol.com'
)
