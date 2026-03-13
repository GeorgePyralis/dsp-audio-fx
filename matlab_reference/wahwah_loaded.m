clc;
clear;

[x, fs] = audioread('guitar1.wav');
Q = 10;
fc = 3000;
V0 = 50;
mix = 0.5;

y = wahwah(x, Q, fc, V0, fs, mix);

specgram(x);
title('Original');

figure;
specgram(y);
title('WahWah');

sound(y, fs);
