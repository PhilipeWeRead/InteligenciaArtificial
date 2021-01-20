class Environment :
"""
implementacao da classe interface
"""
	def initial_percepts ( self ):
		raise NotImplementedError (’ initial_percepts ’)

	def signal ( self , action ) :
 		raise NotImplementedError (’signal ’)

class Agent :
 """
 uma interface para agente
 """
	def __init__ ( self , env ):
		self . env = env

	def act ( self ) :
		raise NotImplementedError (’act ’)
