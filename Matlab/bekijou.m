A =[ i 1 0 0 0;0 i 1 0 0;0 0 i 1 0; 0 0 0 i 1;1 0 0 0 i ]
[ V E ] = eig(A)
abs(E)
% ��Βl�ő�̌ŗL�l�������łȂ���Ώ��3�s������蒼��
% ���f���x�N�g��
x = rand(5,1)-rand(5,1) +i*( rand(5,1)-rand(5,1) )
for k=1:10000
x = A*x;
x = x/norm(x);
end
[ V E ] = eig(A)
x'
x'*A*x % ��Βl���ő�̌ŗL�l