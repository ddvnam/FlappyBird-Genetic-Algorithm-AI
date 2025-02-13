import pygame
from Background import Background
from Floor import Floor
from Pipe import Pipe
from Bird import Bird
from GA import GA

pygame.init()

class Game:
    def __init__(self):
        self.width = 288
        self.height = 512
        self.fps = 60
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flappy Bird")
        self.running = True
        
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 25)

        # Khoi tao cac doi tuong
        self.background = Background(0, 0, self.load_image("assets/background-day.png"))
        self.floor = Floor(0, 450, self.load_image("assets/base.png"))
        self.pipe = Pipe(300, 0, self.load_image("assets/pipe-green.png"))

        # Luu diem cao nhat
        self.best_survival_time = 0
        # Khoi tao GA va tao quan the
        self.birds = GA(50, 0.05) 
        self.birds.create_population()

        self.game_loop()

    def load_image(self, path):
        try:
            return pygame.image.load(path)
        except pygame.error as e:
            print(f"Error loading image: {path} - {e}")
            pygame.quit()
            exit()

    def game_loop(self):
        while self.running:
            self.event_handler()
            self.update()
            self.draw()
            self.set_fps()

    def draw(self):
        self.background.draw(self.win)
        self.pipe.draw(self.win)
        self.floor.draw(self.win)

        for bird in self.birds.population:
            if not bird.isDead:
                bird.draw(self.win)

        self.print_generation()
        self.print_best_fitness()
        self.draw_survival_time()

        pygame.display.update()

    def update(self):
        self.pipe.move()
        
        for bird in self.birds.population:
            if not bird.isDead:
                bird.drop()
                bird.update_survival_time()
                if self.is_collide(bird):
                    bird.isDead = True

        if all(bird.isDead for bird in self.birds.population):
            self.birds.evolve()
            self.restart()
        for bird in self.birds.population:
                self.best_survival_time = max(self.best_survival_time, bird.survival_time)
        
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  
                pygame.quit()
                exit()

        for bird in self.birds.population:
            if not bird.isDead:
                bird.think(self.pipe)  

    def set_fps(self):
        self.clock.tick(self.fps)

    def is_collide(self, bird):
        return (
            bird.rect.colliderect(self.pipe.top_rect) or 
            bird.rect.colliderect(self.pipe.bottom_rect) or 
            bird.rect.colliderect(self.floor.rect) or 
            bird.rect.top <= 0 or 
            bird.rect.bottom >= self.height
        )

        
    def draw_survival_time(self):
        self.print_text(f" Best Survival Time: {self.best_survival_time}", 10, 50)

    def restart(self):
        self.pipe.restart()
        for bird in self.birds.population:
            bird.restart()
    
    def print_text(self, text, x, y):
        text = self.font.render(text, True, (255, 255, 255))
        self.win.blit(text, (x, y))

    def print_generation(self):
        self.print_text(f"Generation: {self.birds.generation}", 10, 10)
    
    def print_best_fitness(self):
        self.print_text(f"Current Best Survival Time: {self.best_survival_time}", 10, 30)
if __name__ == "__main__":
    Game()
