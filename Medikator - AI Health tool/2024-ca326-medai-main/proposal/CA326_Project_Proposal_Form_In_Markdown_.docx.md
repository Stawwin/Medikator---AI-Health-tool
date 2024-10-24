School of Computing            CA326 Year 3 Project Proposal Form

**SECTION A**

***Project Title*:** MedAI - An AImedical diagnosis tool ***Student 1 Name:*** Eoin Delahunty ***IDNumber:*** 21417804 ***Student 2 Name:*** Filip Laskowski ***IDNumber:*** 21366626 ***Staff Member Consulted:*** Mark Humphrys

**Project Description**:

**Project Idea**

The idea is a chatbot that helps diagnose illnesses/diseases based on questions asked by the bot and the answers provided by the user. The user starts by writing a paragraph mentioning the symptoms/issues they are facing. The bot scans the paragraph for keywords and depending on the symptoms/issues mentioned, asks further questions Akinator-style;

- Asks questions and uses answers to parse the decision tree
- Prunes down to possible illness/disease
- Provides user with answers along with confidence levels of each based on the number of matching symptoms
- Suggests possible remedies

When a user registers, they provide details like age, weight, gender, GP details, allergies. Possibility to book a doctor's appointment directly through the chatbot at the end of the conversation by using registered GP details and sending an automatic email to the clinic requesting an appointment. the app also gives recommendations from the bot on what to do next eg. “seek clinical advice”, “seek attention immediately”, and “use OTC medicine”.

Other possible features include medication reminders (user has the option to add their medication and get reminders as notifications), mental health support (relaxation techniques, offer support or redirect to helplines?) and the ability to get a recurring prescription through partnered pharmacies.

**Implementation**

We will use the Chatterbot Library for Python which uses logic adaptors to prune the decision tree. We are going to create a dataset of diseases/illnesses and their symptoms to form the decision tree. We can then narrow the search down to possible choices and give a confidence level (as %) of which disease/illness the user has contracted based on the number of matching symptoms.

**Division of Work**

The plan is to work on all aspects of the project together as it is quite complex and we feel that by working on it together we will learn and understand it better. While individual responsibilities will certainly emerge as we progress, our primary approach is one of cooperation as well as helping one another. We will work on it together in person during and outside of college time as much as we can and in between in-person time go on calls.

**Programming Languages**

- Python
- HTML/CSS

**Programming Tool(s)**

- Vim
- Sublime
- Visual Studio Code
- Django

**Learning Challenges**

We must figure out how to form and use a decision tree algorithm as well as figuring out how to create logic adapters for the Chatterbot Python library.

**Hardware / software platform**

- PC
- Windows
- Visual Studio Code

**Special hardware / software requirements**

N/A
