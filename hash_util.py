import hashlib
import json


def hash_string_256(string):
    """ Create a SHA-256 hash of a string. """
    return hashlib.sha256(string.encode()).hexdigest()


def hash_block(block):
    return hash_string_256(json.dumps(block, sort_keys=True).encode())