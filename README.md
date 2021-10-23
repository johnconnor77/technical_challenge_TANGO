# Tecnhical Challenge TANGO
 
---
This API is  a simple service to help users schedule appointments.



![my-schedule-was-wide-open-pete-davidson](https://user-images.githubusercontent.com/51679898/138545919-8dd69dfe-9a76-4f95-9fb0-b97f2e0db419.gif)

## Environment

GNU/Linux 


## How to install
1. Clone the repository below

`https://github.com/johnconnor77/technical_challenge_TANGO`

2. Install dependencies from requirements.txt

`pip install -r requirements.txt`

3. Execute the following command for Application startup at repository root

`./sabrina_date.py `



##  Files

File Name | Description
--- | ---
`sabrina_date.py` | Executable file for API schema 
`worker.py` | Background job for Redis database 
`appointment_models/__init__.py` |  Module with AppointmentModel  class that specifies the format and data type of input by User post request
`utils/redis_object.py & utils/redis_functions.py` | Files that allows to handle redis connection and the data manipulation over database(SET,GET redis methods)
`utils/extra_functions.py` | Functions that allows handling restrictions over POST request
`requirements.txt & runtime.txt` |  Files that specifies python runtime version and requirements of modules
`Procfile` |  File that specifies the commands that are executed by the app on Heroku startup

## Example Usage

### Local Example

#### cURL

Type the following command at your shell prompt

##### POST

`curl --location --request POST 'http://127.0.0.1:5000/api/schedule/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "user_id": 71697,
  "date_appointment": "2021-11-20",
  "start_time": "9:00",
  "end_time": "9:30"
}'`

##### GET

`curl -X 'GET' \
  'http://127.0.0.1:5000/api/appointments/?user_id=71697' \
  -H 'accept: application/json'`


![curl_examples](https://user-images.githubusercontent.com/51679898/138545800-71762bb2-f739-4b4d-813a-326a28bb7d17.png)


#### Postman


##### POST


![POST-localhost](https://user-images.githubusercontent.com/51679898/138546083-f814677e-39a7-4db8-99cf-858cbe0d0f7d.png)


##### GET


![GET-localhost](https://user-images.githubusercontent.com/51679898/138546090-8f2176e4-948b-4703-8e0f-83f8f6270239.png)



## Remote Testing 

Sabrina Date API was deployed at Heroku where you can also test it from the docs endpoint

[https://sabrina-date-tango.herokuapp.com/docs](https://sabrina-date-tango.herokuapp.com/docs/)


#### Postman


##### POST

![POST-HEROKU](https://user-images.githubusercontent.com/51679898/138546282-c24fca78-cb82-4ecd-9d1c-95d66c78ad03.png)


##### GET


![GET-HEROKU](https://user-images.githubusercontent.com/51679898/138546284-43c0d20f-093b-4f8d-97c4-7a585d82dc9b.png)


### NOTES:

In case you clone this repository for trying locally, have in mind to change this variable HEROKU to *False*

![HEROKU-settings](https://user-images.githubusercontent.com/51679898/138546997-58a4d420-7886-4673-9108-017d0b9c4d0a.png)


Author:

* **Juan F. Calle**  - [johnconnor77](https://github.com/johnconnor77)
