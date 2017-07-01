class cTwo(cLayersIdentifyFiles):
	def __init__(self):
		print 'init two'

	def hello(self):
		print 'two'

	def Analyse(self, sFilename):
		print self.__class__.__name__ + ":" + sFilename