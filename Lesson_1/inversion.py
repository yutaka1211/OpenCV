import math
import cv2
import numpy as np

file_src = 'picture/src.png'                        #ウィンドウ名を決定
file_dst = 'picture/inversion.png'

#2つ目の変数について,1:カラー(アルファチャンネルはむり),0:グレースケール,-1:オリジナル(アルファもいける)
img_src = cv2.imread(file_src, 1)                   #画像の読み込み

#変数(ウィンドウ名,ウィンドウの表示形式)
cv2.namedWindow('src')                              #ウィンドウの作成
cv2.namedWindow('inversion')

img_dst = cv2.flip(img_src, flipCode = 0)           #垂直反転

#変数(ウィンドウ名,表示する画像)
cv2.imshow('src', img_src)                          #入力画像の表示
cv2.imshow('inversion', img_dst)

#変数(保存時のウィンドウ名,保存する画像)
cv2.imwrite(file_dst, img_dst)                      #処理結果の保存

#変数(0:無限,0以上:指定ミリ秒表示)
cv2.waitKey(0)                                      #キーが押されるまで画像を表示したままにする
cv2.destroyAllWindows()                             #全てのウィンドウを破棄