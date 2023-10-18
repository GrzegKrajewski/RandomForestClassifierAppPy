# RandomForestClassifierAppPy
## Application Overview:
This application is designed to predict the likelihood of an individual being insured for travel, along with the probability of this occurrence. To make this prediction, it utilizes a Random Forest Classifier model. Users can input relevant patient data through a user-friendly front-end interface for a seamless experience.

## Key Components:

### Random Forest Classifier Model:

The heart of the system is a Random Forest Classifier model. It is trained to predict whether a person is insured for travel based on provided data.
### User Interface (Front-End):

A user-friendly front-end interface, built using PyQt5, allows users to input patient data for analysis.
### Data Input and Prediction Process:

Users enter essential patient information into the provided interface.

The application employs the Random Forest Classifier model to process this data and determine the probability of the person being insured for travel.

The predicted outcome, including the probability, is presented to the user through the interface.

### Application Purpose:
This application serves as a valuable tool for assessing the likelihood of travel insurance coverage based on individual patient details. It is particularly useful for insurance professionals and travelers to make informed decisions regarding insurance requirements.

## File List

- model_creation_to_pickle_file.py: This script is responsible for generating a machine learning model using the data provided in X and Y files. It employs a Random Forest Classifier to create the model, which is then saved to a pickle file for future use.

- model.py: In this module, we manage the loading of machine learning models from pickle files. This modular approach allows for easy model swapping in the application. By changing the model_path variable within the code, different models can be utilized for predictions.

- prediction.py: Within this script, predictions are generated using the loaded models from model.py. These predictions are stored and made available for presentation in the user interface.

- window_front.py: This component serves as the graphical user interface (GUI) for the application. It's built using PyQt5, enabling users to input their data and receive predictions based on the information provided.

- X, Y: These files contain the data required for training the machine learning models. They serve as the foundation for the model's predictive capabilities.
 
By following this organized structure, you can easily create, manage, and update machine learning models and integrate them into a user-friendly interface for making travel insurance predictions.
