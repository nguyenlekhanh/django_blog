 echo "BUILD START"
 pip uninstall crispy-bootstrap5
 pip uninstall django
 python3.9 -m pip install -r requirements.txt
 python3.9 manage.py collectstatic --noinput --clear
 echo "BUILD END"