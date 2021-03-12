# crypto_app
## Description
 A tool for encoding messages using the RSA method.
 
The RSA algorithm is an asymmetric cryptography algorithm; this means that it uses a public key and a private key (i.e two different, mathematically linked keys). As their names suggest, a public key is shared publicly, while a private key is secret and must not be shared with anyone. [more about RSA](https://www.educative.io/edpresso/what-is-the-rsa-algorithm)

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

`POST /decode`
`POST /encode`
`GET /generate_keys`

## Contact
mikulski.michal2@gmail.com
