class cOne(cLayersIdentifyFiles):
	def __init__(self):
		print 'init one'

	def hello(self):
		print 'one'

	def Analyse(self, sFilename):
		print self.__class__.__name__ + ":" + sFilename