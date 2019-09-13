# Authentication using OAuth2 Protocol
This project is done as part of MyWallSt selection process.



### Brief :
Project is a sample API written in Python + Django and Django REST Framework. The purpose of the API is to provide an authorization service for mobile clients (mobile apps) based on the OAuth2 protocol.

### Main third party libraries used



| Library        | Objective |
| ------------- |:-------------|
| [djangorestframework](https://www.django-rest-framework.org/)     | Design API Requests      |
| [django-oauth-toolkit](https://django-oauth-toolkit.readthedocs.io/en/latest/) | Django OAuth Toolkit helped providing out of the box all the endpoints, data and logic needed to add OAuth2 capabilities to my Django project.|
| [django-use-email-as-username](https://pypi.org/project/django-use-email-as-username/)      | Configuring the **User** model to be email based instead of username based.|

### Deployment

Project was deployed on a Heroku Free Plan under the URL `https://agile-hamlet-49567.herokuapp.com`

## API Documentation

**[POST]** - Register
```
/authentication/register/
```
| Field        | Description |
| ------------- |:-------------|
| email   | User's email address.|
| password| User's secure password.|

*Example*
```
{
	"email":"john@smith.com",
	"password":"password"
}
```
*Response*
```
{
    "access_token": "yjaIrGi0lxKfwAJwINhGh8piQjVvbz",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write",
    "refresh_token": "d2PYIAMG4RtawUlDqBkNrzojpI2JAY"
}
```
___

**[POST]** - Login
```
/authentication/token/
```
| Field        | Description |
| ------------- |:-------------|
| email   | User's email address.|
| password| User's secure password.|

*Example*
```
{
	"email":"john@smith.com",
	"password":"password"
}
```
*Response*
```
{
  "access_token": "dd8wO9BGubktwB6eQjQiQsPP4ZouRH",
  "expires_in": 36000,
  "token_type": "Bearer",
  "scope": "read write",
  "refresh_token": "IP3CKafG7wxs2tlMGfiTt5umLzrZU1"
}

```

___

**[POST]** - Refresh Token
```
/authentication/token/refresh/
```
| Field        | Description |
| ------------- |:-------------|
| refresh_token   | Latest Refresh token stored.|

*Example*
```
{
	"refresh_token":"IP3CKafG7wxs2tlMGfiTt5umLzrZU1",
}
```
*Response*
```
{
    "access_token": "uIpZg94QM23LIIVvbns9aQAM2IVrNR",
    "expires_in": 36000,
    "token_type": "Bearer",
    "scope": "read write",
    "refresh_token": "HyXHTCtrOSlPmNAaBKlRBVkBnccNwX"
}

```
