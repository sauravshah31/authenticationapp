# Authenticationapp
Python Flask REST API authentication app

# directory structure
```
authenticationapp
├── README.md
├── requirements.txt  
├── docs                    //documentation
|   ├── authorize_api.md    //doc forapi routes
├── src
|   ├── api_test.py         //test cases for api routes  
|   ├── app.py              //main
|   ├── authorizerapp
|   |   ├── config.py       //app config file
|   |   ├── authorize       //handle for route /api/...
|   |   ├── main            //homepage renderer
|   |   ├── static          //static files
|   |   ├── models          //database models


```

# Running the script
```
#clone the repo
git clone https://github.com/sauravshah31/authenticationapp.git
cd authenticationapp

#create a virtual environment
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate

#install requirements
pip install -r requirements.txt

#run the server
python src/app.py
```
