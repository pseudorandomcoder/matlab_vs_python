clc; clear; close all;
my_path = "C:/pseudorandomcoder/data_set/matlab/dataset_out";
data_path = "C:/pseudorandomcoder/data_set/dataset";


N = 10;
read_time = zeros(N, 1);
write_time = zeros(N, 1);
for i = 1:N
    tic
    M = csvread(data_path + num2str(i-1) + ".csv");
    read_time(i) = toc;
    fprintf("read dataset%d.csv\n", i-1);
    
    tic
    % dont' use csvwrite, it's limited to 5 points of precision
    dlmwrite(my_path + num2str(i-1) + ".csv", M, 'precision', 16);
    write_time(i) = toc;
    fprintf("wrote dataset%d_out.csv\n", i-1);
end

fprintf("Average Read Time: %f\n", mean(read_time))
fprintf("Average Write Time: %f\n", mean(write_time))