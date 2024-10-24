# Table of Contents

1) Getting Started  
2) Recommended Setup  
3) Using the app  
4) Explanation

# 1.) Getting Started 
Medikator is a full-stack, machine learning-driven medical application. Here, you will find how to best use it.

If using the bot from the web page, don't worry, because there's no set up for you!
Or
If you are using the bot locally, ensure the following steps have been taken first:
	
pip install git  
git clone https://gitlab.computing.dcu.ie/delahue6/2024-ca326-medai.git  
pip install scikit-learn  
pip install numpy  
pip install pandas  
pip install django

Next, type “cd 2024-ca326-medai”
Then, type “cd MedWeb”.

Finally, Run the command “python manage.py runserver”.
And now you should be running the app locally!

# 2.) Recommended setup
Medikator can work on any device with an internet connection, it uses the browser to capture inputs.

For local users, It is only possible to run the application on Windows or Linux.


# 3.) How to use the app
Some people may be confused as to how they use the app for the first time, and so here is how you properly use the application.


Steps:  
1.)Load the website  
2.)Click on diagnosis  
3.)Enter your name  
4.)Enter your main Symptom  
5.)Enter how long you have had the symptom  
6.)Answer the rest of the questions with either “yes” or “no”  
7.)Review your predicted diagnosis  


However, there is no need to keep your eyes glued here as our bot will guide you through the process.

# 4.) Explanation
You may be someone who worries about their privacy, well, don't fret! We have you covered.  
At Medikator we do not keep any stored user data once you leave the site.  
All entries in the database are completely anonymous IF you do not use your real name!  

The way our app works is simple. During the initial consultation (The first 3 questions), The program gathers your information so that it can start predicting your symptoms.  
At this point, the bot will only ask questions to be answered with either yes or no.  
Once the list of new symptoms runs out, the bot thinks it has guessed your disease.  
From here, Congratulations! Now, whenever you're not feeling at your best, you know how to Medikate yourself.  

WARNING - This is a developmental app, and the databases have not been scaled to a size where machine learning is efficient, the app isnt as accurate as it could be. Mediator is meant as a framework to be scaled up to potentially include every disease!
