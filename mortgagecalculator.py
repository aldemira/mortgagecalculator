#!/usr/bin/python

'''
    Copyright (c) 2017 Aldemir Akpinar <https://github.com/aldemira>
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


############## Configuration ##################
#Mortgage Interest (Monthly)
interest=0.0071
#Total Borrowed Sum
borrowed=165000

#Payment Term
term=120
#Fixed installments
payment = 2047.53

# Interest to close the mortgage account
ceaseint = 0.04

############# End Configuration ##############

left = borrowed
topay = payment*term

i = 1
while term>0:
	minterest = left*interest
	left = (minterest + left) - payment
	mcapital = payment - minterest
        tocease = (left * ceaseint) + left
        topay = topay - payment
        print "TERM: %d PAYMENT: %f (CAPITAL: %f INTEREST:%f) LEFT: %f TO CEASE: %f TO PAY: %f" % (i,payment, mcapital, minterest, left, tocease, topay)
	term = term - 1
	i = i + 1

