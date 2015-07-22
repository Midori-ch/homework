#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

"""

student_scores = {
        "Tom":[80,100,90,95],
        "John":[100,93,75,80],
        }

#count score
tom_score = ((sum(student_scores['Tom'])) / 4)
john_score = ((sum(student_scores['John'])) / 4)

#print score
print ("Average of Tom:%s" % (tom_score))
print ("Average of John:%s" % (john_score))
