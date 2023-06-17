# -*- coding: utf-8 -*-

# 使用するモジュールの宣言
from WaveFileIO import WaveFileReader
from WaveFileIO import WaveFileWriter
import numpy as np
import matplotlib.pyplot as plt

#
# wavファイルにインパルス応答を畳み込んで別のwavファイルに書き込む
#
if __name__ == '__main__':
    # 読み込みたいwavファイルのパス
    input_file_name = "./input.wav"

    # 処理後の波形を書き込むwavファイルのパス
    output_file_name = "./output.wav"

    # インパルス応答のファイル
    rir_file_name = "./rir_310.wav"

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
    # インパルス応答(rir: Room Impulse Response)データを読み込む
    # --------------------

    # wavファイルを読み込むクラスを呼び出す。
    rir_reader = WaveFileReader()

    # 入力wavファイルを開く
    rir_reader.open(rir_file_name)

    # インパルス応答の長さを得る。
    rir_num_samples = rir_reader.length

    # wavファイルのデータを全て（全サンプル数の分だけ）読み込む。
    rir_data = rir_reader.read_data(rir_num_samples)

    # インパルス応答データのみ、最大値が1になるように正規化する。
    rir_data = 1.0 * rir_data / 32768

    # wavファイルを閉じる
    rir_reader.close()

    # --------------------
    # 波形を処理する
    # インパルス応答の畳み込み
    # --------------------

    # 出力データのベクトルを用意しておく。
    # (以下では、要素数がnum_samples、全ての要素がゼロのベクトルを作成している。)
    output_data = np.zeros(num_samples)

    print(u"処理中...")
    # "for n in range(N):" は、C言語だと "for( n=0; n <= N-1; n++ ){" に相当する。
    for n in range(num_samples):
        if n-rir_num_samples+1 < 0:
            # このサンプルでは簡単のため、 n-rir_num_samples+1 < 0の場合は畳み込みを行わないことにする。
            # (ベクトルのインデクスが負になってしまうため。)
            output_data[n] = input_data[n]
        else:
            #
            # インパルス応答との畳み込みを行う。
            #
            # input_data[n-rir_num_samples+1] から input_data[n+1] までを取り出して、逆順に並べ替える。
            # (要素の後ろに +1 を加えているのは、例えば x[1:4]とすると、1～3番目が取り出され、4番目が取り出されないため)
            input_rev = input_data[n-rir_num_samples+1:n+1]
            input_rev = np.flip(input_rev, 0)
            # rir_data　と input_rev の内積を計算する。内積はnumpy.dotを使う。
            output_data[n] = np.dot(rir_data, input_rev)
    print(u"処理完了")

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

    #
    # インパルス応答を別のキャンバスで表示する。
    #
    plt.figure()

    time_data = np.arange(rir_num_samples) / sampling_rate
    plt.plot(time_data, rir_data)
    plt.title("Impulse response")
    plt.xlabel("Time [sec]")

    # プロット結果を表示する。
    plt.show()
