import pygame
import os
from win32api import GetSystemMetrics
import time
import random
from math import pi
import sys

import cv2
import mediapipe as mp

# mp_face_detection = mp.solutions.face_detection
# mp_drawing = mp.solutions.drawing_utils
# cap = cv2.VideoCapture(0)

width = 1536
height = 864
pygame.init()
clock=pygame.time.Clock()
a=pygame.display.set_mode((width,height))

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)
PURPLE = (128,0,128)

x1 = GetSystemMetrics(0)
y1 = random.randint(100,300)

x2 = GetSystemMetrics(0)
y2 = random.randint(100,300)

x3 = GetSystemMetrics(0)
y3 = random.randint(100,300)

x4 = GetSystemMetrics(0)
y4 = random.randint(100,300)

x5 = GetSystemMetrics(0)
y5 = random.randint(100,300)

x6 = GetSystemMetrics(0)
y6 = random.randint(100,300)

pygame.display.set_caption("Thienthanmicle")
x=20
y=210
diem=0
c = True
e=False
biendem=0
# with mp_face_detection.FaceDetection(
#  model_selection=0,min_detection_confidence=0.5) as face_detection:
#  while c:
#     success, image = cap.read()
#     if not success:
#         print("Ignoring empty camera frame !!!")
#         continue
#     image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
#     image.flags.writeable = False
#     results = face_detection.process(image)

#         # Draw the face detection annotations on the image.
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     if results.detections:
#         for detection in results.detections:
#             mp_drawing.draw_detection(image, detection)
#     cv2.imshow('MediaPipe Face Detection', image)
#     if cv2.waitKey(5) & 0xFF == 27:
#         break
while c:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            c = False

    a.fill(BLACK)

    c=pygame.draw.line(a,RED,[0,100],[GetSystemMetrics(0),100],2)
    c1=pygame.draw.line(a,RED,[0,350],[GetSystemMetrics(0),350],2)
    box = (x,y,30,30)
    box1 = (x1,y1,25,50)
    box2 = (x2,y2,25,50)
    box3 = (x3,y3,25,50)
    box4 = (x4,y4,25,50)
    box5 = (x5,y5,25,50)
    box6 = (x6,y6,25,50)
    n1=pygame.draw.rect(a,GREEN,box1,2)
    n2=pygame.draw.rect(a,GREEN,box2,2)
    n3=pygame.draw.rect(a,GREEN,box3,2)
    n4=pygame.draw.rect(a,GREEN,box4,2)
    n5=pygame.draw.rect(a,GREEN,box5,2)
    n6=pygame.draw.rect(a,GREEN,box6,2)

    n=pygame.draw.rect(a,BLUE,box)

    b = pygame.key.get_pressed()
    if b[pygame.K_SPACE]: 
        y -= 10
        e=True
    if b[pygame.K_q]: c = False

    if biendem>50:
        x2-=5
    if biendem>100:
        x3-=5
    if biendem>150:
        x4-=5
    if biendem>200:
        x5-=5
    if biendem>250:
        x6-=5

    if n.colliderect(n1):
        c=False
    if n.colliderect(n2):
        c=False
    if n.colliderect(n3):
        c=False
    if n.colliderect(n4):
        c=False
    if n.colliderect(n5):
        c=False
    if n.colliderect(n6):
        c=False

    if (x>200):
        x=200
    if (y<100):
        c=False
    if y>=320:
        c=False
    if x1<0:
        x1=GetSystemMetrics(0)
        y1=random.randint(100,300)
    if x2<0:
        x2=GetSystemMetrics(0)
        y2=random.randint(100,300)
    if x3<0:
        x3=GetSystemMetrics(0)
        y3=random.randint(100,300)
    if x4<0:
        x4=GetSystemMetrics(0)
        y4=random.randint(100,300)
    if x5<0:
        x5=GetSystemMetrics(0)
        y5=random.randint(100,300)
    if x6<0:
        x6=GetSystemMetrics(0)
        y6=random.randint(100,300)

    font = pygame.font.SysFont("comicsansms", 30)
    text = font.render("TIME: " + str(diem), True, (0, 128, 0))
    a.blit(text,((1536/2) - text.get_width() // 2, 50))

    x+=2
    if e==True:
        y+=3
        x1-=5
        biendem+=1
        diem+=1
    pygame.display.flip()
    clock.tick(60)

# c1=True
# if c==False:
#     while c1:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True

#         a.fill(BLACK)
#         font = pygame.font.SysFont("timesnewroman", 100)
#         text = font.render("Lol ngu, TIME: " + str(diem), True, (0, 128, 0))
#         text1 = font.render("Nhấn q để thấy mặt lol", True, (0, 128, 0))
#         a.blit(text,((1536/2) - text.get_width() // 2, 200))
#         a.blit(text1,((1536/2) - text1.get_width() // 2, 300))
#         b = pygame.key.get_pressed()
#         if b[pygame.K_q]: c1 = False
#         pygame.display.flip()
#         clock.tick(60)

# mp_face_detection = mp.solutions.face_detection
# mp_drawing = mp.solutions.drawing_utils
# cap = cv2.VideoCapture(0)
# with mp_face_detection.FaceDetection(
#     model_selection=0,min_detection_confidence=0.5) as face_detection:
#     while cap.isOpened():
#         success, image = cap.read()
#         if not success:
#             print("Ignoring empty camera frame !!!")
#             continue
#         image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
#         image.flags.writeable = False
#         results = face_detection.process(image)

#         image.flags.writeable = True
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#         if results.detections:
#             for detection in results.detections:
#                 mp_drawing.draw_detection(image, detection)
#         cv2.imshow('MediaPipe Face Detection', image)
#         if cv2.waitKey(5) & 0xFF == 27:
#             break
# cap.release()

