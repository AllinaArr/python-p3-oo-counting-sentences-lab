#!/usr/bin/env python3

class MyString:
    def __init__(self, first_value=''):
        self._value = first_value
      
    @property
    def value(self):
      return self._value
    
    @value.setter
    def value(self, new_value):
      if isinstance(new_value, str):
        self.value = new_value
      else:
        print("The value must be a string.")
      
    def is_sentence(self):
      return self.value[-1] == '.'
    
    def is_question(self):
      return self.value[-1] == '?'
        
    def is_exclamation(self):
      return self.value[-1] == '!'
    
    def count_sentences(self):
      new_value = self.value.replace('!', '.').replace('?','.')
      l = new_value.split('.')
      count = 0
      for item in l:
        if len(item) != 0:
          count += 1
      return count
    
    