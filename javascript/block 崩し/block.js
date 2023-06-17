window.onload = function( ev )
{
const	bw=30;
const   bh=20;
    const   ca = document.getElementById( 'main' );
    const   g = ca.getContext( '2d' );
    g.font = "80px monospace";
    g.fillStyle = "#00ff00";
const	dx=5;
const	dy=5;

blockArray=[0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0];
function DrawBlock(bx,by){
    g.fillRect(bx,by,bw,bh);
}


for(y=0;y<10;y++){

	for(x=0;x<10;x++){

		if(blockArray[x+y*10]==1){
		DrawBlock(dx+x*bw+dx*x,dy+y*bh+dy*y);
		}
	}
}

}