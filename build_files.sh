echo "START"
./venv/Scripts/activate
python3.12 -m pip install -r requirements.txt
python3.12 manage.py collectstatic -noinput
echo "END"