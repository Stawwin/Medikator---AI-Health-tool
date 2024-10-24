# Table of contents
1.0 Introduction \
1.1 Overview \
1.2 Business context \
1.3 Glossary \
2.0 General Description\
2.1 Product/System Functions\
2.2 User Characteristics and Objectives\
2.2.1 User Characteristics\
2.2.2 User objectives\
2.3 Operational Scenarios\
2.3.1 User who is not logged in\
2.3.2 User who is logged in\
2.4 Constraints\
3.0 Functional Requirements\
3.1 Sign Up\
3.2 Log In\
3.3 User Registration\
3.4 My Profile\
3.5 Delete account\
3.6 Submit paragraph / Send message\
3.7 Submit survey\
3.8 Feedback\
3.9 Tutorial\
4.0 System Architecture\
5.0 High-Level Design\
5.1 High-level Design Diagram\
5.2 Higher level design diagram description \
6.0 Preliminary Schedule\
7.0 Appendix 



# 1.0 Introduction:

## _1.1 Overview:_

The app we envision is a revolutionary medical diagnosis application, Medikator. Medikator is designed to provide users with some health insights by analysing a paragraph by the user and using a bot to simulate a consultation and asking questions to prompt for more specific answers. In the same way the game Akinator asks yes or no questions to narrow down what celebrity a user may be thinking of, our app will do the same to help give the user a diagnosis based on symptoms they are experiencing. 

Medikator will be a web based app that will be reachable to everyone on any device that supports an internet browser. It is important to us to make it as accessible as possible. The user interface will be simple to allow users with limited technology knowledge, like some of our older users, to be able to use the app without trouble.

An extensive database of medical conditions will be used to analyse and identify potential health issues. During registration, users will provide some details like their sex, allergies, weight and height which will also be used to determine what the issues they are facing may be. Details like contact information to the user's GP can also be added.This information on the user will be stored but it will not be linked to anyone as we will not be using personal identifiers like names, instead providing the users with usernames. Registration will also be a good point to have users read and agree to our disclaimer which states that our service is merely an online resource for assistance and does not serve as a substitute for a licensed medical professional.

Because of the nature of this app, we will have a lot of possibilities to scale it in the future. These include adding features like tracking user symptoms, interrogation with wearable devices like an Apple Watch/Fitbit, support in other languages, the ability to book a doctor's appointment or renew a prescription using registered details.

## _1.2 Business context:_

There are three possible business contexts that could be applied to our project. These contexts are:

1) **Advertising**: Our app will be free and accessible to everyone. Those who decide to continue using the free version will be subject to non-intrusive ads at the side of their screen so as not to interfere with the Usability of the app.
2) **Subscriptions**: For more frequent users of the app, or for those who want to access the app's premium features. More features to come in future such as offline accessibility.
3) **Partnerships**: Our app could partner with doctors and pharmacies to help link a patient with the right medical care. In return we could charge a small commission of 5-10% per client.
   
   _Context 2 and 3 would work hand in hand, however all three contexts would be viable independently for generating revenue using our app._


## _1.3 Glossary:_

* **Chatterbot** - the Python library Medikators logic will be working on.
* **Consultation** - the process of the submitting the survey questions which supports generating automated responses based on user input
* **Akinator** - the game which provides us with inspiration for td going through the questions phase
* **Redicted diagnosis** - The term we are using for our “Result”. This is not to be confused with a real diagnosis.
* **Django Web Framework** - A web framework connects the front and back ends of a project.
* **React** - the library that will be used to create the frontend.

# 2.0 General Description:

## _2.1 Product/System Functions:_

Listed here are the main functions for our app. These features combined change how users interact with the app by providing them with a smooth experience with an easy to use interface. Most of these features are only available to use by registered users. This makes sure the declaration is read and accepted to avoid any legal trouble.

* Sign up

* Log in

* Profile set up

* My profile\*

* Delete account\*

* Submit paragraph/send message\*

* Submit survey\*

* Feedback\*

* Tutorial

_*Requires login_

## _2.2 User Characteristics and Objectives:_

### 2.2.1 User Characteristics:

The user community for Medikator is diverse as the application is designed to target all users who may be looking for medical information on the internet. Because of this, the age range will be vast and because of how accessible the app is, humans all over the world, as long as they have access to an internet browser, will be able to become users. The app is not tailored for anyone specific, which will be reflected in our diverse user group.

There is no specific expertise level required for users. We believe that if a user is capable of accessing the internet and getting onto our website, they should be able to use it. Anyone with even the most basic knowledge will have no trouble browsing through Medikator, as it will have a simple and user-friendly interface. A tutorial will be featured on the site which will help users familiarise themselves with how the app works.

### 2.2.2 User objectives:

From a user point of view, they can expect the website to have an intuitive interface so that they can get to what they are looking for and start interacting with bot faster. The whole point of the website is to provide users with an insight to what illness or disease they could be suffering with, so the interface should allow users to do that with ease.

The users will expect to receive an accurate diagnosis and this will all come down to the backend involving the dataset and the algorithm. It will need to be programmed and trained in a way where perhaps some form of machine learning is used to give diagnostics that are most accurate.

Users might also want to know how the data they add during registration is used to provide them with a diagnosis. To do this, we are planning to add information on our algorithm somewhere on the page like in an “about” section and explain how the algorithm uses the user’s data to come up with the predicted diagnosis.

## _2.3 Operational Scenarios:_

Due to the nature of our proposed design, some users of the website will only have limited access to its functionality as we need to make sure they have agreed to the terms and conditions. We propose that there will be two different kinds of users of our site, those being:

1) Users who are not logged in.

2) Users who are logged in.

_Below is some information on what functionality will be accessible to which users._

### 2.3.1 User who is not logged in

This type of user will be someone who is either visiting our website for the first time, or is a regular user who is not currently signed into an account. For this user, we will allow them to see the website, but not allow them to interact with its functionality. This will show users enough to make them want to make an account to use the service. The functions this user will be able to access are:

1) Sign up: This function will bring a user to a page where they can enter the required details to create an account with us. They will also have to accept our Terms and Conditions here.

2) Log In: This function is designed for users who have already created an account. This will bring them to a page where they will have to enter their username and password. After doing this, users will have full access to the site's functionality.Tour: Before creating an account, a first time user will be recommended a tour of the Website to familiarise them with it and show them where important features are.

### 2.3.2 User who is logged in

These are the users who have created an account and logged in. They have already agreed to our Terms of Service and are allowed access to all functions of the website. From here users will have access to functions such as:

1) My Profile: This function will take users to a page where they will have access to certain features of our site. From here, users will be able to edit the details associated with their account. Users will also be able to access the function to delete their account from this page.

2) Consultation: This functionality will allow users to interact with the main element of our site. Users will be prompted to answer questions in the form of text-based and questionnaire based questions. At the end of this process a user will be given their predicted diagnosis. After this, a user will be prompted with questions about how they found the experience of using our website. This feedback will help fine tune the website and further hone in on what turns out to be our target demographic.

## _2.4 Constraints:_

**Ethical Issues**: The system must adhere to strict ethical standards by ensuring user privacy and data confidentiality throughout the diagnostic process. To do this we are not taking in any user personal information during registration like email or name.

**Disclaimer**: Users must acknowledge and agree to the app's disclaimer during the registration process, emphasising that the service is an online resource and not a substitute for licensed medical professionals.

**Mandatory registration**: The registration process is a mandatory step for users to interact with the website. It will ensure that only users who accepted the disclaimer will be allowed to use the app.

**Software**: The application is designed to be accessible via web browsers, requiring compatibility with a range of software systems to ensure universal reach.

**Hardware**: Users should be able to access Medikator on any device supporting an internet browser, promoting inclusivity and ease of use across various hardware configurations.

**Database size**: The system relies on an extensive medical conditions database. It will need to be of the right size. Since it will be an easy process to sign up (just username+password), many accounts will be created only to be used once or twice and abandoned. We will need to handle this by deleting these accounts after 365 days to free up the database storing them.

**Reliability**: The system must consistently deliver accurate diagnoses, requiring reliable algorithms and continuous monitoring to minimise errors and ensure user loyalty.

# 3.0 Functional Requirements:

## _3.1 Sign up_

**Description:** When users first access the website, they will be required to create an account using a username and password. This is important as we need to store information such as age, gender, weight and height to help with diagnosing as well as making sure users are aware of our Terms of Service.

**Criticality:** This is required for users to be aware of our Ethics policy and Terms of Service. Users will be able to browse the site, but it will lack any function if a user is not signed in.

**Technical issues:** It may be difficult to implement the ability to browse the site without being signed in, as they will be able to access content that should be behind our Terms of service agreement. We will either need to get rid of the idea of browsing before sign up, or find a way to restrict the content of our page.

**Dependencies:** None.


## _3.2 Log In_

**Description:** When users are re-visiting the website, they will have the ability to use their username and password to log into their previously created account.

**Criticality:** This function is critical to make sure that data that the data we collect is saved and put to use appropriately.

**Technical issues:** None.

**Dependencies:** None.


## _3.3 Profile Set Up_

**Description:** This is a page that will be required to be filled in before the website can be fully accessed. This will be a page that will acquire the users age, height, weight, gender and possible allergies. This information will be stored, however all data will be stored under an anonymous “Username” as to keep any information we keep completely untraceable to any particular user. After completing this form, Users will be brought to a page to read and accept our Terms of Service.

**Criticality:** The way our Design will work relies upon certain data about the user, as some medical conditions or issues may be directly related to such. Our system will not solely rely on this data, but it will be taken into account.

**Technical issues:** It will be difficult to translate subjective data such as height or weight into a Decision tree algorithm or probability table, as for example, take two people with the same height and weight, one may still be extremely fit and the other may be extremely out of shape. We will need to find an appropriate function to convert this data into usable information.

**Dependencies:** Users Will access this page through the “sign up” button or the “My profile” button.


## _3.4 My Profile_

**Description:** When users are logged in, they may access the “My profile” page to change certain details that they entered during registration. This will allow people to rectify any mistakes they may have made during registration, or change certain information such as if they have changed weight, or need to add new allergy information.
**Criticality:** Our design relies upon having accurate data about the user. If the user is not able to make their information as up-to-date and accurate as possible, it will drastically increase the chances of a misdiagnosis from our algorithm.

**Technical issues:** None.

**Dependencies:** Users will have to already be signed in to access this page.

## _3.5 Delete account_

**Description**: Our website will highlight anonymity. Users are free to, and encouraged to delete and create as many accounts as they wish. All accounts will be automatically erased after 1 year if not actively logged in. Users can delete all information about them along with their account from the “My profile” page, where a button for this function will be highlighted in red.

**Criticality:** Users need to be able to control what information is being stored from them, and we need to be able to remove inactive accounts so as not to end up with spam accounts or inactive accounts from people who;

A) forgot their login information and created a new profile.

Or

B) Used our service once and do not plan on coming back.
This will help with the amount of storage space required to actively run the website.

**Technical issues:** None.

**Dependencies:** Users will have to be signed in, and on the “My Profile” page to access this function.


## _3.6 Submit paragraph / Send message_ 

**Description:** Users will initiate conversation with the bot by sending in a paragraph describing how they are feeling and providing details like their symptoms. This feature will allow the bot to prepare the types of questions to ask the user to narrow down the diagnosis. It will do so by scanning the submitted message for keywords and utilising this input to generate more targeted and relevant questions in the diagnostic process.

**Criticality:** This function will help the bot prepare the questions to ask users and improve the accuracy of diagnoses. It enhances user engagement and contributes to the effectiveness of the diagnostic algorithm.

**Technical issues:** The main difficulties with this will most likely include trying to figure out what are the keywords in the text and how do we use these to help the algorithm prepare the questions. The system will need to be designed to handle different formats and potential ambiguities in language.

**Dependencies:** Users must be signed in to access this function as it is what initiates the conversation.

## _3.7 Submit survey_

**Description:** This function involves the automated process of presenting users with a series of targeted "yes or no" questions to gather specific information for the app's diagnostic algorithm. These surveys are designed to efficiently narrow down potential health conditions based on user responses. The questions will be carefully crafted to cover a range of symptoms, experiences, and relevant factors that contribute to the diagnostic process and allow a diagnosis to be made by the end of the conversation.

**Criticality:** This function is crucial as it involves gathering information and ensures the accuracy of the diagnostic algorithm. By using the user responses to prepare the next question, the app will be able to streamline the diagnosis and to provide precise results. The app's overall efficacy in detecting possible health problems is greatly impacted by this function.

**Technical issues:** It takes complex algorithms to create a dynamic and adaptable survey system that can provide pertinent questions depending on user responses. In order to retrieve the most important data for the diagnosis, the system should be able to handle a variety of user input combinations and dynamically modify the survey in order to narrow down the possible answers.

**Dependencies:** Users must be signed in and after sending a paragraph describing their issues to access this function as the questions in the survey are based on the user input in the initial paragraph.

## _3.8 Feedback_

**Description:** This feature allows users to provide feedback on the accuracy and performance of the bot during the diagnostic process. This will allow the user to provide us with feedback which can be used to improve the experience for users.

**Criticality:** In order to fix bugs and find areas for development in the app, user feedback is crucial. It enhances user satisfaction and engagement and raises the app's general quality.

**Technical issues:** Making the feedback option appealing to users so that it prompts them to use it and make it short enough where users are bothered to finish it but long enough where it is able to provide us with useful information.

**Dependencies:** Users must be signed in to provide feedback

## _3.9 Tutorial_

**Description:** This feature provides step-by-step guidance for new users to navigate the website. It aims to assist users in understanding how to navigate through the app, how the diagnostic process works and how to optimise the accuracy of diagnoses.

**Criticality:** A good and detailed tutorial enhances new user experience, reduces the learning curve and ensures users can get the most out of the app. It allows users to get familiar with all features of the app and use it correctly.

**Technical issues:** What may seem obvious to us may not be so obvious to the users. It is important to cover all aspects of the app which may cause some ambiguity as to avoid confusion

**Dependencies:** The tutorial will be available to all users, regardless if they are signed in or not. This will allow potential users to see what the app is like.

# 4.0 System Architecture

 The system will be made up of a website, the Chatterbot application, a MySQL Database, and the Django Framework. The user machine will open up a web browser and access the website, which integrates both the Django framework and React for an interactive user interface. Users engage with the Chatterbot application through the website interacting with the bot and other features. Behind the scenes, Chatterbot is connected to the MySQL Database to retrieve data based on these interactions.
![](https://lh7-us.googleusercontent.com/L_10p-B32TwtpGR5XTLzT5btrNKT5Nyn9J81R8yLsCgT5_EFr5CLdKA_5vStSEHnC5A2DFzNd1sBzL7Bq0LXd-Pbt5JMPekxoIwLDNWNzM9BjChZ-Ho7LaA1ifALlBrNO7te_apNeOygK5g5EOz37r4)


# 5.0 High-Level Design

_5.1 High-level Design Diagram\
_![](https://lh7-us.googleusercontent.com/AODvlJ_Ba3gqc_2VM5TX5yszd0okwDbzr3rQxwQPbHWSbCgkFG3Lx1T9PREUg8IvtTGLMGsXZByWLZVAGinoQMhkLoTeOQTo-I6mr8YSJtHDBZIry9HjpVWUZCfNs2AxOFERuj4Ewb6R_NMDg7XO-hU)__


## _5.2 Higher level design diagram description_

_Fig 5.1 will be explained below_

**Step 1: Register/Sign Up**\
Register with a username, password and relevant details for our website.

**Step 2: Log in**\
Use the username and password from Step 1 to access your account and full site functionality.

**Step 3: Tour**\
The user will be given a tutorial on how to use the website and answer questions.
**Step 4: Initial Consultation**\
A user will submit a worded paragraph, based on which they will be asked certain questions. 

**Step 5: Refinement of consultation**\
A user will be prompted with certain questions based on what data we can find in the paragraph submitted in Step 5. This data will be used to refine and rule-out what illnesses the user may have.

**Step 6: Predicted Diagnoses**\
Based on the answers from the questions our bot will give to the user, it will try to see what symptoms the user had that matched best to certain conditions. For example, the user might have a pain in the throat and so our bot can rule out any illnesses that affect the stomach.

**Step 7: Feedback**\
Users will be asked to give insight on their experience using our website. Here will ask questions such as “Do you feel like our Predicted Diagnosis was accurate?” and “How do you feel about the usability of the website?”.

**Step 8: Log out**\
When Users are done using our site, they can log out.

# 6.0 Preliminary Schedule

We have agreed on a preliminary schedule, and have shown such on a PERT and GANTT diagram. The PERT chart shows what order we plan to develop our website in, and how long each step is expected to take. It also shows the margin of error in our predicted schedule using “Slack” days.\
![](https://lh7-us.googleusercontent.com/7K-mnpbH4LWKhBvCOns--uyq2R6G70rmm4_z-SolF9Xp9_Lu3GC2tiaBEzoI_gr_PPGe17fbd_HlHVc4-Fw1sJTA56dky3afpgRNVneYQBJXF4pxDiB-Y2lc5IYEXKDPYg7HeBwBNzApntT7xQUOnwU)**PERT chart**

Key:

|                        |      |      |     |    |    |     |
| ---------------------- | ---- | ---- | --- | -- | -- | --- |
| Activity               | A    | B    | C   | D  | E  | F   |
| Immediate Predecessors | None | None | A,B | C  | C  | D,E |
| Expected Time (days)   | 7    | 3    | 3   | 14 | 14 | 2   |

|   |                        |
| - | ---------------------- |
| A | ES                  EF |
| T | LS                  LF |

A = attribute, T = time,  ES = Earliest start, EF = earliest finish, LS = Latest start, LF = Latest finish.

A Making the website - 1 week

B making the database - 3 days

C Terms of service and UI elements - 3 days

D Coding the Datasets - 2 weeks

E Coding the bot - 2 weeks

F User study - 2 days

**Gantt Chart:** 

The Gantt chart here shows the tasks and their scheduling over the next period of time up until the deadline date. It shows the steps of the project along with their start and end dates. It also shows the dependencies the tasks have on each other, like what tasks have to be

done before a particular task can be started or completed, like in the case of the user study which is the last task.

\
![](https://lh7-us.googleusercontent.com/cs21-zTsJfaAnXVfMd332qgyylPqvqNZIor29hA0WxRRf-_ExIAeDuZcZ3qI0b9dVikyYD36qY6C51XD1fpa1-5kU0mfmWdOfDiLXwQNb4yJWZa__qrxTSkSvbh86TimSNgaYUzcETTlqLAA8Swdr90)


#

# 7.0 Appendix

## _7.1 Resources_

# *Sample Functional Specs:* 

* <https://www.computing.dcu.ie/~davids/CA326/lorcan.pdf>

* <https://www.computing.dcu.ie/~davids/CA326/aris.pdf>

* <https://www.computing.dcu.ie/~davids/CA326/Alsaa.pdf>
#
Links to used software:
* <https://react.dev/>

* <https://chatterbot.readthedocs.io/en/stable/>

* <https://www.mysql.com/>

* <https://www.djangoproject.com/>**

## _7.2  References_

Akinator game:
<https://en.akinator.com/>





