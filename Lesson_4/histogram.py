import cv2
import numpy as np

img_src = cv2.imread('picture/moon_homo.png', 1)

img_gry = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

#ヒストグラム表示用のイメージを作成
img_histgram = np.zeros([100, 256]).astype('uint8')
rows, cols = img_histgram.shape

#次元ごとの度数分布サイズ
hdims = [256]

#各次元の度数分布の最小値と最大値
hranges = [0, 256]

#変数(入力画像,入力画像の種類(0:グレースケール,0~2:カラー画像でのrgb),マスク画像(画像中の全画素ならNone),ビンの数(全てなら[256]),計測したい画素値の範囲)
histgram = cv2.calcHist([img_gry], [0], None, hdims, hranges)                                           #histgramは[256][1]の配列で,各要素は対応する画素値を持つ画素の数を表す

#グレースケールから最も明るい画素と暗い画素の位置を出力する(min_val,max_val:画素の値、min_loc,max_loc:画素の位置)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(histgram)

for i in range(0, 255):

    v = histgram[i]

    #変数(線を引く画像,開始座標,終了座標,線の色,(線の太さ))
    cv2.line(img_histgram, (i, rows), (i, rows - int(rows * float(v / max_val))), (255, 255, 255))

cv2.imshow('dst', img_histgram)
cv2.waitKey(0)
cv2.destroyAllWindows()