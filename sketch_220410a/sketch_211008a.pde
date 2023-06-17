void setup(){
 size(400,400);
 stroke(100);
 background(0,10,0);
}

void draw(){
 background(0,10,0);
 for(int i=0;i<=100;i++){
 line(0,0,random(400),random(400));
  line(400,0,random(400),random(400));
    line(400,400,random(400),random(400));
      line(0,400,random(400),random(400));
      saveFrame();
}
}
