# -*- coding: utf-8 -*-

import cv2
from google.colab.patches import cv2_imshow

img = cv2.imread("틀 이미지 파일 경로") # 8컷 틀 파일 경로

# imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, imthres = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
# contour, hierachy = cv2.findContours(imthres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

"""
for item in contour:
  if len(item)==4:
    print(item.tolist())
locations = []
tempdict = {}

for item in contour:
  if len(item)==4:
    for pixel in item.tolist():
      tempdict[pixel[0][0]] = 0
      tempdict[pixel[0][1]] = 0
for item in contour:
  if len(item)==4:
    for pixel in item.tolist():
      tempdict[pixel[0][0]] += 1
      tempdict[pixel[0][1]] += 1
index_4 = sorted([k for k, v in tempdict.items() if v == 8])

pixels = [[], [], [], []]
for item in contour:
  if len(item)==4:
    for pixel in item.tolist():
      if pixel[0][0] == index_4[0]:
        pixels[0].append(pixel[0])
      elif pixel[0][0] == index_4[1]:
        pixels[1].append(pixel[0])
      elif pixel[0][0] == index_4[2]:
        pixels[2].append(pixel[0])
      else:
        pixels[3].append(pixel[0])
pixel_fixed = [sorted(pixels[0]), sorted(pixels[1]), sorted(pixels[2]), sorted(pixels[3])]
pixel_w = pixel_fixed[1][0][0] - pixel_fixed[0][0][0]
pixel_h = pixel_fixed[0][1][1] - pixel_fixed[0][0][1]

reg_points_1 = []
reg_points_4 = []
for i in range(len(pixel_fixed)):
  if i%2==0:
    for j in range(len(pixel_fixed[i])):
      if j%2==0:
        reg_points_1.append(pixel_fixed[i][j])
  else:
    for j in range(len(pixel_fixed[i])):
      if j%2!=0:
        reg_points_4.append(pixel_fixed[i][j])
"""

in1 = cv2.imread("이미지1") # 사진1
in2 = cv2.imread("이미지2") # 사진2
in3 = cv2.imread("이미지3") # 사진3
in4 = cv2.imread("이미지4") # 사진4

# 직사각형 각 점의 위치
reg_points_1 = [[46, 45],
 [46, 411],
 [46, 776],
 [46, 1141],
 [636, 45],
 [636, 411],
 [636, 776],
 [636, 1141]]
reg_points_4 = [[568, 392],
 [568, 758],
 [568, 1123],
 [568, 1488],
 [1158, 392],
 [1158, 758],
 [1158, 1123],
 [1158, 1488]]

 # 직사각형의 길이
pixel_w = 520
pixel_h = 345

def crop(img, pixel_w, pixel_h): #사진 자르는 함수, 들어갈 틀의 크기에 맞는 한도 내에서 최대한 크게 자름
  h,w,c = img.shape
  ratio = pixel_w/pixel_h
  if w >= ratio*h :
    out_img = img[:, round(w/2-((pixel_w/2)*(h/pixel_h))):round(w/2+((pixel_w/2)*(h/pixel_h)))]
  else:
    out_img = img[round(h/2-((pixel_h/2)*(w/pixel_w))):round(h/2+((pixel_h/2)*(w/pixel_w))), :]
  return out_img

def setimgs(img, pixel_w, pixel_h): #잘라진 사진을 8컷 틀에 맞게 사진 확대 및 축소하는 함수
  return cv2.resize(crop(img, pixel_w, pixel_h), dsize=(522, 347)) # 반올림 시 1픽셀 오차가 존재해 1픽셀은 덮어버리기 위해 상하좌우로 1픽셀씩 추가

# 사진 욱여넣는 함수
inputlist = [in1, in2, in3, in4, in1, in2, in3, in4]
for i in range(0, 4):
  img[reg_points_1[i][1]:reg_points_4[i][1], reg_points_1[i][0]:reg_points_4[i][0]] = setimgs(inputlist[i], pixel_w, pixel_h)
for i in range(4, 8):
  img[reg_points_1[i][1]:reg_points_4[i][1], reg_points_1[i][0]:reg_points_4[i][0]] = setimgs(inputlist[i], pixel_w, pixel_h)

from datetime import datetime
img = cv2.putText(img, str(datetime.now().strftime('%Y.%m.%d')), (213, 1730), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
img = cv2.putText(img, str(datetime.now().strftime('%Y.%m.%d')), (810, 1730), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)

cv2.imwrite('OutputImage.jpg', img)

