from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
api = Api(app)

ALPHABET = " ,.:(_)-0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
users = []
methods = [
    {"id": 1, "caption": "CAESAR", "json_params": '{"shift": "int"}', "description": "Caesar cipher"},
    {"id": 2, "caption": "VIGENERE", "json_params": '{"key": "string"}', "description": "Vigenere cipher"}
]
sessions = []
user_counter = 1
session_counter = 1

from itertools import cycle
def form_dict():
    return dict([(i, chr(i)) for i in range(128)])

def comparator(value, key):
    return dict([(idx, [ch[0], ch[1]])
                for idx, ch in enumerate(zip(value, cycle(key)))])

def encode_val(word):
    d = form_dict()
    return [k for c in word for k,v in d.items() if v == c]

def full_encode(value, key):
    d = comparator(value, key)
    l = len(form_dict())
    return [(v[0] + v[1]) % l for v in d.values()]

def decode_val(list_in):
    l = len(list_in)
    d = form_dict()
    return [d[i] for i in list_in if i in d]

def full_decode(value, key):
    d = comparator(value, key)
    l = len(form_dict())
    return [(v[0] - v[1]) % l for v in d.values()]

def coder():
    for i in b:
        if i in c:
            print(chr(ord(i)), end='')
        if i.islower():
            if ord(i) + a > ord('я'):
                print(chr(ord(i) + a - 32), end='')
            else:
                print(chr(ord(i) + a), end='')

        elif i.isupper():
            if ord(i) + a > ord('я'):
                print(chr(ord(i) + a - 32), end='')
            else:
                print(chr(ord(i) + a), end='')
    return()

class User:
         def __init__(self, login, secret):
               self.login = login
               self.secret = secret
class Method:
          def __init__(self, id, caption, json_params, description):
                    self.id = id
                    self.caption = caption
                    self.json_params = json_params
                    self.description = description
class Session:
        def __init__(self, id, user_id, method_id, data_in, params, data_out, status, created_at, time_op):
                 self.id = id
                 self.user_id = user_id
                 self.method_id = method_id
                 self.data_in = data_in
                 self.params = params
                 self.data_out = data_out
                 self.status = status
                 self.created_at = created_at
                 self.time_op = time_op
class API:
        def __init__(self):
               self.users = []
               self.methods = []
               self.sessions = []

def add_user(self, login, secret):
         if not any(user.login == login for user in self.users):
                     self.users.append(User(login, secret))
         else:
                    print("User with login {} already exists.".format(login))
def view_users(self):
          for user in self.users:
                    print(user.login)
def add_method(self, id, caption, json_params, description):
                    self.methods.append(Method(id, caption, json_params, description))

def encrypt_decrypt_data(self, method_id, data):
         method = next((method for method in self.methods if method.id == method_id), None)
         if method:
                  print("Using method {} to encrypt/decrypt data: {}".format(method.caption, data))
         else:
                  print("Method with id {} not found.".format(method_id))

def get_session_data(self, session_id):
          session = next((session for session in self.sessions if session.id == session_id), None)
          if session:
                return session
          else:
                print("Session with id {} not found.".format(session_id))
def delete_session(self, session_id, secret):
          session = next((session for session in self.sessions if session.id == session_id and any(user.secret == secret for user in self.users if user.id == session.user_id)), None)
          if session:
                 self.sessions.remove(session)
                 print("Session with id {} deleted.".format(session_id))
          else:
                 print("Session with id {} and secret not found.".format(session_id))

