function xdot=state_equation(x)
global m2 l2 g c2 J2 J2b;

qdot=x(1);
q=x(2);
xdot=[
     (- m2*g*l2*sin(q) - c2*qdot)/J2b;
      qdot
      ];
end