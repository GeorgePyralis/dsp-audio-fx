clc;
clear;

[x, fs] = audioread('guitar1.wav');

% Step 1: Tube Distortion
Q = -0.2;
dist = 8;
gain = 10;
y1 = tube_dist(x, Q, dist, gain);

% Step 2: WahWah
Q = 10;
fc = 3000;
V0 = 50;
mix = 0.5;
y2 = wahwah(y1, Q, fc, V0, fs, mix);

% Step 3: Reverb
room = 1;
mix = 0.5;
y3 = reverb(y2, room, mix);

sound(y3, fs);