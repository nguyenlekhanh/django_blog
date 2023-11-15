 echo "BUILD START"
 python3.9 -m pip install --upgrade pip
 python3.9 -m pip uninstall crispy-bootstrap5
 python3.9 -m pip uninstall django
 python3.9 -m pip install -r requirements.txt
 python3.9 manage.py collectstatic --noinput --clear
 echo "BUILD END"