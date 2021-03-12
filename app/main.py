from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from RSA import encode_RSA, decode_RSA
from RSA_key_generator import generate_keys_RSA
from pydantic import BaseModel
import uvicorn
import secrets

class to_encode(BaseModel):
    original_text: str
    public_key: list

class to_decode(BaseModel):
    encode_text: list
    private_key: list
    
app = FastAPI()
    
security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    """
|    The method that performs user authentication.
|    Default credentials:
|    **Login:** user
|    **Password:** pass
    
    :param credentials: credentials
    :return: credentials.username
    """
    correct_username = secrets.compare_digest(credentials.username, "user")
    correct_password = secrets.compare_digest(credentials.password, "pass")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
 
@app.get("/")
def default():
    """
    default method
    """
    return "crypto-app API"
 
@app.post("/decode")
async def decode(To_decode: to_decode, username: str = Depends(get_current_username)):
    """
|    The method for decode message. /decode
|    **Example body request:**
|    {
|        "encode_text": 
|        [your_encode_text],
|        "private_key":
|        [your_private_key]
|    }

    :param To_decode: to_decode [BaseModel]
    :param username: get_current_username [function]    
    :return: original_text [plaintext]
    """
    
    plaintext = decode_RSA(To_decode.encode_text, To_decode.private_key)
    return {"original_text": plaintext}

@app.post("/encode")
async def encode(To_encode: to_encode, username: str = Depends(get_current_username)):
    """
|    The method for encode message. /encode
|    **Example body request:**
|    {
|        "original_text": 
|        [your_original_text],
|        "public_key":
|        [your_public_key]
|    }

    :param To_encode: to_encode [BaseModel] 
    :param username: get_current_username [function]    
    :return: encode_text [list]
    """
    
    encode_text = encode_RSA(To_encode.original_text, To_encode.public_key)
    return {"encode_text": encode_text}

@app.get("/generate_keys")
def generate_keys(username: str = Depends(get_current_username)):
    """
    The method for generate keys. /generate_keys
    
    :param username: get_current_username [function]    
    :return: public_key [list], private_key [list], 
    """
    
    public_key, private_key = generate_keys_RSA()
    return {"public_key": public_key, "private_key": private_key}