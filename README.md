# RandomForestClassifierAppPy
This is a app which based on data inputed by user in a window predicts whether or not the person is travel insured with propability of it happening.

- Model creation to pickle file.py - reads data from X and Y files and based on that creates Random Forest Classifier model which is later used to predict. The model is saved into Pickle file to be used later.
- model.py - a file designated to read models from pickle files, this approach allows for using different models for our prediciton. We can just  change model_path in code and then we can easily use different model.
- preidiction.py - stores predictions made using model.py that are later shown in the window.
- window_front.py - front end app created using PyQt5 in which user can input data and receive predictions based on it.
- X,Y - data files
