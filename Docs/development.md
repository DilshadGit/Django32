# .env required pip install django-dotenv we use django verion not python-dotenv

# In Digital ocean need 
pip install gunicorn
pip install psycopg2-binary

This need to be added to and python version must be also declear to make this create runtime.txt

# Create Generate random secret-key runing this line:
$ python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# You can use another way to create secret key using:
go to python shell:
import uuid
uuid.uuid4()