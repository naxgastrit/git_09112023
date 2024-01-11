import datetime

import jwt

import settings

payload = {
    "my_name": "Ilya",
    "age": 16,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
}

encode_jwt = jwt.encode(
    payload=payload,
    key=settings.JWT_SECRET,
    algorithm="HS256",
)
print(encode_jwt)


def encode_jwt(payload: dict) -> str:
    return jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET,
        algorithm="HS256",
    )


def decoded_jwt(encoded_jwt_str: str) -> dict:
    try:
        return jwt.decode(
            encoded_jwt_str,
            settings.JWT_SECRET,
            algorithms=["HS256"],
        )
    except jwt.exceptions.ExpiredSignatureError:
        return {}
    except jwt.exceptions.InvalidSignatureError:
        return {}


data = encode_jwt(payload)

result = decoded_jwt(data)
