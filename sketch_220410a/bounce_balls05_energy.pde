/*
  bounce_balls05_energy.pde
 
 - Show balls bouncing in the window. 
 - Click to toggle states of run/stop.
 */


boolean runningStateToggle = true;
float simulationTime = 0.0;
int simulationStep = 0;

int NBALLS = 300; 
float BALL_MASS = 1.0; 
float GRAVITY_ACCELERATION = 9.8;

float energy0;  // Total energy at t=0.

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

  float getEnergy() {
    float vsq = pow( vx, 2 ) + pow( vy, 2 );   // velocity squared
    float kinetic_energy = 0.5*BALL_MASS*vsq;
    float potential_energy = BALL_MASS * GRAVITY_ACCELERATION * ( height - y );
    return kinetic_energy + potential_energy;
  }

  void reflect( float[] posvel ) {
    if ( ( posvel[0] > width ) && posvel[2] > 0 ) {// Hit the right wall.
      posvel[2] = -posvel[2]; // Reverse the direction.
    }
    if ( ( posvel[0] < 0 ) && posvel[2] < 0 ) {  // Hit the left wall.
      posvel[2] = -posvel[2];
    }
    if ( ( posvel[1] > height ) && posvel[3] > 0 ) {// Hit the floor.
      posvel[3] = -posvel[3]; // Reverse the direction.
    }
    if ( ( posvel[1] < 0 ) && posvel[3] < 0 ) {  // Hit the ceiling.
      posvel[3] = -posvel[3];
    }
  }

  void move( float dt ) {        
    x += vx*dt;
    y += vy*dt;
    vy += GRAVITY_ACCELERATION/BALL_MASS*dt;

    float[] posvelForPassByReference = new float[4];
    
    posvelForPassByReference[0] = x;
    posvelForPassByReference[1] = y;
    posvelForPassByReference[2] = vx;
    posvelForPassByReference[3] = vy;
    
    reflect( posvelForPassByReference );

    x = posvelForPassByReference[0];
    y = posvelForPassByReference[1];
    vx = posvelForPassByReference[2];
    vy = posvelForPassByReference[3];
  }
} 


float totalEnergy() {
  float sum = 0.0;
  for( int i=0; i<NBALLS; i++ ) {
    sum = sum + balls[i].getEnergy();
  }
  return sum;
}


void simulation_step( float dt ) 
{
  float energy, error;

  if ( runningStateToggle ) {
    for ( int i=0; i<NBALLS; i++ ) {
      balls[i].move( dt );
    }  
    if ( simulationStep % 100 == 0 ) {
      energy = totalEnergy();
      error = abs( ( energy-energy0 ) / energy0 ); 
      println( " t=" + simulationTime 
             + " step=" + simulationStep
             + " energy=" + energy
             + " error="  + error );
    }
    simulationTime += dt;
    simulationStep++;
  }   
}

void draw() 
{
  background( 255 );  

  float dt = 0.1;      // delta t (time increment).
  //float dt = 0.01;   // delta t (time increment).
  simulation_step( dt );
  
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
  
  energy0 = totalEnergy();  // Total energy at t=0. 
}


void mousePressed() {
  runningStateToggle = !runningStateToggle;
  if ( !runningStateToggle ) { // stopped.
    saveFrame();
    println( " Stopped. Frame saved." );
  }
}
