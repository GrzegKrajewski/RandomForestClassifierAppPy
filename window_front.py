from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import pandas as pd
import model as m
import prediction as prediction
import numpy as np



def window(model_ML, model_name):
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(200,200,500,300)
    win.setWindowTitle("Insurance")
    
    win.setCentralWidget(QtWidgets.QWidget())
    win.centralWidget().setLayout(QtWidgets.QGridLayout())
    list_labels=["Age","Annual income", "Family Members" ,"Chronic Diseases", "Self Employed", "Graduated","FrequentFlyer","EverTravelledAbroad"]
    age_spinner=QtWidgets.QSpinBox()
    age_spinner.setMaximum(100)
    age_spinner.setMinimum(18)

    income_edittext=QtWidgets.QLineEdit()

    family_spinner=QtWidgets.QSpinBox()
    family_spinner.setMaximum(20)
    family_spinner.setMinimum(0)

    diseases_chb=QtWidgets.QCheckBox()
    self_employed_chb=QtWidgets.QCheckBox()
    graduated_chb=QtWidgets.QCheckBox()
    flyer_chb=QtWidgets.QCheckBox()
    abroad_chb=QtWidgets.QCheckBox()
    
    submit_button=QtWidgets.QPushButton("Submit")

    result_label=QtWidgets.QLabel("No results provided yet")

    list_widgets=[age_spinner, income_edittext, family_spinner,diseases_chb, self_employed_chb, graduated_chb, flyer_chb, abroad_chb]
    for i, (label, widget)  in enumerate(zip(list_labels, list_widgets)):
        win.centralWidget().layout().addWidget(QtWidgets.QLabel(label), i, 0)
        win.centralWidget().layout().addWidget(widget, i, 1)

    win.centralWidget().layout().addWidget(submit_button,len(list_widgets),0, 1, 2)
    win.centralWidget().layout().addWidget(result_label,len(list_widgets)+1,0,1,2)
    
    def click_button():
        age=age_spinner.value()
        family=family_spinner.value()
        income=float(income_edittext.text())
        diseases=diseases_chb.isChecked()
        self_emp=self_employed_chb.isChecked()
        graduated=graduated_chb.isChecked()
        flyer=flyer_chb.isChecked()
        abroad=abroad_chb.isChecked()
        X={"age": [age], 
           "annual_income":[income],
           "family_members": [family],
            "is_chronic_diseases":[diseases],
            "is_self_employed": [self_emp],
            "is_graduated": [graduated],
            "is_frequent_flyer": [flyer],
            "is_ever_travelled_abroad": [abroad] }
        X=pd.DataFrame(data=X)
        answer,proba=prediction.make_pred(X,model_ML)
        proba=np.max(proba)
        print(answer)
        print(proba)
        result_label.setText(F'Status of person travel insurance is {answer} with {round(proba,2)} %')



    submit_button.clicked.connect(click_button)
    win.show()
    sys.exit(app.exec_())

model_path='model_RF.pickle'

model_ML,model_name=m.read_model(model_path)


window(model_ML, model_name)
