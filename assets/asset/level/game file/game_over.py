import pygame
import sys
from config import *
from main_menu import StartScreen

class GameOver:
    def __init__(self,screen):
        self.screen =screen
        self.clock =pygame.time.Clock()
        self.font_Big =pygame.font.Font(None,80)
        self.font_small =pygame.font.Font(None,40)
        

    def run(self,final_score):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
    

            #Baground
            self.screen.fill((0,0,0))
            # Text
            title = self.font_Big.render('GAME OVER', True,(255,0,0))
            score_text = self.font_small.render(f"Your Score: {final_score}", True, (255, 255, 255))
            continue_text = self.font_small.render("click anywhere to menu", True, (200, 200, 200))
            # Draw centered
            self.screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))
            self.screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 280))
            self.screen.blit(continue_text, (150, 350))


            pygame.display.flip()
            self.clock.tick(60)
