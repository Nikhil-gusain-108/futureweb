echo "BUILD START"
.\venv\Scripts\activate 
python3.9 -m pip install -r requirements.txt
py manage.py collectstatic --noinput --clear
echo "BUILD END"