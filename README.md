# django-sales

django-sales is a Django app for displaying different contact details based on query parameter (with cookie).
It provides sales, partners and affiliates custom links to send out to the public.
It gives sales, partners and affiliates their opportunity to convert every contact detail on the website to their own.
It thus encourages sales, partners and affiliates to promote the website and the business. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django-sales.

```bash
pip install django-sales
```

## Usage

### Step 1. Add sales app (in settings.py file)
```python
INSTALLED_APPS = [
    '...',
    'django.contrib.staticfiles',
    'sales',  # here 
    'myapp',
    '...',
]
```

Make sure sales app is before all custom apps. 
Otherwise, Django will not recognize the 'sales' template tag.

### Step 2. Add sales middleware (in settings.py file)
```python
MIDDLEWARE = [
    'sales.middleware.sales.SalesMiddleware',  # here 
    'django.middleware.security.SecurityMiddleware',
    '...'
]
```

### Step 3. Add sales context processors (in settings.py file)
```python
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                '...',
                'django.contrib.messages.context_processors.messages',
                'sales.context_processors.sales',  # here
            ],
        },
    },
]
```

### Step 4. Customize sales settings (in settings.py file) (optional)
The defaults are:
```python
SALES_LINK_PARAMETER = 'sales'
SALES_DEFAULT_ID = 1  # ?sales=1
SALES_COOKIE_NAME = 'sales'
SALES_COOKIE_MAX_AGE = 3600  # 1 hour
```

### Step 4. Load sales tag (in any .html file)
```html
{% load static %}
{% load sales %}  # here
```

### Step 5. Build sales links (in any .html file)
```html
<a href="{% sales '/' %}">Home</a>
<a href="{% sales '/contact' %}">Contact</a>
```

### Step 6. Display sales information (in any .html file)
```html
<a href="mailto:{{ sales.email }}">Email</a>
<p>{{ sales.first_name }} {{ sales.last_name }}</p>
```

django-sales makes use of django.contrib.auth.models.User model, which can be easily extended according to your needs. (e.g. Add a phone number field)

## Contributing
Pull requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)
