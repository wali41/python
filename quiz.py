import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1000, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 149, 237)
RED = (220, 20, 60)
GREEN = (34, 139, 34)

# Fonts
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 48)

# Button class
class Button:
    def __init__(self, text, x, y, width, height, color, action):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


# Quiz data (question, options, correct answer)
quiz = [
    ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], "Mars"),
    ("Who connquered Palestine'?", ["Suleiman The Magnificent", "Sultan Mehmed", "Osman Ghazi", "Caliph Umar Bin Abdul Aziz"], "Salahuddin Ayyubi"),
]

# Game state
current_question = 0
score = 0
selected_answer = ""
result = ""

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.is_clicked(event.pos):
                    selected_answer = button.action
                    if selected_answer == correct_answer:
                        result = "Correct!"
                        score += 1
                    else:
                        result = f"Wrong! Correct: {correct_answer}"

    # Display current question
    if current_question < len(quiz):
        question, options, correct_answer = quiz[current_question]

        question_text = large_font.render(question, True, BLACK)
        screen.blit(question_text, (50, 50))

        # Buttons for answers
        button_width, button_height = 200, 50
        spacing = 20
        buttons = []
        for i, option in enumerate(options):
            btn = Button(option, 100, 150 + i * (button_height + spacing), button_width, button_height, BLUE, option)
            buttons.append(btn)
            btn.draw(screen)

        # Show result
        if result:
            result_text = font.render(result, True, RED if "Wrong" in result else GREEN)
            screen.blit(result_text, (100, 400))

            # Move to next question after short delay
            pygame.display.flip()
            pygame.time.wait(1500)
            current_question += 1
            result = ""
            selected_answer = ""

    else:
        # Quiz finished
        final_text = large_font.render(f"Quiz Over! Score: {score}/{len(quiz)}", True, BLACK)
        screen.blit(final_text, (150, 200))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
