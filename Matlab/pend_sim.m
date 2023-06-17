clear
format compact
% -----------------------
global m2 l2 g c2 J2 J2b;
m2 = 4.2e-03; 
l2 = 7.60e-02;
g  = 9.81e+00;

c2  = 1.0e-05; %3.0e-05; 9.0e-05;
J2  = 9.54e-06;
J2b = J2+m2*l2^2;

tmin = 0;
tmax = 7;

phi20 = 90*pi/180;
q=phi20;
qdot=0;
qdotdot=0;
pend_free_sim1;
figure(1)
plot(t_sim,phi2_sim*180/pi,'r')
hold on

set(gca,'fontname','arial','fontsize',30)
xlim([0 tmax-tmin]); ylim([-100 100])

xlabel('t [s]','fontsize',30)
ylabel('{\phi}_{2}(t) [deg]', 'fontsize',30)
title('Naoki Okami, 1935084T','fontsize',30) % 氏名?�ローマ字）と学番を記�?
%title('Time history of {\phi}_{2} [deg]', 'interpreter', 'latex', 'Units', 'normalized', 'Position', [0.5, -0.3, 0])
legend({'Nonlinear Simulation'}, 'location','northeast')
set(legend,'fontsize',30)

set(gca,'xtick',0:1:tmax-tmin)
set(gca,'ytick',-90:45:90)
set(gcf,'PaperUnits','inches','PaperPosition',[0 0 8 6])
hold off;



print -djpeg figure_pend.jpg

