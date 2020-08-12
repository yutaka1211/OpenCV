import cv2
import numpy as np
import matplotlib.pyplot as plt

img_src = cv2.imread('picture/cell.png', 1)
img_chs = cv2.split(img_src)                    #この時,BGRの順でimg_chsに格納される

binimg = (img_chs[2]>100)                       #条件を満たすピクセルのみが1になった2値画像が得られる
binimg = binimg.astype(np.uint8)                #uint8に型変換
#変数(入力画像(8bit,シングルチャネル),距離関数(整数か小数),カーネル)
distmap = cv2.distanceTransform(binimg, 1, 3)   #輪郭から遠い部分で、高い値をもつ画像が得られる

out = distmap * 0                               #マップを初期化
ksize = 10

#周辺の20*20ピクセルの領域中で最も値が大きい場所を1とする
for x in range(ksize, distmap.shape[0]-ksize):
    for y in range(ksize, distmap.shape[1]-ksize):
        if distmap[x, y] > 0 and distmap[x, y] == np.max(distmap[x-ksize:x+ksize, y-ksize:y+ksize]):
            out[x, y]=1

out = cv2.dilate(out, (3,3))                    #3*3のカーネルによって膨張させる->近くに同じ極大値をもつピクセルがあれば、1つの塊にする

#変数(入力画像,抽出モード,近似手法)
contours, _ = cv2.findContours(out.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#contoursは検出された前輪郭をlistとして出力,list内の各輪郭は輪郭上の点の(x,y)座標をnumpyのarrayとして保存

arr = []                                        #[]で配列を作ると早い
for i in contours:
    x_ = 0
    y_ = 0
    for j in i:
        x_ += j[0][0]
        y_ += j[0][1]
    arr.append([x_/len(i), y_/len(i)])          #arrの末尾に要素を追加
arr = np.array(arr)                             #リストをnumpy配列に変換

plt.imshow(out)
plt.colorbar()
plt.show()

print(len(arr))
print(arr)

#dilateはカーネル内に画素値が1の画素が1つでもあれば、出力画像の注目画素の画素値を1にする
#cv2.CHAIN_APPROX_SIMPLE:findcontoursの近似手法