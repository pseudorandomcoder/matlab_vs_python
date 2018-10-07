% Generae n x m data set
m = 1e2;
n = 10;
N = 1;
for i = 1:N
    data = 10000*rand(m, n);
    csvwrite("dataset" + num2str(i) + ".csv", data)
end