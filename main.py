from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.entity.config_entity import ModelTrainerConfig
from networksecurity.components.model_trainer import ModelTrainer
if __name__=="__main__":
    try:
        trainingpipipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Intiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data initation completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipipelineconfig)
        logging.info("Initiate the data validation")
        data_validation = DataValidation(data_ingestion_artifact=dataingestionartifact,data_validation_config=data_validation_config)

        logging.info("Data Initation Completed")
       
        logging.info("Initate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)

        data_transformation_config=DataTransformationConfig(trainingpipipelineconfig)
        logging.info("data transformation started")
        data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data transformation started")

        logging.info("Model Training Started")
        model_trainer_config=ModelTrainerConfig(trainingpipipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        


 
        logging.info("Model Training artifact created")
    except Exception as e:
        raise NetworkSecurityException(e,sys)    
        