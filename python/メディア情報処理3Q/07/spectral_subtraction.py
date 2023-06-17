# -*- coding: utf-8 -*-

# 使用するモジュールの宣言
from WaveFileIO import WaveFileReader
from WaveFileIO import WaveFileWriter
import numpy as np
import matplotlib.pyplot as plt

#
# スペクトルサブトラクション
#
if __name__ == '__main__':
    # 雑音の混ざった音声のwavファイル
    input_file_name = "./noisy_input.wav"

    # スペクトルサブトラクション処理後の波形を書き込むwavファイル
    output_file_name = "./output.wav"

    # 雑音スペクトルの推定に用いる時間
    noise_estimate_time = 1.0

    # 短時間分析を行う間隔
    frame_size = 512

    # --------------------
    # 入力データを読み込む
    # --------------------

    # wavファイルを読み込むクラスを呼び出す。
    input_reader = WaveFileReader()

    # 入力wavファイルを開く
    input_reader.open(input_file_name)

    # 入力wavファイルのサンプリング周波数、チャネル数、ファイルの長さを得る。
    sampling_rate = input_reader.sampling_rate
    num_channels = input_reader.num_channels
    num_samples = input_reader.length

    # wavファイルのデータを全て（全サンプル数の分だけ）読み込む。
    input_data = input_reader.read_data(num_samples)

    # wavファイルを閉じる
    input_reader.close()

    # --------------------
    # 雑音のパワースペクトルの推定
    # noise_estimate_time = 1.0 秒間のデータを使って
    # 雑音のパワースペクトルの平均を求める。
    # --------------------

    # 推定した雑音の振幅スペクトル
    noise_spectrum = np.zeros(frame_size)

    # 時刻
    n = 0
    # ループした回数
    count = 0
    # while True: は C言語における while(1){ と同じ。
    while True:
        # 処理する時刻が 雑音の推定に用いる時間を超える場合はループを抜ける
        if n >= noise_estimate_time * sampling_rate:
            break

        # n から n+frame_size までの短時間データ（フレーム）を切り出す
        frame = input_data[n: n+frame_size]

        # FFTを実施し、複素数のスペクトルを得る。
        spectrum = np.fft.fft(frame)

        # spectrumの絶対値を計算し、振幅スペクトルを得る。
        absolute_spectrum = np.abs(spectrum)

        # noise_spectrum に振幅スペクトルを足す。
        # (whileループを抜けた後で、足した回数で割ることで平均を計算する。)
        noise_spectrum += absolute_spectrum

        # ループした回数（noise_spectrumに足した回数）を１増やす。
        count += 1

        # 読み込んだ分 n を増やす
        n += frame_size

    # noise_spectrum をループした回数で割り、平均を算出する。
    noise_spectrum /= count

    # --------------------
    # スペクトルサブトラクションを実施する。
    # --------------------
    # 出力データのベクトルを用意しておく。
    # (以下では、要素数がnum_samples、全ての要素がゼロのベクトルを作成している。)
    output_data = np.zeros(num_samples)

    # 時刻
    n = 0
    # while True: は C言語における while(1){ と同じ。
    while True:
        # 読み込む範囲が入力のサイズを超える場合はループを抜ける
        if n + frame_size >= num_samples:
            break

        # n から n+frame_size までの短時間データ（フレーム）を切り出す
        frame = input_data[n: n + frame_size]

        # FFT(numpy.fft.fft)を実施し、複素数のスペクトルを得る。
        input_spectrum =

        # spectrumの絶対値を計算(numpy.abs)し、振幅スペクトルを得る。
        input_absolute_spectrum =

        # 入力の振幅スペクトルから、推定しておいた雑音の振幅スペクトル(noise_spectrum)を引く。
        output_absolute_spectrum =

        # 振幅が負になる周波数は、入力の振幅スペクトルの定数倍をかけた値を入れる。
        output_absolute_spectrum[output_absolute_spectrum < 0] = 1E-5

        # 推定した音声の複素スペクトルを計算する。
        output_spectrum =

        # 逆FFTを実施し、時間波形に戻す。
        output_frame = np.fft.ifft(output_spectrum).real

        # 出力波形用のベクトルに格納する。
        output_data[n: n + frame_size] = output_frame

        # 読み込んだ分 n を増やす
        n += frame_size

    # --------------------
    # 処理音声をwavファイルに書き込む
    # --------------------

    # wavファイルを書き込むクラスを呼び出す。
    # 引数1: サンプリング周波数
    # 引数2: チャネル数(1=モノラル, 2=ステレオ)
    output_writer = WaveFileWriter(sampling_rate, num_channels)

    # 書き込み先のファイルを開く。
    output_writer.open(output_file_name)

    # ファイルに処理後データを書き込む
    output_writer.write_data(output_data)

    # wavファイルを閉じる
    output_writer.close()

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
