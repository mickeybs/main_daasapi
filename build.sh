echo "BUILD START"
python3.9 - m pip install -r requirements.txt
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput
echo "collecting static"
python3.9 manage.py collectstatic --noinput --clear 
echo = "BUILD END"