import os, sys

import numpy as np
import pandas as pd

from sklearn.metrics import r2_score

import dill

from src.exception import custom_exception

def evaluate_model(x_train, y_train, x_test, y_test, models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]

            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            model_score = r2_score(y_test, y_pred)

            report[list(models.keys())[i]] = model_score

        return report
        
    except Exception as e:
        raise custom_exception(e, sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except:
        pass