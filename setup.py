import pathlib

from setuptools import setup

CWD = pathlib.Path(__file__).parent
README = (CWD / "README.rst").read_text()

setup(
    name='django-sales',
    version='0.1.1',
    description='Display different contact details based on query parameter and cookie',
    packages=["src/sales", "src/sales/middleware", "src/sales/templatetags"],
    include_package_data=True,
    install_requires=["Django"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description=README,
    long_description_content_type='text/x-rst',
    url='https://github.com/yifaneye/django-sales',
    author='Yifan Ai',
    author_email='yifanai@aol.com'
)
