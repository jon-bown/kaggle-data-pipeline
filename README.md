# Kaggle Data Pipeline Template

Welcome to the Kaggle Data Pipeline Template! This repository serves as a blueprint for creating automated data pipelines using the Kaggle API. It includes the necessary scripts and file structure to get your own data pipeline up and running quickly.

## Prerequisites

You will need:

- A Kaggle account.
- API credentials from Kaggle.

## Set Up

To use this repository as a template, follow these steps:

1. Click on the `Use this template` button to create a new repository.
2. Clone the new repository to your local machine.
3. Install the Kaggle API by running `pip install kaggle`.

## Kaggle API Credentials

To use the Kaggle API, you will need to add your API credentials as secrets to your repository. To do this, follow these steps:

1. Download your Kaggle API credentials file (`kaggle.json`) from the Account section of your Kaggle profile.
2. Navigate to the 'Settings' tab of your new repository.
3. Click on 'Secrets'.
4. Click on 'New repository secret'.
5. Name the new secret `KAGGLE_USERNAME` and set its value to your Kaggle username (found in the `kaggle.json` file).
6. Create another secret named `KAGGLE_KEY` and set its value to the corresponding key from the `kaggle.json` file.

By doing this, you ensure that your Kaggle credentials are kept secure and are not shared publicly.

## Usage

Once you have set up your Kaggle API credentials, you can start using the data pipeline. 

- `data` folder: Whatever datasets you generate should be placed within the data folder and should be referenced directly by the dataset-metadata.json file. For more info on structuring the metadata file, see the [Metadata Wiki](https://github.com/Kaggle/kaggle-api/wiki/Dataset-Metadata). The data_card.md can be updated to be included in your metadata file `description` key.
- `utils` folder: Convenient place to put helper functions for your pipeline. There is an example for updating the data card in the metadata file. 
- `requirements.txt`: Add names of all python packages used. Lock versions if applicable.
- `generator.py`: Build your data generator. Basic code is included to update a kaggle data version.
- `actions` folder: Contains an example of a github action that will run the `generator.py` script on the first day of every month. This template will not do anything by itself, it must be developed within a github action by navigating to the 'Actions' tab and creating a new workflow.

## Contact

For any questions or concerns, please open an issue on this repository.

---
© 2023 `jon-bown`
