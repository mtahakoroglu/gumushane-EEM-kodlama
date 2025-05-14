import serial
import pygame
import math
import sys

# Seri port ayarları (KENDİ PORTUNU YAZ)
ser = serial.Serial("COM12", 9600)  
ser.flushInput()

# Pygame ekran ayarları
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SONAR-RADAR")
clock = pygame.time.Clock()

# Renk tanımları
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)

# Radar merkezi ve yarıçap (yukarı kaydırıldı)
radar_radius = 250
center_x = screen_width // 2
center_y = radar_radius + 20  # üstte olacak şekilde

# Ölçümleri depolamak için
MAX_POINTS = 100  # İstediğin sayıya göre değiştirilebilir
points = []

def draw_radar_background():
    screen.fill(BLACK)
    # Yaylar
    for r in range(50, radar_radius + 1, 50):
        pygame.draw.circle(screen, DARK_GREEN, (center_x, center_y), r, 1)
    # Çizgiler
    for angle in range(0, 181, 30):
        x = center_x + radar_radius * math.cos(math.radians(angle))
        y = center_y - radar_radius * math.sin(math.radians(angle))
        pygame.draw.line(screen, DARK_GREEN, (center_x, center_y), (x, y), 1)

def draw_sweep(angle):
    x = center_x + radar_radius * math.cos(math.radians(angle))
    y = center_y - radar_radius * math.sin(math.radians(angle))
    pygame.draw.line(screen, GREEN, (center_x, center_y), (x, y), 2)

def draw_points():
    for ang, dist in points:
        if dist > radar_radius:
            continue
        x = center_x + dist * math.cos(math.radians(ang))
        y = center_y - dist * math.sin(math.radians(ang))
        pygame.draw.circle(screen, GREEN, (int(x), int(y)), 3)

# Ana döngü
running = True
try:
    while running:
        draw_radar_background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False

        try:
            if ser.in_waiting:
                data = ser.readline().decode('utf-8').strip()
                angle_str, distance_str = data.split(',')
                angle = int(angle_str)
                distance = int(distance_str)

                draw_sweep(angle)
                points.append((angle, distance))
                if len(points) > MAX_POINTS:
                    points.pop(0)

        except Exception as e:
            print("Veri okuma hatası:", e)

        draw_points()
        pygame.display.update()
        clock.tick(60)

except KeyboardInterrupt:
    print("Klavye ile durduruldu.")

finally:
    ser.close()
    pygame.quit()
    sys.exit()