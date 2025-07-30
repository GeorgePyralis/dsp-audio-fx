clc;
clear;

[x, fs] = audioread('guitar1.wav');

Q = -0.2;
dist = 8;
gain = 10;

y = tube_dist(x, Q, dist, gain);

specgram(x);
title('Original');

figure; 
specgram(y);
title('Tube Distortion');

sound(x, fs); 

