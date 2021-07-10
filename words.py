import string
import random
import json

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    word_list = open("word.txt","r")
    line=word_list.readline()
    word_list=line.split()
    return word_list

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word

