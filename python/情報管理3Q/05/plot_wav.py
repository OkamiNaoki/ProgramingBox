# -*- coding: utf-8 -*-

# 使用するモジュールの宣言
from WaveFileIO import WaveFileReader
import numpy as np
import matplotlib.pyplot as plt

#
# wavファイルを読み込んで波形を表示する。
#
if __name__ == '__main__':
    # 読み込みたいwavファイルのパス
    input_file_name = "./input.wav"

    # --------------------
    # wavデータを読み込む
    # --------------------

    # wavファイルを読み込むクラスを呼び出す。
    wave_reader = WaveFileReader()

    # wavファイルを開く
    wave_reader.open(input_file_name)

    # wavファイルのサンプリング周波数を得る。
    sampling_rate = wave_reader.sampling_rate

    # wavファイルのチャネル数を得る。(チャネル数1=モノラル, チャネル数2=ステレオ)
    num_channels = wave_reader.num_channels

    # wavファイルの長さ(=1チャネル当たりのサンプル数)を得る。
    num_samples = wave_reader.length

    # wavファイルの情報を表示する。
    print( u"サンプリング周波数: %d Hz" % (sampling_rate) )
    print( u"チャネル数: %d" % (num_channels) )
    print( u"1チャネルあたりのサンプル数: %d" % (num_samples) )
    print( u"(音声の長さ = 1チャネルあたりのサンプル数 / サンプリング周波数 = %f 秒)" % (num_samples / sampling_rate) )

    # wavファイルのデータを全て（全サンプル数の分だけ）読み込む。
    wave_data = wave_reader.read_data(num_samples)

    # wavファイルを閉じる
    wave_reader.close()

    # --------------------
    # 波形をプロットする。
    # --------------------

    # グラフを描画するキャンバスを作成する。
    plt.figure()

    # グラフの x軸 (時間)を定義する。
    # numpy.arange(N) は、 中身が[0, 1, ..., N-1]のベクトルを作成する関数。
    # サンプル数をサンプリング周波数で割れば、時間に換算できる。
    time_data = np.arange(num_samples) / sampling_rate

    # グラフの y軸は読み込んだwave_dataの値である。
    # x軸とy軸の値をプロットする。
    plt.plot(time_data, wave_data)

    # グラフにタイトルを付ける
    # (デフォルトでは日本語が使えないので注意)
    plt.title("Waveform")

    # x軸とy軸にラベルを付ける
    # (デフォルトでは日本語が使えないので注意)
    plt.xlabel("Time [sec]")
    plt.ylabel("Amplitude")

    # プロット結果を表示する。
    plt.show()
