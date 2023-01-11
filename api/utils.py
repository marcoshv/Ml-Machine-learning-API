import hashlib
import imp
import pathlib
import os


def allowed_file(filename):
    """
    Checks if the format for the file received is acceptable. For this
    particular case, we must accept only image files. This is, files with
    extension ".png", ".jpg", ".jpeg" or ".gif".

    Parameters
    ----------
    filename : str
        Filename from werkzeug.datastructures.FileStorage file.

    Returns
    -------
    bool
        True if the file is an image, False otherwise.
    """
    # Current implementation will allow files with extension ".png", ".jpg", ".jpeg" or ".gif".
    # TODO
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")): # .lower() to be case insensitive
        return True
    else:
        return False


def get_file_hash(file):
    """
    Returns a new filename based on the file content using MD5 hashing.
    It uses hashlib.md5() function from Python standard library to get
    the hash.

    Parameters
    ----------
    file : werkzeug.datastructures.FileStorage
        File sent by user.

    Returns
    -------
    str
        New filename based in md5 file hash.
    """
    # Returns a new filename based on the file content using MD5 hashing.
    # TODO
    file_ext = pathlib.Path(file.filename).suffix # returns the file extension
    hash = hashlib.md5(file.read()).hexdigest() # returns the hash filename
    filename = hash+file_ext
    file.seek(0)
    return filename
