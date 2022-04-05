# codebase-cleanup-exercise


# Setup

Create virtual environment:

```sh
conda create -n cleanup-env python=3.8
```

Activate virtual environment:
```sh
conda activate cleanup-env
```

Install packages:

```sh
pip install -r requirements.txt
```
# Configuration

## AlphaVantage API Key Setup
Obtain a premium AlphaVantage API Key [here](https://www.alphavantage.co/). You will use your premium AlphaVantage
API Key to access the necessary stock, crypto, and unemployment report information to run the program. Once you create your AlphaVantage API Key, we will want to store the API Key in an environment variable in the .env file called ```ALPHAVANTAGE_API_KEY```. Use a ".env" file approach to manage these files, as mentioned in the ".env file approach" section below.

## Environment Variables - ".env" File Approach
You must set up a local file named ".env" that is outside the root directory of the project. In this file, you will be able to store the necessary environment variables to run the program. For the purposes of the shopping-cart program, the following code will suffice:
```sh
# this is the .env file

# for the AlphaVantage API Premium Key Requirements
ALPHAVANTAGE_API_KEY="..."
```

Note that you will need to update the values of the SendGrid environment variables to meet your specific API key and email address that you created in your SendGrid account (instructions for that mentioned in the "SendGrid API Key Setup" Section). Similarly, you will have to update the values of the ```ALPHAVANTAGE_API_KEY``` to your specific premium AlphaVantage API Key to run certain aspects of the program. 


# Usage - Run Appropriate Files
Once you have properly set up your local environment, installed all necessary packages, and set up your AlphaVantage API Key credentials, you are ready to run the program. 

In order run the game, please enter the following into the command line:
```sh
python -m app.game
```

In order to run the inventory report, please enter the following into the command line: 
```sh
python -m app.groceries
```

In order to run the stocks report, please enter the following into the command line:
```sh
python -m app.stocks
```

In order to run the crypto report, please enter the following into the command line:
```sh
python -m app.crypto
```

In order to run the unemployment report, please enter the following into the command line:
```sh
python -m app.unemployment
```
# Usage - Run Appropriate Tests
In order to run any internal tests within the program, please enter the following in the command line: 
```sh 
pytest
```
