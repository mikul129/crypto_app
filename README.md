# crypto_app
## Description
 A tool for encoding messages using the RSA method.
 
The RSA algorithm is an asymmetric cryptography algorithm; this means that it uses a public key and a private key (i.e two different, mathematically linked keys). As their names suggest, a public key is shared publicly, while a private key is secret and must not be shared with anyone. [more about RSA](https://www.educative.io/edpresso/what-is-the-rsa-algorithm)

## Documentation

Documentation created with the Sphinx tool. To run the documentation, open the file in docs / index.html. The documentation page looks like this:
![documentation_part](https://user-images.githubusercontent.com/41323564/110986932-a0a8f280-836e-11eb-8986-4fff17784e94.png)


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
### GET /generate_keys<br />
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

### POST /encode<br />
Example<br />
Request URL:<br /> 'http://127.0.0.1:8000/encode'<br />

Request body:<br />
```json
{
  "original_text": "Lorem ipsum dolor...",
  "public_key": [
    "0x1d79b5325aa056f224dc81f",
    "0x36c2c5873b3ec72266122af"
  ]
}
```
Response body:<br />
```json
{
  "encode_text": [
    "0x2dfb921b29ba5e0fb5e68cc",
    "0x2830711e86a1a230ff0f113",
    "0x34de023baa46994e7ac786e",
    "0x1af2c75bd6739600e44b96b",
    "0x250a5f0e0f7f593ce5db336",
    "0xd9f1fb45e13d90e45cdece",
    "0x24c4df12ed2a51488496be",
    "0x34551d532776a8075aaf77c",
    "0x12e7cc9dc0f26fc0a1dd275",
    "0x1cd4f2c9fc078c1ed943f5b",
    "0x250a5f0e0f7f593ce5db336",
    "0xd9f1fb45e13d90e45cdece",
    "0x34481ff70651c2dcc798392",
    "0x2830711e86a1a230ff0f113",
    "0x14f7ddda723111d9107c28c",
    "0x2830711e86a1a230ff0f113",
    "0x34de023baa46994e7ac786e",
    "0x2018bea43a60f35bb8823f4",
    "0x2018bea43a60f35bb8823f4",
    "0x2018bea43a60f35bb8823f4"
  ]
}
```

### POST /decode<br />
Example<br />
Request URL:<br /> 'http://127.0.0.1:8000/decode'<br />

Request body:<br />
```json
{
  "encode_text": [
    "0x2dfb921b29ba5e0fb5e68cc",
    "0x2830711e86a1a230ff0f113",
    "0x34de023baa46994e7ac786e",
    "0x1af2c75bd6739600e44b96b",
    "0x250a5f0e0f7f593ce5db336",
    "0xd9f1fb45e13d90e45cdece",
    "0x24c4df12ed2a51488496be",
    "0x34551d532776a8075aaf77c",
    "0x12e7cc9dc0f26fc0a1dd275",
    "0x1cd4f2c9fc078c1ed943f5b",
    "0x250a5f0e0f7f593ce5db336",
    "0xd9f1fb45e13d90e45cdece",
    "0x34481ff70651c2dcc798392",
    "0x2830711e86a1a230ff0f113",
    "0x14f7ddda723111d9107c28c",
    "0x2830711e86a1a230ff0f113",
    "0x34de023baa46994e7ac786e",
    "0x2018bea43a60f35bb8823f4",
    "0x2018bea43a60f35bb8823f4",
    "0x2018bea43a60f35bb8823f4"
  ],
  "private_key": [
    "0x2030417d240fb7322c340cf",
    "0x36c2c5873b3ec72266122af"
  ]
}
```
Response body:<br />

```json
{
  "original_text": "Lorem ipsum dolor..."
}
```

## Contact
mikulski.michal2@gmail.com
