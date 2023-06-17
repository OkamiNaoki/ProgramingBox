# -*- coding: utf-8 -*-

# 使用するモジュールの宣言
from WaveFileIO import WaveFileReader
from WaveFileIO import WaveFileWriter
import numpy as np
import matplotlib.pyplot as plt

#
# 音響エコーキャンセリング
#
if __name__ == '__main__':
    # スピーカ信号が混ざった音声のwavファイル
    input_file_name = "./echo_mixed_input.wav"

    # 参照信号（スピーカから出力させる源信号）のwavファイル
    reference_file_name = "./reference.wav"

    # エコーキャンセリング処理後の波形を書き込むwavファイル
    output_file_name = "./output.wav"

    # 推定するインパルス応答の長さ (スライド中の K に相当)
    rir_length = 1024

    # 推定インパルス応答の修正率
    myu = 1.0

    # インパルス応答の修正を止める時刻
    stop_update_time = 10.0

    # --------------------
    # 入力データを読み込む
    # input_data は　スライド中の z に相当
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
    # 参照信号(スピーカから出力する源信号)データを読み込む
    # reference_data は　スライド中の x に相当
    # --------------------

    # wavファイルを読み込むクラスを呼び出す。
    reference_reader = WaveFileReader()

    # wavファイルを開く
    reference_reader.open(reference_file_name)

    # 参照信号の長さを得る。
    reference_num_samples = reference_reader.length

    # wavファイルのデータを全て（全サンプル数の分だけ）読み込む。
    reference_data = reference_reader.read_data(reference_num_samples)

    # wavファイルを閉じる
    reference_reader.close()

    # --------------------
    # 波形を処理する
    # 音響エコーキャンセリング
    # --------------------

    # 出力データのベクトルを用意しておく。
    # (以下では、要素数がnum_samples、全ての要素がゼロのベクトルを作成している。)
    output_data = np.zeros(num_samples)

    # 推定したインパルス応答の格納先を用意しておく。(長さはrir_length)
    # estimated_rir はスライド中の hハット に相当。
    estimated_rir = np.zeros(rir_length)

    print(u"処理中...")
    # "for n in range(N):" は、C言語だと "for( n=0; n <= N-1; n++ ){" に相当する。
    for n in range(num_samples):
        if n-rir_length+1 < 0:
            # このサンプルでは簡単のため、 n-rir_length+1 < 0 の場合は処理を行わないことにする。
            # (ベクトルのインデクスが負になってしまうため。)
            output_data[n] = input_data[n]
        else:
            #
            # NLMSアルゴリズムによるエコーキャンセリングを実行する。
            #

            #
            # 現在の推定インパルス応答と参照信号の畳み込みを行い、
            # スピーカの収録信号（エコー）を推定する。
            #
            # 参照信号 reference_data[n-rir_length+1] から reference_data[n+1] までを取り出す。
            reference_part = reference_data[n-rir_length+1:n+1]
            # reference_part を逆順に並び替える。
            reference_rev =np.flip(reference_part,0)
            # estimated_rir　と reference_rev の内積を計算することで、畳み込みが行われ、スピーカ収録音（エコー）の推定値が得られる。
            estimated_echo =np.dot(estimated_rir,reference_rev)

            #
            # 入力信号からエコー信号を引くことで、エコーを除去する。
            # このとき、減算結果がエコーの消し残り(error)である。
            #
            # 入力信号からエコーの推定値を引く。
            output_data[n] =input_data[n]-estimated_echo
            # 上記output_data[n]は消し残りに相当する。
            error =output_data[n]

            #
            # 正規化項(参照信号の二乗和)を求める。
            # このとき、ゼロ除算による計算エラーを防ぐため、小さい値(flooring係数=1E-10)を足しておくこと。
            #
            norm =np.sum(reference_rev**2)+1E-10

            #
            # インパルス応答の更新を止める時間(stop_update_time * sampling_rate)に達していない場合は、
            # インパルス応答の推定値を更新する。
            #
            if n < stop_update_time * sampling_rate:
                # NLMS アルゴリズムの更新式に従って、 estimated_rir を更新する。
                estimated_rir =estimated_rir+(myu/norm*error*reference_rev)

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
    # 推定したインパルス応答を別のキャンバスで表示する。
    #
    plt.figure()

    time_data = np.arange(rir_length) / sampling_rate
    plt.plot(time_data, estimated_rir)
    plt.title("Estimated room impulse response")
    plt.xlabel("Time [sec]")

    # プロット結果を表示する。
    plt.show()