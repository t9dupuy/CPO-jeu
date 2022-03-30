import pygame


class Player:

	def __init__(self):
		self.sprite = dict()
		self.load_images()
		self.pos_rel = [0,0]
		self.facing = 'front'
		self.walking = True
		self._count = 0

	def load_images(self):
		front = []
		front.append(pygame.image.load("resources/player/front_idle.png"))
		front.append(pygame.image.load("resources/player/front_walk1.png"))
		front.append(pygame.image.load("resources/player/front_walk2.png"))
		front.append(pygame.image.load("resources/cart/front.png"))

		self.sprite['front'] = front

		back = []
		back.append(pygame.image.load("resources/player/back_idle.png"))
		back.append(pygame.image.load("resources/player/back_walk1.png"))
		back.append(pygame.image.load("resources/player/back_walk2.png"))
		back.append(pygame.image.load("resources/cart/back.png"))

		self.sprite['back'] = back

		left = []
		left.append(pygame.image.load("resources/player/left_idle.png"))
		left.append(pygame.image.load("resources/player/left_walk1.png"))
		left.append(pygame.image.load("resources/player/left_walk2.png"))
		left.append(pygame.transform.scale(pygame.image.load("resources/cart/left.png"), (44,44)))

		self.sprite['left'] = left

		right = []
		right.append(pygame.image.load("resources/player/right_idle.png"))
		right.append(pygame.image.load("resources/player/right_walk1.png"))
		right.append(pygame.image.load("resources/player/right_walk2.png"))
		right.append(pygame.transform.scale(pygame.image.load("resources/cart/right.png"), (44,44)))

		self.sprite['right'] = right


	def move_up(self):
		self.facing = 'back'
		self.pos_rel[1] -= 10

	def move_down(self):
		self.facing = 'front'
		self.pos_rel[1] += 10

	def move_left(self):
		self.facing = 'left'
		self.pos_rel[0] -= 10

	def move_right(self):
		self.facing = 'right'
		self.pos_rel[0] += 10


	def draw(self, screen):
		
		#cart
		if(self.facing == 'back'):
			screen.blit(self.sprite[self.facing][3], [self.pos_rel[0]+6, self.pos_rel[1]-10])

		if(self.walking):
			self._count += 1
			if(self._count < 10):
				screen.blit(self.sprite[self.facing][1], self.pos_rel)
			elif(self._count < 20):
				screen.blit(self.sprite[self.facing][2], self.pos_rel)
				if(self._count == 19): self._count = 0
		else:
			screen.blit(self.sprite[self.facing][0], self.pos_rel)

		#cart
		if(self.facing == 'front'):
			screen.blit(self.sprite[self.facing][3], [self.pos_rel[0]+6, self.pos_rel[1]+70])
		if(self.facing == 'left'):
			screen.blit(self.sprite[self.facing][3], [self.pos_rel[0]-20, self.pos_rel[1]+65])
		if(self.facing == 'right'):
			screen.blit(self.sprite[self.facing][3], [self.pos_rel[0]+35, self.pos_rel[1]+65])
