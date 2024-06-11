
import os
import json
import requests
from firebase_admin import auth



FIREBASE_WEB_API_KEY = 'AIzaSyBn5j66LqXPJ9cUnz4im5qygNdk__SWXdc'
REST_API_URL = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword'

def sign_in_with_email_and_password(email: str, password: str, return_secure_token: bool = True):
    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": return_secure_token
    })

    r = requests.post(REST_API_URL, params={"key": FIREBASE_WEB_API_KEY}, data=payload)
    return r.json()

# firebase_utils.py


def verify_firebase_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return uid
    except Exception as e:
        return None
