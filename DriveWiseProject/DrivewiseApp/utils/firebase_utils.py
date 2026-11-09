
import os
import json
import requests
from django.core.exceptions import ImproperlyConfigured
from firebase_admin import auth


REST_API_URL = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword'


def get_firebase_web_api_key() -> str:
    """Return the Firebase Web API key from the environment.

    Loaded from the `FIREBASE_WEB_API_KEY` entry in the project's .env file
    (see the Configuration section of the README). Read lazily so that a
    missing value surfaces as a clear configuration error on sign-in rather
    than an opaque 400 from the Identity Toolkit endpoint.
    """
    api_key = os.environ.get('FIREBASE_WEB_API_KEY')
    if not api_key:
        raise ImproperlyConfigured(
            "FIREBASE_WEB_API_KEY is not set. Add it to your .env file - you "
            "can find it in the Firebase console under "
            "Project settings > General > Web API Key."
        )
    return api_key


def sign_in_with_email_and_password(email: str, password: str, return_secure_token: bool = True):
    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": return_secure_token
    })

    r = requests.post(REST_API_URL, params={"key": get_firebase_web_api_key()}, data=payload)
    return r.json()

# firebase_utils.py


def verify_firebase_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return uid
    except Exception as e:
        return None
