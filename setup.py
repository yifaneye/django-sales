import pathlib

from setuptools import setup

CWD = pathlib.Path(__file__).parent
README = (CWD / "README.rst").read_text()

setup(
    name='django-sales',
    version='0.1.0',
    description='Display different contact details based on query parameter and cookie',
    py_modules=['sales'],
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description=README,
    long_description_context_type='text/markdown',
    url='https://github.com/yifaneye/django-sales',
    author='Yifan Ai',
    author_email='yifanai@aol.com'
)
