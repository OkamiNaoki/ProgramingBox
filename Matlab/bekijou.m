A =[ i 1 0 0 0;0 i 1 0 0;0 0 i 1 0; 0 0 0 i 1;1 0 0 0 i ]
[ V E ] = eig(A)
abs(E)
% 絶対値最大の固有値が実数でなければ上の3行分をやり直し
% 複素数ベクトル
x = rand(5,1)-rand(5,1) +i*( rand(5,1)-rand(5,1) )
for k=1:10000
x = A*x;
x = x/norm(x);
end
[ V E ] = eig(A)
x'
x'*A*x % 絶対値が最大の固有値