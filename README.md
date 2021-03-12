# crypto_app
## Description
 A tool for encoding messages using the RSA method.
 
The RSA algorithm is an asymmetric cryptography algorithm; this means that it uses a public key and a private key (i.e two different, mathematically linked keys). As their names suggest, a public key is shared publicly, while a private key is secret and must not be shared with anyone. [more about RSA](https://www.educative.io/edpresso/what-is-the-rsa-algorithm)

## Files

app/main.py - file with api methods<br />
app/RSA.py - file with encode and decode methods<br />
app/RSA_key_generator.py - file for public and private keys generator<br />
app/unit_tests.py - aplication unit tests
docker-compose.yml - docker compose configuration
Dockerfile - file docker for image configuration

## Library

fastapi==0.63.0

## Quick start
If you want to run the application, all you have to do is enter the project folder and call:<br />
`docker-compose build`<br />
`docker-compose up`

The API aplication works at 'http://127.0.0.1:8000/'

## Authorization API

Api has HTTP Basic Auth for simple authorization. Default authorization data:<br />
Login: user<br />
Password: pass<br />

## API methods
###`GET /generate_keys`<br />
Example<br />
Request URL:<br /> 'http://127.0.0.1:8000/generate_keys'<br />

Response body:<br />
```json
{
  "public_key": [
    "0x1d79b5325aa056f224dc81f",
    "0x36c2c5873b3ec72266122af"
  ],
  "private_key": [
    "0x2030417d240fb7322c340cf",
    "0x36c2c5873b3ec72266122af"
  ]
}
```
Response header:<br />
```json
content-length: 144 
content-type: application/json 
date: Fri,12 Mar 2021 08:31:07 GMT 
server: uvicorn 
```

`POST /encode`<br />
`POST /decode`<br />

## Contact
mikulski.michal2@gmail.com
