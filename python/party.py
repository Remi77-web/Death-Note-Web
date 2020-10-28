import random
import numpy

INIT_POINTS=3
playersList=[]
places=[True, True, True, True, True]
popularity=0
suspection=0
cibledCriminals=[]
cards=["gun", "handcuffs", "candies", "criminal", "falseBadge", "helmet", "mandate",
"markup", "deathNote", "chest", "apple", "shinigamiEyes", "watariPC", "rope",
"penberPC"]
cardsPoints=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

"""the different player's variables are stocked here"""
class player:

	def __init__(self, charactere, pseudo, name, team):
		self.pseudo=pseudo
		self.name=name
		self.charactere=charactere
		self.actions=[]
		self.actionsOption=[]
		#self.actionPoints=0
		self.playersKnow=[]
		self.team=team
		self.hand=[]
		self.draw=[]
		self.drawSelec=[]
		self.spy=[]
		self.handcuffs=[]
		#self.attribute (handcuffs, helmet, falseBadge...)
		#cheat
		self.hide=False
		self.area=0
		self.alive=True

	def show(self):
		print("pseudo= ", self.pseudo, 
		"\nname= ", self.name, 
		"\ncharactere= ", self.charactere,
		"\nactions= "	, self.actions,
		"\nactionsOption= ", self.actionsOption,
		"\nplayersKnow= ", self.playersKnow,
		"\nteam= ", self.team,
		"\nhand= ", self.hand,
		"\ndraw= ", self.draw,
		"\ndrawSelec= ", self.drawSelec,
		"\nspy= ", self.spy,
		"\nhide= ", self.hide,
		"\narea= ", self.area,
		"\nalive= ", self.alive)

	def move(self, num):
		self.area=num

	"""cards functions"""

	"""kill the mentionned player"""
	def _gun(self, pseudo):
		player=find(pseudo)
		if player in playersList:
			player.alive=False
			playersList.remove(find(pseudo))
		else:
			print("error, player already dead\n")

	"""see all the mentionned player's movements and conversely"""
	def _handcuffs(self, pseudo):
		player=find(pseudo)
		player.handcuffs=self.pseudo
		self.handcuffs=pseudo

	"""add 2 action points"""
	def _candies(self):
		pass
		
	"""Depend of your team:
	POLICE: focus one (random) criminal. If Light kill him, the suspection gauge increase by ?.
	LIGHT: focus one (random) criminal. If one player of the police team the same, his identity gauge increase"""
	def _criminal(self, criminalName):
		if criminalName not in cibledCriminals:
			cibledCriminals.append(criminalName)

	"""give a False name to the other players"""
	def _falseBadge(self):
		pass

	"""hide your face, protect ou from the shinigami eyes"""
	def _helmet(self):
		self.hide=True

	"""see what a player take from the deck this day"""
	def _mandate(self, pseudo):
		player=find(pseudo)
		player.mandate=self.pseudo

	"""forbide one access' place during the next night"""
	def _markup(self, num):
		try:
			places[i]=False
		except:
			print("error, number invalid")

	"""kill the mentionned player if you know his real name or kill a criminal to increase
	the citizen support gauge"""
	def _deathNote1(self, pseudo, name):
		player=find(pseudo)
		if player in playersList:
			if(player.name==name):
				player.alive=False
				playersList.remove(find(pseudo))
				#popularity-=1 ?
		else: 
			print("error, player already dead\n")

	def _deathNote2(self, criminalName):
		global suspection
		global popularity
		if criminalName in cibledCriminals:
			suspection+=1
		popularity+=1


	"""hide the cards that you take from this day and choose the cards that people will see if
	they used a mandate"""
	def _chest(self, falseDraw, falseDrawSelec):
		player.draw=falseDraw
		player.drawSelec=falseDrawSelec


	"""ask Ryuuk to kill one player, even if you don't his name"""
	def _apple(self, pseudo):
		player=find(pseudo)
		player.alive=False


	"""see the real name of one player the next night if you're in the same place this night"""
	def _shinigamiEyes(self):
		for player in playersList:
			if self.area==player.area:
				if player.hide==False:
					if [player.pseudo, player.name] not in self.playersKnow:
						self.playersKnow.append([player.pseudo, player.name])


	"""allow L to give orders to the police team"""
	def _watariPC(self):
		pass

	"""increase a lot the suspection gauge but kill yourself"""
	def _rope(self):
		global suspection
		suspection+=1
		playersList.remove(self)
		self.alive=False


	"""see the identity of an allies (in police team)"""
	def _penberPC(self):
		policeTeam=[]
		for player in playersList:
			if player.alive==True and player.team=="police" and player.charactere!="Penber":
				policeTeam.append(player)
		playerChoose=random.choice(policeTeam)
		if [playerChoose.pseudo, playerChoose. name] not in self.playersKnow:
			self.playersKnow.append([playerChoose.pseudo, playerChoose. name])

	"""add to the draw variable "num" draw cards"""
	def _draw(self, num):
		for i in range(num):
			drawCard=numpy.random.choice(cards, p=[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
			self.draw.append(drawCard)

	"""verifies the number of cards in the hand and their types (from the frontend) to
	prevent cheating"""
	def verif_cheat(self, newActions, newHand):
		if len(newActions)+len(newHand)!=self.hand+3:
			print("wrong cards' number, it's a cheater!\n")
			return False

		verifCards=self.draw+self.hand
		currentCards=newHand+newActions
		for card in currentCards:
			try:
				verifCards.remove(card)
			except:
				print("wrong cards' type, it's a cheater!\n")
				return False

		numPoints=0
		for action in actions:
			actionIndex=self.actions.index(action)
			numPoints+=actionPoints[actionIndex]
		if numPoints>INIT_POINTS:
			print("too many action points, it's a cheater!\n")
			return False
		
		self.drawSelec=newActions+newHand-self.hand
		self.actions=newActions
		self.hand=newHand
		return True

	def do_action(self):
		for action in actions and option in actionsOption:
			if action=="gun": self._gun(option)
			if action=="handcuffs": self._handcuffs(option)
			if action=="candies": self._candies()
			if action=="criminal": self._criminal(option)
			if action=="falseBadge": self._falseBadge()
			if action=="helmet": self._helmet()
			if action=="mandate": self._mandate(option)
			if action=="markup": self._markup(option)
			if action=="deathNote1": self._deathNote1(option[0], option[1])
			if action=="deathNote2": self._deathNote2(option)
			if action=="chest": self._chest(option)
			if action=="apple":self._apple(option)
			if action=="watariPC": self._watariPC()
			if action=="shinigamiEyes": self._shinigamiEyes(option)
			if action=="rope": self._rope()
			if action=="penberPC": self._penberPC()

	def after_actions(self):
		if self.handcuffs!=[]: pass
		if self.spy!=[]: pass


	#def card-action(self, action):
	#	pass


def find(value):
	for player in playersList:
		if player.pseudo==value:
			return player
	print("error, no player has this pseudo\n")
	exit()

def new_round():
	for player in playersList:
		player.actionPoints=INIT_POINTS
		player.actions=[]
		player.draw=[]
		player.handcuffs=""
		player.spy=[]
		player.drawSelec=[]
		player._draw(5)
		#self.spy=[]
		#roundInfos=[]
		#cibledCriminals=[]
		player.hide=False

		#envoie

	for place in places:
		place=True