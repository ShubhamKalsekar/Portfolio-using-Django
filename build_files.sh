
echo " BUILD START"

# Install dependencies using pip
python3.10 -m pip install -r requirements.txt

# Run collectstatic
python3.10 manage.py collectstatic --noinput --clear

echo " BUILD END"
