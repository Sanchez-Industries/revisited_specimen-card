#coding: utf-8
import random as rnd
import time
import os
import hashlib
from os import system
class specimen(object):
	def generate_mem(self):
		rnd.seed(self.seed)
		self.card = {}
		for c in self.cols:
			for r in self.rows:
				code = ""
				for i in range(0,self.sizecode):
					code = code + rnd.choice(self.caracts)
				self.card[c+":"+r] = code

	def generate_card(self,filepath):
		self.generate_mem()
		f = open(filepath,"w")
		f.write(",".join(self.cols)+"\n")
		for r in self.rows:
			f.write(r+",")
			kk=[]
			for c in self.cols:
				kk.append(self.card[c+":"+r])
			f.write(",".join(kk)+"\n")
		f.close()

	def  __init__(self,seed=0):
        self.seed = seed
        self.card = {}
        self.sizecode = 5
        self.cols = ["A","B","C","D","E","F","G","H"]
        self.rows = ["1","2","3","4","5","6","7","8"]
        self.caracts = "AZERTYUIOPQSDFGHJKLMWXCVBN0123456789"
        
    def load_reset_keyfile(self):
        system("echo $(cat {filepath}.priv | base64) > {filepath_}.priv".format(
            filepath = self.reset_key_path,
            filepath_ = self.reset_key_path
        ))
        f=open(self.reset_key_path,'rb')
        self.keyfile = f.read()
        f.close()
        
	def verify_key(self, key):
		return hashlib.sha512(key).hexdigest() == self.keyfile
		
	def set_key(self, keypath):
		f = open(keypath, 'rb')
		self.seed = f.read()
		f.close()
		self.generate_mem()

	def isValid(self, locate, code):
		if locate == "": return False
		return self.card[locate] == code

	def ask(self):
		rnd.seed(time.time())
		return rnd.choice(self.cols)+":"+rnd.choice(self.rows)

	def generate_crypto_key_file(self,filepath="bases/reset-key.key",size=4096):
        print("Vous allez creer une cle RSA.")
		system("openssl genrsa -out {filepath}.pem -aes256 4096".format(
            filepath = filepath
        ))
        print("changement des droits du fichier ({filepath}.pem) ...".format(
            filepath = filepath
        ))
        system("chown -R $USER:$USER {filepath}.pem".format(
            filepath = filepath
        ))
        print("Extraction de la clé privée...")
        system("openssl rsa -out {filepath_1}.priv < {filepath_0}.pem".format(
            filepath_0 = filepath,
            filepath_1 = filepath
        ))
        print("changement des droits du fichier ({filemath}.priv)".fomat(
            filepath = filepath
        ))
        system("chown -R $USER:$USER {filepath}.priv".format(
            filepath = filepath
        ))
		
		
# =====================================
# 		 !! USE THAT UNDER !!		
# =====================================
class specimenation(object):
	def __init__(self):
		pass
		
	def generate_reset_key():	
		specard = specimen()
		specard.generate_crypto_key_file()

	def generate_key_and_card(card_name):
		specard = specimen()
		specard.generate_crypto_key_file("bases/"+card_name+".key",size=4000000)
		specard.set_key("bases/"+card_name+".key")
		specard.generate_card("bases/"+card_name+".txt")

	def ask_key(card_name):
		specard = specimen()
		specard.set_key("bases/"+card_name+".key")
		asked = specard.ask()
		#code ??
		validity = specard.isValid(asked,code)
		return validity

	def test(card_name):
		#test
		specard = specimen()
		specard.set_key("bases/"+card_name+".key")
		asked = specard.ask()
		print (asked)
		code = input(">")
		validity = specard.isValid(asked,code)
		print (validity)

        
