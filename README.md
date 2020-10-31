# BoundlessAgro

## Abstract

Hydroponic farming is a technique by which plants are grown with the help of nutrients from water instead of soil. <br>
This project aims to develop a system to remotely and efficiently manage and monitor hydroponic farming, which is a good solution for the problem of scarce arable lands.<br>
It aims at implementing predictive maintenance, diagnostic analysis with the help of a dashboard and automating the conditions such as temperature, pH, amount of nutrients present per unit of water(ppm) to be pumped, etc.. while also enabling the user to manually control them. 

## Machine Learning Models

The dataset used is specific to the **Blueberry** plant, to be grown using hydroponic farming.

This project uses two machine learning models.
1. K-Nearest Neighbor Classifier 

    This algorithm is used to predict features like increasing or decreasing the ppm, temperature and the pH of the water based on other features in the dataset.
2. Multivariate Linear Regression 

    This algorithm is used to predict the optimal pH of the water, given ppm and temperature of the water.

## Dashboard

The dashboard is made using Flask.
It lets the user control pH,ppm and temperature remotely.

## Usage

1. Clone the repository 

    ``` git clone https://github.com/sakshi2912/BoundlessAgro.git ```

2. Run the dashboard

    ``` cd dashboard ``` <br>
    ``` python3 app.py ```
    
    Name to the hosted link in the browser.

3. Run the Machine Learning model

    ``` cd ../model ```<br>
    ``` python3 hydroponics.py ```

    The values will start updating to firebase, and can be seen in the dashboard now.

4. Run the ino script on NodeMCU to replicate actuators

    - Open ArduinoIDE, and install necessary libraries.
    - Select ESP8266 board and a corresponding baud rate.
    - Make connections on the board as given in the test_actuator.ino file.
    - Compile and upload the code.

