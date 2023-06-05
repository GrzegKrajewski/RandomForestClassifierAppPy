import pickle
def read_model(model_path):
    with open(model_path,'rb') as model_file:
        model=pickle.load(model_file)
    #zmienna model to slownik z dwiema kluczami model oraz name
    return model['model'], model['name']


