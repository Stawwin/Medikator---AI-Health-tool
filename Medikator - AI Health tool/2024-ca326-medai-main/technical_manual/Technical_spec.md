        Table Of Contents
        1 - [Introduction]
        2 - [System Architecture]
            2.1 - [Django Framework]
            2.2 - [Main Processes]
            2.3 - [Third party Dependencies]
            2.4 - [Changes from initial Design]
        3 - [High-Level Design]
            3.1 - [CSV files instead of models]
        4 - [Problems and Solutions]
        5 - [Installation Guide]

[link to blogs](https://docs.google.com/document/d/18HjIpNmN0detn-j9yC7usRB4zPKV4OhfN4sYjHMl6SI/edit?usp=sharing)

[link to Screencast](https://youtu.be/JRTyZJfl2J8)
 

# 1) INTRODUCTION

For our project, we have created a framework for a full-stack machine-learning medical application using Django and Python. The logic of our app (medbot.py) relies heavily on the “Sci kit” module; in particular its “preprocessing“ and “model selection” functions.

To use this module, the app takes input from users on a front-end page, then passes that information back to the “views.py” file, where it is passed further to “med_bot.py” to be processed.

The information is processed by training an algorithm using “Training.csv”, where it learns what symptoms are present for each disease in the database in Preprocessing.

After this, the app begins to take user input. First, it asks the user’s name, initial symptom, and how long they have had said symptom. By giving the initial symptom to the algorithm, it will pick out every disease that contains the symptom and then finally it will ask yes/no questions about subsequent symptoms until it has enough information to make a diagnosis.

A crucial feature of our app is that we do not store any permanent data. All stored data is anonymous and temporary. When the user exits the diagnosis page, all information stored on them will be deleted.




# 2) SYSTEM ARCHITECTURE

## 2.1) Django Framework

The core of our application is the Django Web Framework. In this project it is being used to render the webpages as well as process user input. This approach allows for our app to take a modular approach with 3 main stages:  

1) Front-end - This is where user inputs are taken and where the bot response is given.

2) views.py - Here is where information is taken from the front end and given to the back end. In the project, a list is constructed here with inputs that are continuously fed to the back-end each time a new input is given / a new page is rendered The way we use it in this project makes it a “Pseudo-API”.

3) Medbot.py - Here is where user inputs are processed and where the algorithm will determine what questions to ask next if the output is accurate (meaning the sec_predict() function ended up with the same prediction), what the output/disease was, possible remedies, and finally whether you should seek urgent care (Using the calc_condition() function.


## 2.2) Main Processes

### main1(user_inputs):

This is the function that is called in “views.py” to load the back-end of our app each time user input is received. “User_inputs” is the list of responses from a user during a consultation. This list is then fed recursively to the back end, getting longer and closer to a diagnosis each time.


### ListInputProgram(user_inputs):

This is a class method that creates a local version of the list of responses a user has given. This class has methods for handling each input in the list before removing them and proceeding in the code until either:

No inputs remain - The program will run into an except() statement which returns the next question for the front end.

OR

The back-end code finishes - Once the back end has produced a diagnosis, any further inputs will always lead to the same return statement.




### tree_to_code(clf, cols, program):

This is the function that takes in user input from “views.py” inside the “program” input list. From here, the function contains many “while True:” loops and try:/except: statements that handle user input and error detection. There are 3 main inputs in this function.

Initial symptom - the symptoms used to match initial possible diseases.

Length of illness - duration of symptoms which is later used by the “Severityindex” to calculate the severity of your condition.

Yes/No questions - Lastly, the bot enters a loop(recurse(0, 1)) where it asks “Are you experiencing any $Symptom$”. Symptoms are saved when answering “yes” and discarded when answering “no”. 


### recurse(node, depth):

This is the function that populates the “Decision Tree” algorithm which drives our bot. Once the function has populated all nodes, it will exit to the second part of its functionality where it will recursively enter the inputs from the “program” list. Before a diagnosis is made, this function returns the next question to be asked to the front end. As the input list gets filled by the user, it makes it further into the function without an except() or return().
Finally, once a diagnosis is made, this function will return it to the front end to be given to the user.

### Session Variables

Session variables are used in our code in place of storing data. The input list is stored locally on the browser and is being read by the server every time the page refreshes. The inputs are then deleted once you exit the “diagnosis” page. It was decided that this was the best way to handle our implementation/design since our app places a big emphasis on anonymity, as well as the fact that our “models.py” are replaced by .csv files; allowing our app to serve as a template to add as many diseases as needed in the future.

## 2.3) Third Party Dependencies

Our project relies on some already existing libraries for Python, mainly for the implementation of the algorithm that traverses our Decision Tree and the interpreting of the .csv files that contain our training data. 

List of Libraries used:
Pandas
Numpy (for reading .csv files)
Sklearn (tree, preprocessing, train_test_split, cross_val_score, SVC)
re (regular expressions for pattern matching)



## 2.4 Changes from the initial design:

The biggest change from our initial design was giving up on the idea of using the “Chatterbot” library for our processing. While getting used to coding with Chatterbot we found that it was impossible to have a reliable output stream, with outputs being randomised each time depending on inputs it had seen before.

We decided to replace it with the “Sci-kit learn” module in particular as we saw its models came with a “random_state” variable, which we could use to make sure we got reliable outputs for certain inputs. Scikit also came with the structure for our Decision Tree built-in.

We also decided that since there was no need to store user data, we would omit the account features planned for the app to be replaced by a “terms of service agreement” that the user must consent to every time they use the app.

Users also no longer interact with the bot in the form of a traditional “chatbot” as inputs are not necessarily random. Instead, users are prompted with questions based on previous symptoms answered.

Here are the before and after for our System Architecture diagrams;

Before:
![alt](technical_manual/D3.png)

After:
![alt](technical_manual/D2.png)






















Our new system performs a loop until an answer is achieved.









# 3) HIGH-LEVEL-DESIGN:

Here is a Sequence Diagram showing the data flow for our application:
![alt](technical_manual/D1.png)






















Step by step our app works by:
The user types the URL into the search bar
The user sees the home page and proceeds to get a diagnosis
The user sees the diagnosis page
Views.py initialize Medbot.py for receiving input_program
Medbot.py returns the first question to Views.py, which passes it to User
User answers returned the answered question
Medbot.py is called again and progresses further with new input. Gives new questions.
Step 7. continues until Medbot.py sends a diagnosis instead of a question.
All data is deleted when the user exits the diagnosis page

## 3.1) CSV files instead of models
The goal of this project was to produce an app that serves as a framework for a much larger application and can be hosted online. Because of this, we needed to host our CSV files online for testing purposes. We decided to use the files from Gitlab as we needed to upload them for the project deliverables anyway.

The CSV files work via pattern matching in the chk_pattern() function. The files are label encoded as they are read so that they can be used inside the app logic. The “Training.csv” file, for example, contains all of the diseases for our database along with the associated symptoms which can then be used to train the bot's algorithm

# 4) PROBLEMS AND SOLUTIONS

Once we switched to Sci-kit over Chatterbot, we assumed that the biggest challenge would be to get the logic working. In reality, the logic was quite a challenge and we ran into errors when it came to providing the “Are you experiencing any $syms$” questions. We quickly realised that we were not returning the return functions from the nested functions properly. 

After being stuck for a while, we eventually figured out how to get the logic of the code working locally. Yet what we did not expect was how much of a challenge it was to then deploy a front-end to interact with users.

Because of the way our bot is coded, the user_inputs were being reset every time a new message was sent to the bot. There were 2 fixes for this:

Develop a GUI for the logic and have it work offline
Create a list of inputs to run each time the page is re-rendered

We decided to go with option 2 as we felt developing a GUI for the project defeated the purpose of having it accessible to everyone.

After realising we would need to send input differently, we decided to start by making the CSV files remote on Gitlab. When we did this, the code stopped working unexplainably. Later we found out that when reading files from the web, the logic for reading the CSV files broke, requiring us to re-develop it.

After re-developing the way CSV was translated, we then implemented the ability to send inputs as a list rather than a string. Now we needed a way to print the most recent response to the front end. To do this, we made it so that Medbot.py always returned a string containing its most recent response no matter which line of logic it was following. We ran into a lot of errors (EG TypeError, IndexError, NoneType, etc…) while trying to test this function, so we added Try()/Except statements to the code so that if it tried to get input, but got an error instead (in case of NOT yes or invalid) This made it so that the website would sometimes get stuck, but never crash.

Once we figured out how to send input and output bi-directionally using this method, There was still a lot of input testing to do, as our code would sometimes get infinitely stuck. After adding features such as the sec_pred() function, and examining what the value of the user's most recent input was, we were getting reliable outputs without the website freezing or crashing.


# 5) INSTALLATION GUIDE
The installation of our bot for local purposes is quick and easy.


Simply type these commands into your terminal:

1)
git clone https://gitlab.computing.dcu.ie/delahue6/2024-ca326-medai.git

pip install scikit-learn

pip install numpy

pip install pandas

pip install django

2).
Next, type “cd 2024-ca326-medai”

Then, type “cd MedWeb”

3).
Finally,
Run the command “python manage.py runserver”.

And now you should be running the app locally!
