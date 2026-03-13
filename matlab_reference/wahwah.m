function y = wahwah(x, Q, fc, V0, fs, mix)
    y_a = zeros(length(x), 1);
    for n = 3:length(x)
        sawtooth_wave = sawtooth(2 * pi * n / fs, 1);
        triangle_wave = 2 * abs(mod(sawtooth_wave, 2) - 1) - 1;

        F = fc * (1 + 0.35 * triangle_wave);
        K = tan(pi * F / fs);

        b0 = (1 + (K * V0 / Q) + K^2) / (1 + (K / Q) + K^2);
        b1 = 2 * (K^2 - 1) / (1 + (K / Q) + K^2);
        b2 = (1 - (K * V0 / Q) + K^2) / (1 + (K / Q) + K^2);
        a1 = b1;
        a2 = (1 - (K / Q) + K^2) / (1 + (K / Q) + K^2);

        y_a(n) = b0 * x(n) + b1 * x(n - 1) + b2 * x(n - 2) ...
                 - a1 * y_a(n - 1) - a2 * y_a(n - 2);
    end

    y = mix * y_a + (1 - mix) * x;
end
