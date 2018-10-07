clc; clear; close all;

n = 1e4;
trials = 1e1;
time = zeros(trials, 1);

for i = 1:trials
    A = ceil(100*rand(n, n));
    % must be invertable
    while(det(A) == 0)
        A = ceil(100*rand(n, n));
    end
    
    tic
    A_inv = inv(A);
    time(i) = toc;
    fprintf('%d runs complete\n', i)
end

fprintf('Average run time: %f seconds\n', mean(time))