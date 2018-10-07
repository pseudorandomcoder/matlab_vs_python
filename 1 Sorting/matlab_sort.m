N = 1e5;
trials = 1e3;

times = zeros(trials, 1);

for i = 1:trials
    data = rand(N, 1);
    tic
    data = sort(data);
    times(i) = toc;
    fprintf('Completed %d trials\n', i)
end

fprintf('Average Time: %d\n', mean(times))