# build_files.sh
pip install -r requirements.txt
python3.11 manage.py collectstatic
export PATH=$PATH:/usr/lib/postgresql/14/bin
