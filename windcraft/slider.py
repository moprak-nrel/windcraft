import pygame
import windcraft.colors as colors
import windcraft.fonts as fonts


class Slider:
    def __init__(self, x, y, width, height, min_val, max_val, initial_val, label=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_val = min_val
        self.max_val = max_val
        self.value = int(max(min_val, min(max_val, initial_val)))
        self.label = label
        self.handle_radius = height // 2 + 2
        self.dragging = False
        self.colors = colors.Colors()
        self.fonts = fonts.Fonts()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            hx = int(
                self.x
                + (self.value - self.min_val)
                / (self.max_val - self.min_val)
                * self.width
            )
            hy = self.y + self.height // 2
            if (mx - hx) ** 2 + (my - hy) ** 2 <= self.handle_radius**2:
                self.dragging = True
            elif (
                self.x <= mx <= self.x + self.width
                and self.y <= my <= self.y + self.height
            ):
                rel = (mx - self.x) / self.width
                rel = max(0, min(1, rel))
                self.value = int(self.min_val + rel * (self.max_val - self.min_val))
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            mx, _ = pygame.mouse.get_pos()
            rel = (mx - self.x) / self.width
            rel = max(0, min(1, rel))
            self.value = int(self.min_val + rel * (self.max_val - self.min_val))

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.colors.gray,
            (self.x, self.y, self.width, self.height),
            border_radius=10,
        )
        hx = int(
            self.x
            + (self.value - self.min_val) / (self.max_val - self.min_val) * self.width
        )
        hy = self.y + self.height // 2
        pygame.draw.circle(screen, self.colors.purple, (hx, hy), self.handle_radius)
        text = self.fonts.types["medium"].render(
            f"{self.label}{self.value}", True, self.colors.black
        )
        screen.blit(text, (self.x + 5, self.y - self.height))
