ba = [4	12	40	144	544	2112	8320	33024	131584	525312	2099200	8392704	33562624	134234112];
fa = [19	68	196	512	1264	3008	6976	15872	35584	78848	173056	376832	815104	1753088];
N=[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192];
idealB = 2*N.^2;
plot(N(1:8),fa(1:8),N(1:8),ba(1:8))
legend('FFT','Brute Force','location', 'NW');
grid on;
xlabel('Number of coefficients (N)');
ylabel('Number of Assignments');
title('FFT vs Brute Force Assignments based on input');
plot(N,fa,N,ba)
legend('FFT','Brute Force','location', 'NW');
grid on;
xlabel('Number of coefficients (N)');
ylabel('Number of Assignments');
title('FFT vs Brute Force Assignments based on input');
plot(N,idealB, N, ba);

bc = [1	4	16	64	256	1024	4096	16384	65536	262144	1048576	4194304	16777216	67108864];
fc = [3	12	36	96	240	576	1344	3072	6912	15360	33792	73728	159744	344064];
plot(N(1:6),fc(1:6),N(1:6),bc(1:6))
legend('FFT','Brute Force','location', 'NW');
grid on;
xlabel('Number of coefficients (N)');
ylabel('Number of Comparisons');
title('FFT vs Brute Force Comparisons based on input');

plot(N,fc,N,bc)
legend('FFT','Brute Force','location', 'NW');
grid on;
xlabel('Number of coefficients (N)');
ylabel('Number of Comparisons');
title('FFT vs Brute Force Comparisons based on input');