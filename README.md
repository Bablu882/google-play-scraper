# google-play-scraper
this project is on python and django 
# installation:
#make sure celery apt should be running in local system 
#clone the repo 

#cd myproject where manage.py located 
#pip install -r requirements.txt
#in it some error will occur than run --pip install <pakage_name>
#now run the development server in terminal1 -
#python3 manage.py runserver
#now run the celery beat in terminal2
#celery -A myproject.celery worker --loglevel=info
