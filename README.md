# Tecnhical Challenge TANGO
 
---
This API is  a simple service to help users schedule appointments.


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
`appointment_models/__init__.py` |  Module with AppointmentModel  class that specifies the format and data type of input by User post request
`requirements.txt & runtime.txt` |  Files that specifies python runtime version and requirements of modules
`Procfile` |  File that specifies the commands that are executed by the app on startup

## Example Usage

### Local Example

#### cURL

Type the following command at your shell prompt

`curl -X 'GET' \
  'http://127.0.0.1:5000/api/appointments/?user_id=1020450794' \
  -H 'accept: application/json'`



### Remote Example 

Sabrina Date API 




Author:

* **Juan F. Calle**  - [johnconnor77](https://github.com/johnconnor77)
