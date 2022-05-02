import imp
import pygame
from tiles import Tile
from settings import tile_size
from player import Player

class Level: 
    def __init__(self, level_data, surface):

        #level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
    
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index,col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == 'X':
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                if col == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    def scroll_x(self):     
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < 200 and direction_x < 0: 
            self.world_shift = 8
            player.speed = 0   
        elif player_x > 1000 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else: 
            self.world_shift = 0
            player.speed = 8

    def run(self):
        #draws level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        #draws player
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()