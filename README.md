# Team Name: CodeShark
## Project Name: C.A.C.H.E - Tagline here
The name of our project is C.A.C.H.E. It stands for **'Clean Air and Care for Healthy Environment'**
### Aim of Project: To mobilise people and aware them about Air Pollution.
1. CACHE is an open-source area targetted to solve problems of air pollution. We are creating a platform that aims to provide all of the 'Air Quality Index' statistics in one place. We have utilized sensors that send data to our Machine Learning models. The model processes it and generates predicted values. 
2. We are promoting the Saaf Hawa Aur Nagrik (S.H.A.N) campaign through our project. Our project provides people with different ways they can use to combat air pollution and climate change. We are also initiating a campaign for gathering data from users. 
3. In our country, we do not have many datasets that can give us data related to Air Quality. Hence using our project people can crowdsource and send data that can be further used for analysis and prediction. 
*We would be able to mobilize people to fight for Air Pollution because one of the most pressing issues in the post-COVID-era is 'Air pollution'. This is our attempt to encourage people for our cause in the reduction of air pollution and make the country a better place to live.*

## Technologies used:
- **Python (Flask)** was used to link our project with the web as a webapp. With a webapp, this project can be easily deployed anywhere.
- **HTML/CSS** was used to create the webpages for our website. We added styling, hyperlinks and content to our website with these languages.
- **MySQL** was used for the database functionality. For linking user input with web, python program and ML, we needed it.
- We used the **VAR (Vector-Auto Regression) algorithm** for working on our datasets and prediction. It is a time series based algorithm that can also support multivariable data structure.
- **Google Cloud** was used to host our project online. After hosting it, it could be deployed.
## What is happening in the project?
1. The website has 4 tabs: 'Home', 'About Us', 'Contact Us' and 'Give us your data?'. The first page i.e; Home talks about the common information that we wish to provide the
   people. It hosts of ML algorithm and statistical data. In the second page we explain our campaign S.H.A.N in detail. In the third page we share our contact details while in the
   last page we ask user to share any AQI data that they wish to provide us with better analytics.
2. When the user visits the home page, he enters the city of which he wishes the analytics. Our python program takes in the city input, assigns it to the correct 'Machine Learning' (ML) model, and correct analysis dataset. Then, the Vector Auto Regression algorithm
## Challenges we ran into:
Each time a project get created, it involves many hurdles and issues. We also faced issues in creating the project:
1. Difficulty in finding dataset that could give AQI readings from major cities of India.
2. Since the current ML algorithm used is time-series based, the datasets need to be updated regularly, for which we had to find an API that could give us precise and reliable data.
3. We faced problems in getting the queried data from our website to our Python program and pass it into our ML algoritm.
4. There were difficulties in hosting our flask based app on the web. Since we are juvenile, we could not find hosting services that work without use of a Credit Card.
5. We have still not been able to completely finalise our idea. It's just a proof of concept. We are still working on sending data from our flask app to the ML algorithm. 
We hope it works out fine.
