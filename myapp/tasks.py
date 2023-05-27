# myapp/tasks.py

from celery import shared_task

@shared_task
def fetch_package_details(package_name):
    # Implement the logic to fetch package details here
    # This function will be executed asynchronously by Celery
    print('<<<<<<<<<',package_name)
    pass
