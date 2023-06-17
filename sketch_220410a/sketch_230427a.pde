//サンプルにあったカメラを使用して、3次元に配置した球体を場所ごとに色を変え観察できるプログラムです。
void setup() {
  size(1000, 1000, P3D);
  fill(100);
}

void draw() {
  lights();
  background(0);
  
  // Change height of the camera with mouseY
  camera(-100, mouseY-100, -100, // eyeX, eyeY, eyeZ
         0.0, 0.0, 0.0, // centerX, centerY, centerZ
         0.0, 2.0, 0.0); // upX, upY, upZ
  
  noStroke();
  stroke(255);
  for(int z = 0; z < 5; z ++){    //立方体を、z軸方向に30ピクセルごとに並べて6個生成  
    for(int y = 0; y < 5; y ++){    //立方体を、y軸方向に30ピクセルごとに並べて6個生成  
      for(int x = 0; x < 5; x ++){    //立方体を、x軸方向に30ピクセルごとに並べて6個生成
        stroke(x*50,y*50,z*50);
        pushMatrix();
        translate(x*20, y*20, z*20);
        sphere(10);    //20 x 20 x 20pxの立方体を描く
        popMatrix();
      }
    }
  }
}
