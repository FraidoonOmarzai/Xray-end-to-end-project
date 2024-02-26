from Xray.entity.config_entity import DataIngestionConfig
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.components.data_ingestion import DataIngestion
from Xray.logger import logging
from Xray.exception import CustomException
import sys


STAGE_NAME = 'Data Ingestion'


class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = DataIngestionConfig()
        data_ingestinion = DataIngestion(config)
        data_ingestion_artifact: DataIngestionArtifact = data_ingestinion.initiate_data_ingestion()
        


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e, sys)