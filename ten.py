#10
class Bank:
	def __init__(self,p,t,r):
		self.p = p
		self.t = t
		self.r = r

	def simple_interest(self):
		si = (self.p * self.t * self.r)/100
		print('The Simple Interest is', si)
		return si
	def compound_interest(self):
		ci = self.p * ( (1+self.r/100)**self.t - 1)
		print('The compound Interest is',ci)
		return ci
pnb = Bank(2,3,4)
icici = Bank(3,5,3)
hdfc = Bank(3,6,7)

pnb.simple_interest()
pnb.compound_interest()

icici.simple_interest()
icici.compound_interest()

hdfc.simple_interest()
hdfc.compound_interest()