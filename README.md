# codebase-cleanup-exercrise


## Setup

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


## Configuration

# AlphaVantage API Key Setup
Obtain a premium AlphaVantage API Key [here](https://www.alphavantage.co/).



# SendGrid API Key Setup
First, [sign up for a SendGrid account](https://app.sendgrid.com/login?redirect_to=%2Fsettings%2Fapi_keys), then follow the instructions to complete your "Single Sender Verification", clicking the confirmation email to verify your account. 
NOTE: some users in the passed have reported issues with using yahoo-issued, university-issued, or work-issued emails in the past. Consequently, if you run into similar issues when attempt to set up your SendGrid account, perhaps consider using a personal Gmail account. 

Then, [create your SendGrid API Key with "full access" permissions](https://app.sendgrid.com/login?redirect_to=%2Fsettings%2Fapi_keys). Once you create your SendGrid API Key, we will want to store the API Key in an environment variable in the .env file called ```SENDGRID_API_KEY```. Also set an environment variable called ```SENDER_ADDRESS``` to be the same email address as the single sender address you just associated with your SendGrid account.

Use a ".env" file approach to manage these files, as mentioned in the ".env file approach" section above. 

For reference, you will want to set the environment variables using a ".env" file approach like the following:

```sh
ALPHAVANTAGE_API_KEY="..."

SENDER_ADDRESS="example@gmail.com"
SENDGRID_API_KEY="SG...."
```


# Environment Variables - ".env" File Approach
You must set up a local file named ".env" that is outside the root directory of the project. In this file, you will be able to store the necessary environment variables to run the program. For the purposes of the shopping-cart program, the following code will suffice:
```sh
# this is the .env file

# for the Sengrid API capabilities
SENDGRID_API_KEY="SENDGRID_API_KEY"
SENDER_ADDRESS="SENDER_ADDRESS"

# for the AlphaVantage API Key Requirements
ALPHAVANTAGE_API_KEY="..."
```

Note that you will need to update the values of the SendGrid environment variables to meet your specific API key and email address that you created in your SendGrid account (instructions for that mentioned in the "SendGrid API Key Setup" Section). Similarly, you will have to update the values of the ```ALPHAVANTAGE_API_KEY``` to your specific premium AlphaVantage API Key to run certain aspects of the program. 

Also, make sure to add all of your environment variable to your repository's ".gitignore" file to ensure it does not get tracked in version control or uploaded to Github:  
```sh
# the .gitignore file

# ignore environment variables in the ".env" file:
.env
```

# Usage - Run Appropriate Files
Once you have properly set up your local environment, installed all necessary packages, and set up your SendGrid API Key and AlphaVantage API Key credentials, you are ready to run the program. 

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
If to run any internal tests within the program, please enter the following in the command line: 
```sh 
pytest
```
