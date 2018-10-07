clc; clear; close all;
N = 1;
read_time = zeros(N, 1);
write_time = zeros(N, 1);

for i = 1:N
    tic
    M = csvread("C:/pseudorandomcoder/data_set/dataset" + num2str(i) + ".csv");
    read_time(i) = toc;
    fprintf("read dataset%d.csv\n", i);
    
    tic
    % csvwrite("C:/pseudorandomcoder/data_set/matlab/dataset_out" + num2str(i) + ".csv", M);
    dlmwrite("C:/pseudorandomcoder/data_set/matlab/dataset_out" + num2str(i) + ".csv", M, 'precision', 16);
    write_time(i) = toc;
    fprintf("wrote dataset%d_out.csv\n", i);
    break
end

fprintf("Average Read Time: %f\n", mean(read_time))
fprintf("Average Write Time: %f\n", mean(write_time))