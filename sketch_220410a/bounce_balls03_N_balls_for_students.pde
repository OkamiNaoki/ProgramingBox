/*
  bounce_balls03_N_balls_for_students.pde
 
 - Show balls bouncing in the window. 
 - Click to toggle states of run/stop.
 */


boolean runningStateToggle = true;

float simulationTime = 0.0; 

int NBALLS=10; 

Ball[] balls = new Ball[NBALLS];

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
  
  background( 255, 255, 255 );  

  if ( runningStateToggle ) {
    for ( int i=0; i<NBALLS; i++ ) {
      balls[i].move( dt );
    }  
    simulationTime = simulationTime + dt;  
    println( " t = " + simulationTime );
  } 

  for ( int i=0; i<NBALLS; i++ ) {
    balls[i].show();
  }
}


void setup() {
  size( 500, 400 );
  float maxVelocity = 50.0;
  float minVelocity =  0.0;
  
  for ( int i=0; i<NBALLS; i++ ) {
    // position
    float x0 = random( width );
    float y0 = random( height );
    // velocity
    float vel = random( minVelocity, maxVelocity );
    float angle = random( 0, TWO_PI );
    float vx0 = vel*cos( angle );
    float vy0 = vel*sin( angle );
    // color
    int r = int( random( 100, 255 ) );
    int g = int( random( 100, 255 ) );
    int b = int( random( 100, 255 ) );
    balls[i] = new Ball( x0, y0, vx0, vy0, r, g, b ); 
  }
}


void mousePressed() {
  runningStateToggle = !runningStateToggle;
  if ( !runningStateToggle ) { // stopped.
    println( " Stopped." );
    saveFrame(); 
  }
}
