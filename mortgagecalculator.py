#!/usr/bin/python


interest=0.0071
borrowed=165000
left = borrowed

term=120
payment = 2047.53
topay = payment*term

i = 1


while term>0:
	minterest = left*interest
	left = (minterest + left) - payment
	mcapital = payment - minterest
        tocease = (left * 4 / 100) + left
        topay = topay - payment
        print "TERM: %d PAYMENT: %f (CAPITAL: %f INTEREST:%f) LEFT: %f TO CEASE: %f TO PAY: %f" % (i,payment, mcapital, minterest, left, tocease, topay)
	term = term - 1
	i = i + 1

