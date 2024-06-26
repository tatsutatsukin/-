# -*- coding: utf-8 -*-
"""Listing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wftb3GWlfO3FeeWlWS12JX-jVkW8i53Y

受け取り：なし

出力：名前が格納された配列、中身が格納された配列(return_list関数)


説明：

テキストファイルを各配列の名前と中身をリスト型のする

(受け入れ書式はFASTA形式のみ)

インスタンスのnamelistには配列の名前が格納されており、ncllistには配列の中身が格納されている
"""

from os import name
class Listing:

  def __init__(self, path):
    #path = '/content/drive/MyDrive/卒業研究/塩基配列サンプル/ex1_LSU_rRNA.txt'
    self.namelist = []
    self.ncllist = []
    file_line_num = 0


    with open(path) as f:
      for s_line in f:
        file_line_num += 1


    with open(path) as f:
      n = 0
      ncl = ''
      count = 0

      for s_line in f:
        count += 1
        if s_line[0] == '>':
          if n != 0:
            self.ncllist.append(ncl)
            ncl = ''
          self.namelist.append(s_line[:-1])
          n += 1
        else:
          ncl += ncl.join(s_line.splitlines())
          if file_line_num == count:
            self.ncllist.append(ncl)

  def return_list(self):
    return self.namelist, self.ncllist