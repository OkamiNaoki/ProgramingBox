close
graphics_toolkit("gnuplot")
pkg load control
A= [ 0 0 1/3 0 0 ; 1/2 0 0 1/2 0; 1/2 0 0 0 1; 0 1 1/3 0 0 ; 0 0 1/3 1/2 0]
[ V E ] = eig(A)
sys=ss(A,[0 0 0 0 1]',eye(5),zeros(5,1),1)
initial(sys,[1 0 0 0 0]',30,'r')
hold on
sys=ss(A,[0 0 0 0 1]',eye(5),zeros(5,1),1)
initial(sys,[0 0 0 0 1]',30,'b--')
pause()
close