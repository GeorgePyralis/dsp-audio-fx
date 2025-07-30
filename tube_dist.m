function y = tube_dist(x, Q, dist, gain)
    maxAbs_x = max(abs(x));
    normalized_x = x / maxAbs_x;
    gained_x = normalized_x * gain;

    if Q ~= 0
        f = ((gained_x - Q) ./ (1 - exp(-dist * (gained_x - Q)))) + ...
            (Q / (1 - exp(dist * Q)));
    else
        f = (1 ./ dist) * ones(size(x));
    end

    maxAbs_f = max(abs(f));
    y = f / maxAbs_f;
end
