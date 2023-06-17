/*
  bounce_balls04_bug_pass_by_value.pde
 
 - Show balls bouncing in the window. 
 - Click to toggle states of run/stop.
 */


boolean runningStateToggle = true;
float simulationTime = 0.0;
int simulationStep = 0;

int NBALLS = 300; 
float BALL_MASS = 1.0; 
float GRAVITY_ACCELERATION = 9.8;

Ball[] balls = new Ball[NBALLS];


class Ball {
  float x, y;      // Ball's position x & y.
  float vx, vy; // Ball's velocity, x & y components.
  color col;    // Ball's color.

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
    stroke( 0 );  // black circumference ring
    fill( col );
    ellipse( x, y, 10, 10 );  // place a circle
  }

  void reflect_bug( float x, float y, float vx, float vy ) {
    if ( ( x > width ) && vx > 0 ) {// Hit the right wall.
      vx = -vx; // Reverse the direction.
    }
    if ( ( x < 0 ) && vx < 0 ) {  // Hit the left wall.
      vx = -vx;
    }
    if ( ( y > height ) && vy > 0 ) {// Hit the floor.
      vy = -vy; // Reverse the direction.
    }
    if ( ( y < 0 ) && vy < 0 ) {  // Hit the ceiling.
      vy = -vy;
    }
  }

  void move( float dt ) {        
    x += vx*dt;
    y += vy*dt;
    vy += GRAVITY_ACCELERATION/BALL_MASS*dt;
    
    reflect_bug( x, y, vx, vy ); // pass by value
  }
} 


void draw() {
  float dt = 0.1; // delta t (time increment).
  
  background( 255 );  
  
  if ( runningStateToggle ) {
    for ( int i=0; i<NBALLS; i++ ) {
      balls[i].move( dt );
    }  
    if ( simulationStep % 100 == 0 ) {
      println( " t=" + simulationTime 
             + " step=" + simulationStep );
    }
    simulationTime += dt;
    simulationStep++;
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
    saveFrame();
    println( " Stopped. Frame saved." );
  }
}
