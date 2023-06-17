/*
  bounce_balls01_single_ball_for_students.pde
 
 - Show a ball bouncing in the window. 
 - Click to toggle states of run/stop.
 */


boolean runningStateToggle = true;

float simulationTime = 0.0; 

Ball greenBall;
Ball redBall;

class Ball {
  float x; // Ball's position x
  float y; //             and y
  float vx, vy; // Ball's velocity, x and y components.
  color col;  // color.

  Ball( float xInit, float yInit, 
        float vxInit, float vyInit, 
        int red, int green, int blue ) {
    x = xInit;
    y = yInit;
    vx = vxInit;
    vy = vyInit;
    col = color( red, green, blue );
  }
  
  void show() {
    stroke( 0 );
    fill( col );
    ellipse( x, y, 10, 10 );  // place a circle
  }

  void move(float dt) {
    x += vx*dt;  // shift the ball position in x.
    y += vy*dt;  // ... in y.
    if ( x >= width ) {// The ball hits the right wall. 
      x = width;
      vx = -vx; // Reverse the direction.
    }
    if ( x<= 0 ) {  // Hit the left wall.
      x = 0;
      vx = -vx;
    }
    if ( y >= height ) {// Hit the floor. 
      y = height;
      vy = -vy; // Reverse the direction.
    }
    if ( y <= 0 ) {  // Hit the ceiling.
      y = 0;
      vy = -vy;
    }
  }
void moveR(float dt,float vxd,float vyd) {
    vx=vxd;
    vy=vyd;
    x += vx*dt;  // shift the ball position in x.
    y += vy*dt;  // ... in y.
    if ( x >= width ) {// The ball hits the right wall. 
      x = width;
      vx = -vx; // Reverse the direction.
    }
    if ( x<= 0 ) {  // Hit the left wall.
      x = 0;
      vx = -vx;
    }
    if ( y >= height ) {// Hit the floor. 
      y = height;
      vy = -vy; // Reverse the direction.
    }
    if ( y <= 0 ) {  // Hit the ceiling.
      y = 0;
      vy = -vy;
    }
  }
  
 }

void hit(float dt){
  float vgx=(greenBall.vx+redBall.vx)/2;
  float vgy=(greenBall.vy+redBall.vy)/2;
  float ex=greenBall.y-redBall.y;
  float ey=-(greenBall.x-redBall.x);
  float v1x=greenBall.vx-vgx;
  float v1y=greenBall.vy-vgy;
  float v2x=redBall.vx-vgx;
  float v2y=redBall.vy-vgy;
  float fai=acos((v1x*ex+v1y*ey)/sqrt(v1x*v1x+v1y*v1y));
  greenBall.moveR(dt,cos(2*fai)*v1x+sin(2*fai)*v1y+vgx+vgx,-sin(2*fai)*v1x+cos(2*fai)*v1y+vgy+vgy);
  redBall.moveR(dt,cos(2*fai)*v2x+sin(2*fai)*v2y+vgx*2,-sin(2*fai)*v2x+cos(2*fai)*v2y+vgy*2);
}

void draw() {
  float dt = 0.01; // delta t (time increment).
  
  background( 200, 200, 150 );  

  if ( runningStateToggle ) {
    if(sqrt((greenBall.x-redBall.x)*(greenBall.x-redBall.x)+(greenBall.y-redBall.y)*(greenBall.y-redBall.y))<=10){
       hit(dt);
    }else{
       greenBall.move( dt );
       redBall.move(dt);
    }

    simulationTime = simulationTime + dt;
    println( " t = " + simulationTime );
  }
  greenBall.show();
  redBall.show();
}


void setup() {
  size( 300, 300 );
  float x0 = width/2;
  float y0 = height/2;
  float vx0 = 13.0;
  float vy0 = 13.0;
  greenBall = new Ball( x0, y0, vx0, vy0, 50, 255, 50 ); 
  redBall = new Ball( x0+100, y0+100.0, -vx0, -vy0, 255, 50, 50 ); 
}


void mousePressed() {
  runningStateToggle = !runningStateToggle;
  if ( !runningStateToggle ) { // stopped.
    println( " Stopped." );
  }
}
