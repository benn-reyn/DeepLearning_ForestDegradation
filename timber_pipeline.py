from airflow.decortators import dag, task
from datetime import datetime
import os

@dag(
    schedule=None,
    start_date = datetime(2026, 4, 1),
    catchup=False,
    tags=['timber_pipeline']
)

def timber_pipeline():
    @task
    def check_windows_access():
        windows_path = "/mnt/c/Users/reyno/Desktop/Coding/ADV_ANALYTICS/timber_degradation_pipeline"
        if os.path.exists(windows_path):
            return "Windows path exists"
        else:
            raise Exception("Windows path malformed")
    
    @task
    def download():
        return "Pretending"
    
    status = check_windows_access()
    download = download()
    status >> download

timber_pipeline()