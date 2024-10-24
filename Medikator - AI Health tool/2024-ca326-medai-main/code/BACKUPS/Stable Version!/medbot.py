import pandas as pd
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier, _tree
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
import csv
import warnings
import re

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Loading training data
training = pd.read_csv('https://gitlab.computing.dcu.ie/delahue6/2024-ca326-medai/-/raw/main/code/CSV%20files/Training.csv')

reduced_data = training.groupby(training['prognosis']).max()

# Extracting features and labels
cols = training.columns[:-1]
x = training[cols]
y = training['prognosis']

# Label encoding
le = preprocessing.LabelEncoder()
le.fit(y)
y = le.transform(y)

# Splitting the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# Creating and training the decision tree classifier
clf1 = DecisionTreeClassifier()
clf = clf1.fit(x_train, y_train)
scores = cross_val_score(clf, x_test, y_test, cv=3)
decision_tree_score = scores.mean()

# Creating and training the support vector machine (SVM) model
model = SVC()
model.fit(x_train, y_train)
svm_score = model.score(x_test, y_test)

# Feature importance
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]
features = cols

severityDictionary = dict()
description_list = dict()
precautionDictionary = dict()

symptoms_dict = {}

# Mapping symptoms to their indices
for index, symptom in enumerate(x):
    symptoms_dict[symptom] = index


class ListInputProgram:
    def __init__(self, input_list):
        self.input_list = input_list.copy()

    def get_input(self):
        if not self.input_list:
            return None
        return str(self.input_list.pop(0))


def calc_condition(exp, days):
    sum_val = sum(severityDictionary[item] for item in exp)
    if (sum_val * days) / (len(exp) + 1) > 13:
        return "You should take the consultation from a doctor."
    else:
        return "It might not be that bad, but you should take precautions."


def getDescription():
    global description_list
    description_list = {}
    csv_file = pd.read_csv(
        'https://gitlab.computing.dcu.ie/delahue6/2024-ca326-medai/-/raw/main/code/CSV%20files/symptom_Description.csv?ref_type=heads')
    try:
        for _, row in csv_file.iterrows():
            symptom = row[0]
            description = row[1]
            description_list[symptom] = description
    except:
        pass


def getSeverityDict():
    global severityDictionary
    severityDictionary = {}
    csv_file = pd.read_csv(
        'https://gitlab.computing.dcu.ie/delahue6/2024-ca326-medai/-/raw/main/code/CSV%20files/Symptom_severity.csv?ref_type=heads')
    try:
        for _, row in csv_file.iterrows():
            symptom = row[0]
            severity = int(row[1])
            severityDictionary[symptom] = severity
    except:
        pass


def getprecautionDict():
    global precautionDictionary
    precautionDictionary = {}
    csv_file = pd.read_csv(
        'https://gitlab.computing.dcu.ie/delahue6/2024-ca326-medai/-/raw/main/code/CSV%20files/symptom_precaution.csv?ref_type=heads')
    try:
        for _, row in csv_file.iterrows():
            symptom = row[0]
            precautions = [row[1], row[2], row[3], row[4]]
            precautionDictionary[symptom] = precautions
    except:
        pass


def getInfo(input_program):
    return "Hello, " + input_program.get_input()


def check_pattern(dis_list, inp):
    pred_list = []
    inp = inp.replace(' ', '_')
    patt = f"{inp}"
    regexp = re.compile(patt)
    pred_list = [item for item in dis_list if regexp.search(item)]
    if len(pred_list) > 0:
        return True, pred_list
    else:
        return False, []


def sec_predict(symptoms_exp):
    df = pd.read_csv(
        'https://raw.githubusercontent.com/itachi9604/healthcare-chatbot/master/Data/Training.csv')
    X = df.iloc[:, :-1]
    y = df['prognosis']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=20)
    rf_clf = DecisionTreeClassifier()
    rf_clf.fit(X_train, y_train)

    symptoms_dict = {symptom: index for index, symptom in enumerate(X)}
    input_vector = np.zeros(len(symptoms_dict))
    for item in symptoms_exp:
        input_vector[[symptoms_dict[item]]] = 1

    return rf_clf.predict([input_vector])


def tree_to_code(tree, feature_names, input_program):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]

    chk_dis = ",".join(feature_names).split(",")
    symptoms_present = []

    while True:
        try:
            disease_input = input_program.get_input()
            conf, cnf_dis = check_pattern(chk_dis, disease_input)
            if conf:
                break
            else:
                return("Enter a Valid Symptom in first true Loop")
        except IndexError:
            return("Enter the main symptom you are experiencing")
            

    while True:
        try:
            num_days = int(input_program.get_input())
            break
        except IndexError:
            return("Enter how many days?")

    def recurse(node, depth):
        nonlocal symptoms_present
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]

            if name == disease_input:
                val = 1
            else:
                val = 0
            if val <= threshold:
                recurse(tree_.children_left[node], depth + 1)
            else:
                symptoms_present.append(name)
                recurse(tree_.children_right[node], depth + 1)
        else:
            present_disease = print_disease(tree_.value[node], le)
            red_cols = reduced_data.columns
            symptoms_given = red_cols[reduced_data.loc[present_disease].values[0].nonzero()]
            print("Are you experiencing any ")
            symptoms_exp = []
            for syms in list(symptoms_given):
                inp = ""
                print(syms, "? : ", end='')
                while True:
                    inp = input_program.get_input()
                    if inp == "yes" or inp == "no":
                        break
                    else:
                        print("Provide proper answers i.e. (yes/no) : ", end="")
                if inp == "yes":
                    symptoms_exp.append(syms)

            second_prediction = sec_predict(symptoms_exp)
            print(calc_condition(symptoms_exp, num_days))
            if present_disease[0] == second_prediction[0]:
                print("You may have " + present_disease[0] + "\n" + description_list[present_disease[0]])
            else:
                print("You may have " + present_disease[0] + " or " + second_prediction[0] + "\n" + description_list[present_disease[0]] + "\n" + description_list[second_prediction[0]])

            precution_list = precautionDictionary[present_disease[0]]
            print("Take the following measures : ")
            for i, j in enumerate(precution_list):
                print(i + 1, ")", j)

    recurse(0, 1)

def print_disease(node, le):
    node = node[0]
    val = node.nonzero()
    disease = le.inverse_transform(val[0])
    return list(map(lambda x: x.strip(), list(disease)))



def main1(user_inputs):
    #user_responses = ["cough", "5", "yes", "yes", "yes"]
    program = ListInputProgram(user_inputs)
    getSeverityDict()
    getDescription()
    getprecautionDict()
    if len(user_inputs) == 0:
        return ("What is your name?")
    elif len(user_inputs) == 1:
        return (getInfo(program))
    else:
        result = tree_to_code(clf, cols, program)
        return result



if __name__ == "__main__":
    result = main1()
    print(result)