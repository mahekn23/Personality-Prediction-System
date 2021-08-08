# Personality Prediction System
A ML based Personality Prediction System.

Problem statement: 

The idea is to create a Personality prediction system using ML model and Flask Framework. The users can belong to any one of the serious, responsible, extraverted, lively or dependable personality types after giving an input as a score ( on a scale of 1 to 8 ) for the following attributes:

Open to Experience: It involves various dimensions, like imagination, sensitivity, attentiveness, preference to variety, and curiosity.  
Conscientiousness: This trait is used to describe the carefulness and diligence of the person. It is the quality that describes how organized and efficient a person is.
Extraversion: It is the trait that describes how the best candidates can interact with people, that is how good are his/her social skills.
Agreeableness: It is a quality that analyses the individual behavior based on the generosity, sympathy, cooperativeness and ability to adjust with people.  
Neuroticism: This trait usually describes a person to have mood swings and has extreme expressive power.
 
 
Dataset Description:
 
The dataset used has 8 columns as shown in the figure below. Out of these columns, the features of our model include "openness", "neuroticism", "conscientiousness", "agreeableness", "extraversion" and the target is “Personality”. Our dataset has 315 records out of which 70% data is used for training the model and 30% is used for testing the model.

Machine Learning Model:
 
Random Forest Classifier is chosen as it has a higher accuracy compared to other classifiers

Our System:
 
Web application link: http://mlflaskcodedeveloper.pythonanywhere.com/
 
Conclusion:
 
Our system is a ML and Flask framework based web application which uses Random Forest Classifier to predict personality of a given user. The accuracy of our model is 71% specific to our dataset.
 
Future Scope:
 
Increase accuracy of the ML Model.
Improvements in the UI.
Customization of email templates.
More communication via emails eg: Welcome emails when a user registers.
Email ID verification functionality (OTP based).
Forgot password functionality (OTP based).
Using a larger dataset.
Adding contact us page.


