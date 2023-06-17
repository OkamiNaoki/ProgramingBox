/*
  bounce_balls01_single_ball_for_students.pde
 
 - Show a ball bouncing in the window. 
 - Click to toggle states of run/stop.
 */


boolean runningStateToggle = true;

float simulationTime = 0.0; 

Ball greenBall;

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
}


void draw() {
  float dt = 0.1; // delta t (time increment).
  
  background( 200, 200, 150 );  

  if ( runningStateToggle ) {  
    greenBall.move( dt );
    simulationTime = simulationTime + dt;
    println( " t = " + simulationTime );
  }
  greenBall.show();
}


void setup() {
  size( 300, 300 );
  float x0 = width/2;
  float y0 = height/2;
  float vx0 = 20.0;
  float vy0 = 13.0;
  greenBall = new Ball( x0, y0, vx0, vy0, 50, 255, 50 ); 
}


void mousePressed() {
  runningStateToggle = !runningStateToggle;
  if ( !runningStateToggle ) { // stopped.
    println( " Stopped." );
  }
}
