#!/usr/bin/python 3
# -*- coding : utf-8 -*-

'a test module'

class Students(object):

    def __init(self, name, score):
        self.name = name
        self.score = score

    def print_info(self):
        print('%s \'s score is %s' % (self.name, self.score))

    def judscore(self):
        if self.score > 90:
            return 'A'
        elif self.score > 80:
            return 'B'
        elif self.score > 70:
            return 'C'
        elif self.score > 60:
            return 'D'
        else:
            return 'E'


