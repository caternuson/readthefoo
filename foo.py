"""
`foo`
================

A bunch of foo used to learn Sphinx documenation and Read The Docs.

* Author(s): Carter Nelson
"""

class Foo:
    '''A Foo class which does some stuff.'''

    def __init__(self):
        self._secret = 42

    def feed_pet(self, pet):
        '''Feed the provided pet.

        :param Pet pet: an instance of Pet class

        :return: True if pet ate the food
        '''
        pet.feed()
        return True
