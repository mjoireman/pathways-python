from .credentials import Credentials
import logging

_default_credentials = None

def set_default_credentials(file_path: str) -> None:
    global _default_credentials
    _default_credentials = Credentials.from_file(file_path)
    

def get_default_credentials() -> Credentials:
    global _default_credentials
    if not _default_credentials:
        creds = Credentials.from_env()
        if creds:
            _default_credentials = creds
        else:
            raise ('Credentials not found')
    return _default_credentials


def unset_default_credentials() -> None:
    global _default_credentials
    _default_credentials = None
