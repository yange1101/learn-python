import random
from urllib import urlopen
import sys

word_url = "http://learncodethehardway.org/words.txt"
words = []

phrases = {
    "class %%%(%%%):":
        "Make a class named %%% that is -a %%%.",
    "class %%%(object"
}