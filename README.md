# K-SEC-2023-ChatGPT-Client

![image](/assets/overview.png)

## Local debug
### 1. Prerequisites
- Install Python 3
- Clone this repository

### 2. Install required packages
run following command in your terminal.
```
pip install -r requirements.txt
```
### 3. Set environment variables
```
export USER_NAME={Your username}
export USER_PASS={Your passphrase}
export OPENAI_API_ENDPOINT={Your Azure OpenAI API endpoint URL}
export OPENAI_API_VERSION={API Vearsion (eg:2023-03-15-preview)}
```

### 4. Run the application
```
streamlit run app.py
```

## Deploy to Azure
### 1. Deploy App Service
Deploy Python Stack Web Apps

### 2.Deploy this application
Web Apps > Deployment Center > Setting
- Source : External Git
- Repository : https://github.com/07JP27/K-SEC-2023-ChatGPT-Client
- Branch : main
- Repository Type : Public

![image](https://github.com/07JP27/openai-client/assets/11060273/ddb1893c-6384-47a2-bf17-ebe7b90e2139)

And click Save button.

### 3.Set startup command
Web Apps > Configuration > General settings > Startup Command

```
python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0
```

![image](https://github.com/07JP27/openai-client/assets/11060273/32fe52a8-15d6-40e2-80ea-10dae3e6457b)

And click Save button.
 
### 4. Set up Managed ID
Go to Web Apps > Identity 

Turn on statu and click Save button.

![2023-06-05_10h56_10](https://github.com/07JP27/openai-client/assets/11060273/515e01e2-b139-479e-aee7-a5b93041f17e)

Go to Azure Onpen AI > Access control(IAM)

Click Add and select Add role assingment.

![2023-06-05_10h58_13](https://github.com/07JP27/openai-client/assets/11060273/4903b974-eae3-44b2-9ec5-b9a258cf85ac)

Select Role as `Cognitive Services User` and Select Web Apps's Managed ID in member section.

Finaly, Click Review+assign.

![2023-06-05_10h58_01](https://github.com/07JP27/openai-client/assets/11060273/2193df82-2a43-48a0-8e76-86d0258b6ad2)

### 5. Set Enviroment variables
Web Apps > Configuration > Application settings

- USER_NAME : Simple auth username
- USER_PASS : Simple auth passphrase
- OPENAI_API_ENDPOINT : Your Azure Open AI API endpoint URL
- OPENAI_API_VERSION : API Vearsion (2023-03-15-preview)

![2023-06-05_11h26_35](https://github.com/07JP27/openai-client/assets/11060273/4c4bd961-3282-41d7-87e7-d96e83fd3dea)

And click Save button.

### Access and Enjoy your private ChatGPT!
If you want to set up authentication to client app, Please refer to following document.
https://learn.microsoft.com/en-us/azure/app-service/scenario-secure-app-authentication-app-service
