# -*- coding: utf-8 -*-

import sys
import numpy as np


# Wavファイル読み込みクラス
class WaveFileReader:
    def __init__(self):
        self.file = None
        self.sampling_rate = 0
        self.num_channels = 0
        self.byte_sample = 0
        self.length = 0
        self.position_of_data = 0
        self.file_size = 0

    # デストラクタ
    def __del__(self):
        # ファイルを閉じる。
        self.close()

    # ファイルを開く
    def open(self, filename):
        # 現在別のファイルを開いている場合は閉じる。
        self.close()
        self.file = open(filename, 'rb')

        # ヘッダを読み込む
        # 'RIFFヘッダ
        tmp = self.file.read(4)
        if tmp != b'RIFF':
            sys.stderr.write('WaveFileReader.open: File format error\n')
            self.close()
            return
        # 'WAVE'ヘッダ
        self.file.seek(8)
        tmp = self.file.read(4)
        if tmp != b'WAVE':
            sys.stderr.write('WaveFileReader.open: File format error\n')
            self.close()
            return
        # 'fmt'チャンク
        tmp = self.file.read(4)
        if tmp != b'fmt ':
            sys.stderr.write('WaveFileReader.open: File format error\n')
            self.close()
            return
        # fmtチャンクの長さ
        fmt_chunk_size = int.from_bytes(self.file.read(4), 'little')
        # 音声フォーマット。リニアPCM(=1)のみ受け付ける。
        tmp = int.from_bytes(self.file.read(2), 'little')
        if tmp != 1:
            sys.stderr.write('WaveFileReader.open: The file format is not linear PCM. This program can read linear PCM only.\n')
            self.close()
            return
        # チャネル数
        self.num_channels = int.from_bytes(self.file.read(2), 'little')
        # サンプリング周波数
        self.sampling_rate = int.from_bytes(self.file.read(4), 'little')
        # 1秒あたりのサイズおよびブロックサイズの読み込みはスキップ
        self.file.seek(6, 1)
        # ビット/サンプル。16bit(=2byte)のみ受け付ける
        self.byte_sample = int.from_bytes(self.file.read(2), 'little') / 8
        if self.byte_sample != 2:
            sys.stderr.write('WaveFileReader.open: The bit sample is %d. This program can read 16bit PCM only.\n' % (self.byte_sample*8))
        # fmtチャンクの残り部分の読み込みをスキップ
        self.file.seek(fmt_chunk_size - 16, 1)
        # dataチャンクを読み込むまで、サブチャンクをスキップする。
        while True:
            # チャンク識別子
            tmp = self.file.read(4)
            # dataチャンクに到達したらループを抜ける
            if tmp == b'data':
                break
            # チャンクサイズ
            chunk_size = int.from_bytes(self.file.read(4), 'little')
            self.file.seek(chunk_size, 1)
        # データサイズ(波形長*チャネル数*バイト数)を得る。
        data_size = int.from_bytes(self.file.read(4), 'little')
        self.length = int(data_size / (self.byte_sample * self.num_channels))
        # データ開始位置を記憶
        self.position_of_data = self.file.tell()
        # ファイルサイズを記憶
        self.file_size = self.position_of_data + data_size

    # ファイルを閉じる
    def close(self):
        # ファイルが開かれていれば閉じる
        if self.file is not None:
            self.file.close()
            self.file = None

    # 指定した時刻に移動する。
    def move_time(self, position):
        if position < 0 or position >= self.length:
            sys.stderr.write('[WaveFileReader.seek] invalid argument\n')
            return
        position_byte = int(position * self.num_channels * self.byte_sample)
        self.file.seek(position_byte+self.position_of_data, 0)

    # データ読み込み
    def read_data(self, size):
        read_size = int(size * self.num_channels * self.byte_sample)
        read_data = np.frombuffer(self.file.read(read_size), 'int16')
        return read_data.astype(np.float)


# Waveファイル書き込みクラス
class WaveFileWriter:
    def __init__(self, sampling_rate, num_channels=1):
        self.file = None
        self.sampling_rate = int(sampling_rate)
        self.num_channels = int(num_channels)

    # デストラクタ
    def __del__(self):
        # ファイルを閉じる。
        self.close()

    # ファイルを開く
    def open(self, filename):
        # 現在別のファイルを開いている場合は閉じる。
        self.close()
        self.file = open(filename, 'wb')

        # ヘッダを書き込む
        # サイズは未知なので、ダミーサイズを書き込む
        dummy_size = 0
        dummy_size_16bit = dummy_size.to_bytes(4, 'little')
        # 'RIFF'ヘッダ
        self.file.write(b'RIFF')
        # ダミーのサイズ書き込み
        self.file.write(dummy_size_16bit)
        # 'WAVE'ヘッダ
        self.file.write(b'WAVE')
        # 'fmt'チャンク
        self.file.write(b'fmt ')
        # fmtチャンクの長さ
        fmt_chunk_size = 16
        self.file.write(fmt_chunk_size.to_bytes(4, 'little'))
        # 音声フォーマット
        format = 1
        self.file.write(format.to_bytes(2, 'little'))
        # チャネル数
        self.file.write(self.num_channels.to_bytes(2, 'little'))
        # サンプリング周波数
        self.file.write(self.sampling_rate.to_bytes(4, 'little'))
        # 1秒あたりのデータサイズ
        size_per_sec = int(self.sampling_rate * self.num_channels * 2)
        self.file.write(size_per_sec.to_bytes(4, 'little'))
        # ブロックサイズ
        block_size = int(self.num_channels * 2)
        self.file.write(block_size.to_bytes(2, 'little'))
        # ビット/サンプル
        bit_sample = 16
        self.file.write(bit_sample.to_bytes(2, 'little'))
        # dataチャンク
        self.file.write(b'data')
        # データサイズ(ダミー)
        self.file.write(dummy_size_16bit)

    # ファイルを閉じる
    def close(self):
        # ファイルが開かれていれば閉じる
        if self.file is not None:
            # データ数を得る
            self.file.seek(0, 2)
            file_size = self.file.tell() - 8
            data_size = self.file.tell() - 44
            # データ数をヘッダに書き込む
            self.file.seek(4, 0)
            self.file.write(file_size.to_bytes(4, 'little'))
            self.file.seek(40, 0)
            self.file.write(data_size.to_bytes(4, 'little'))
            # ファイルを閉じる
            self.file.close()
            self.file = None

    # 指定した時刻に移動する。
    def move_time(self, position):
        if position < 0 or position >= self.length:
            sys.stderr.write('[WaveFileReader.seek] invalid argument\n')
            return
        position_byte = int(position * self.num_channels * 16)
        self.file.seek(position_byte+44, 0)

    # データ書き込み
    def write_data(self, data):
        int_data = np.int16(data)
        byte = int_data.tobytes()
        self.file.write(byte)


# テスト用メイン関数
if __name__ == '__main__':
    input_name = "input.wav"
    output_name = "output.wav"

    wave_reader = WaveFileReader()
    wave_reader.open(input_name)
    wave_writer = WaveFileWriter(wave_reader.sampling_rate, wave_reader.num_channels)
    wave_writer.open(output_name)
    while True:
        data = wave_reader.read_data(1)
        if np.size(data) < 1:
            break
        wave_writer.write_data(data)
