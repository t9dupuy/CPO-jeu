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
		front.append(pygame.image.load("resources/player/p1/idle/front.png"))
		front.append(pygame.image.load("resources/player/p1/push/front1.png"))
		front.append(pygame.image.load("resources/player/p1/push/front2.png"))
		front.append(pygame.image.load("resources/player/p1/push/front3.png"))
		front.append(pygame.image.load("resources/player/p1/push/front4.png"))
		front.append(pygame.image.load("resources/player/p1/push/front5.png"))
		front.append(pygame.image.load("resources/player/p1/push/front6.png"))

		for i, image in enumerate(front):
			front[i] = pygame.transform.scale(image, (64,128))

		front.append(pygame.transform.scale(pygame.image.load("resources/cart/front.png"), (128,128)))

		self.sprite['front'] = front

		back = []
		back.append(pygame.image.load("resources/player/p1/idle/back.png"))
		back.append(pygame.image.load("resources/player/p1/push/back1.png"))
		back.append(pygame.image.load("resources/player/p1/push/back2.png"))
		back.append(pygame.image.load("resources/player/p1/push/back3.png"))
		back.append(pygame.image.load("resources/player/p1/push/back4.png"))
		back.append(pygame.image.load("resources/player/p1/push/back5.png"))
		back.append(pygame.image.load("resources/player/p1/push/back6.png"))

		for i, image in enumerate(back):
			back[i] = pygame.transform.scale(image, (64,128))

		back.append(pygame.transform.scale(pygame.image.load("resources/cart/back.png"), (128,128)))

		self.sprite['back'] = back

		left = []
		left.append(pygame.image.load("resources/player/p1/idle/left.png"))
		left.append(pygame.image.load("resources/player/p1/push/left1.png"))
		left.append(pygame.image.load("resources/player/p1/push/left2.png"))
		left.append(pygame.image.load("resources/player/p1/push/left3.png"))
		left.append(pygame.image.load("resources/player/p1/push/left4.png"))
		left.append(pygame.image.load("resources/player/p1/push/left5.png"))
		left.append(pygame.image.load("resources/player/p1/push/left6.png"))

		for i, image in enumerate(left):
			left[i] = pygame.transform.scale(image, (64,128))

		left.append(pygame.transform.scale(pygame.image.load("resources/cart/left.png"), (128,128)))

		self.sprite['left'] = left

		right = []
		right.append(pygame.image.load("resources/player/p1/idle/right.png"))
		right.append(pygame.image.load("resources/player/p1/push/right1.png"))
		right.append(pygame.image.load("resources/player/p1/push/right2.png"))
		right.append(pygame.image.load("resources/player/p1/push/right3.png"))
		right.append(pygame.image.load("resources/player/p1/push/right4.png"))
		right.append(pygame.image.load("resources/player/p1/push/right5.png"))
		right.append(pygame.image.load("resources/player/p1/push/right6.png"))
		for i, image in enumerate(right):
			right[i] = pygame.transform.scale(image, (64,128))

		right.append(pygame.transform.scale(pygame.image.load("resources/cart/right.png"), (128,128)))

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

		#when player is facing back
		if(self.facing == 'back'):
			screen.blit(self.sprite['back'][7], (self.pos_rel[0] - 2, self.pos_rel[1] - 20))

		if(self.walking):
			frame_per_image = 6
			self._count += 1
			self._count %= (6 * frame_per_image)
			screen.blit(self.sprite[self.facing][1 + int(self._count/frame_per_image)], self.pos_rel)
		else:
			screen.blit(self.sprite[self.facing][0], self.pos_rel)

		#when player is facing front
		if(self.facing == 'front'):
			screen.blit(self.sprite['front'][7], (self.pos_rel[0] - 7, self.pos_rel[1] + 70))
		#when player is facing left
		if(self.facing == 'left'):
			screen.blit(self.sprite['left'][7], (self.pos_rel[0] - 83, self.pos_rel[1] + 20))
		#when player is facing right
		if(self.facing == 'right'):
			screen.blit(self.sprite['right'][7], (self.pos_rel[0] + 58, self.pos_rel[1] + 20))

