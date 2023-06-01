import numpy as np
import pandas as pd
import os
import datetime
from kaggle.api.kaggle_api_extended import KaggleApi
import utils.update_metadata as update_metadata
from tests.integrity import check_data_integrity

#TODO: Create dataset within data folder
data_df = pd.DataFrame()
#update data card
update_metadata.update_description()
#init kaggle api
api = KaggleApi()
api.authenticate()
#create data version
integrity_result = check_data_integrity(data_df)

if integrity_result:
    api.dataset_create_version(
    "./data/",
    version_notes=f"Updated on {datetime.datetime.now().strftime('%Y-%m-%d')}",
    )