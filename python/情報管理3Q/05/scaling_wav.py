# -*- coding: utf-8 -*-

# 使用するモジュールの宣言
from WaveFileIO import WaveFileReader
from WaveFileIO import WaveFileWriter
import numpy as np
import matplotlib.pyplot as plt

#
# wavファイルを読み込み、波形の大きさ（音量）を N 倍して別のwavファイルに書き込む
#
if __name__ == '__main__':
    # 読み込みたいwavファイルのパス
    input_file_name = "./input.wav"

    # 処理後の波形を書き込むwavファイルのパス
    output_file_name = "./output.wav"

    # 音量を変える比率
    scaling_factor = 2.0

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

    # wavファイルのデータを全て（全サンプル数の分だけ）読み込む。
    input_data = wave_reader.read_data(num_samples)

    # wavファイルを閉じる
    wave_reader.close()

    # --------------------
    # 波形を処理する
    # 入力波形の音量をN倍
    # --------------------

    # 入力データ各要素の値を、 scaling_factor倍する。
    # output_data(ベクトル) = input_data(ベクトル) * scaling_factor(スカラー)
    output_data = input_data * scaling_factor

    # --------------------
    # 処理音声をwavファイルに書き込む
    # --------------------

    # wavファイルを書き込むクラスを呼び出す。
    # 引数1: サンプリング周波数
    # 引数2: チャネル数(1=モノラル, 2=ステレオ)
    wave_writer = WaveFileWriter(sampling_rate, num_channels)

    # 書き込み先のファイルを開く。
    wave_writer.open(output_file_name)

    # ファイルに処理後データを書き込む
    wave_writer.write_data(output_data)

    # wavファイルを閉じる
    wave_writer.close()

    # --------------------
    # 波形をプロットする。
    # --------------------

    # グラフを描画するキャンバスを作成する。
    plt.figure()

    # グラフの x軸 (時間)を定義する。
    # numpy.arange(N) は、 中身が[0, 1, ..., N-1]のベクトルを作成する関数。
    # サンプル数をサンプリング周波数で割れば、時間に換算できる。
    time_data = np.arange(num_samples) / sampling_rate

    # キャンバスを2個に分割し、入力データを描画する領域を作成する。
    plt.subplot(2, 1, 1)

    # 入力データをプロットする。
    plt.plot(time_data, input_data)

    # グラフにタイトルを付ける
    # (デフォルトでは日本語が使えないので注意)
    plt.title("Input")

    # y軸にラベルを付ける
    # (デフォルトでは日本語が使えないので注意)
    plt.ylabel("Amplitude")

    # 2個に分割されたキャンバスに、出力データを描画する領域を作成する。
    plt.subplot(2, 1, 2)

    # 出力データをプロットする。
    plt.plot(time_data, output_data)

    # グラフにタイトルを付ける
    # (デフォルトでは日本語が使えないので注意)
    plt.title("output")

    # 出力データ用グラフにもx軸, y軸ラベルを付ける。
    # (デフォルトでは日本語が使えないので注意)
    plt.xlabel("Time [sec]")
    plt.ylabel("Amplitude")

    # プロット結果を表示する。
    plt.show()
