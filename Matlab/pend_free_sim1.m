
x=[qdot;q];
dt=0.001;
t_sim=(tmin:dt:tmax)';
phi2_sim=zeros(length(t_sim),1);
j=1;
%%%%%%%%���ߥ��쥷�������`��%%%%%%%%%%%%%%%%

for i=tmin:dt:tmax
dx1=dt*state_equation(x);
dx2=dt*state_equation(x+0.5*dx1);
dx3=dt*state_equation(x+0.5*dx2);
dx4=dt*state_equation(x+dx3);
x=x+(dx1+2*dx2+2*dx3+dx4)/6; %Runge-Kutta��

phi2_sim(j)=x(2);
j=j+1;
end

