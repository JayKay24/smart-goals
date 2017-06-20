# -*- coding: utf-8 -*-
import hashlib # Used for hashing

class User(object):
    # User created when __init__ runs

    def __init__(self, full_name, email, password):
        self.fullname = full_name
        self.email = email
        
        # make password into hash
        hash_object = hashlib.sha1(password.encode())
        self.password = hash_object.hexdigest()

        self.user_details = {'name':self.fullname, 'email':self.email, 'password': self.password}


    # Get User details
    def getUser(self):
        return self.user_details
    

    def updateUser(self, full_name, email):
        self.fullname = full_name
        self.email = email

        return {'name': self.fullname, 'email': self.email}


class Bucketlist(object):
    def __init__(self, bucketlist_name, bucketlist_description):
        pass


class Bucketlist_Activities(Bucketlist):
    def __init__(self, bucketlist_activity_name, bucketlist_description, due_date):
        super(Bucketlist_Activities, self).__init__()
        self.done = False