

/*

  関数pressedBtnは次の処理を行う

  (1) getElementById() メソッドでform要素全体を取得して変数targetに格納する

  (2) getElementById() メソッドでp要素全体を取得して変数reportに格納する

  (3) 問で選ばれた選択肢のvalue属性の値をv1とv2に格納する

  (4) v1とv2を比較演算子を用いて比較し判定結果を出力する

*/function pressedBtn(){
  var v1;
  var v2;

  target = document.getElementById('quizForm');
  report = document.getElementById('quizReport');

  // value属性の値を変数v1と変数v2に代入

v1 = target.radios1.value;
v2 = target.radios2.value;

  console.log(v1,v2);



  // 得点0点から始める(変数pntに0を代入)

 pnt = 0;



  // 問1が正解か不正解か判定

if (v1 ==0) {//正解

  pnt = pnt + 5;

  q1m = '問1は正解です';



}else if (v1 ==1) {//不正解

   q1m = '問1はよく読んでください';

}else if (v1 ==2) {//不正解

   q1m = '問1はそれでいいですか？';

}else if (v1 ==3) {//不正解

   q1m = '問1は選択肢4を選びましたね。困ったな。';

}else{

  //どれでもない

     q1m = 'どの選択肢も選ばれていません';

  }

// 問が2正解か不正解か判定

if (v2 ==3) {//正解

  pnt = pnt + 5;

q2m = '問2は正解です';

}else if (v2 ==0) {//不正解

q2m = '問2は残念です';

}else if (v2 ==1) {//不正解

q2m = '問2は本当ですか';

}else if (v2 ==2) {//不正解

q2m = '問2はそんなに少ないです';

}else{

//どれでもない

console.log('問2は何も選んでいません');

}

// レポートの文字列の結合

  result = pnt + '点でした。<br>' + q1m + '<br>' + q2m;



  // 結果表示部分に出力する

  report.innerHTML = result;

 console.log('クイズが判定されました',pnt+'点です');

  if( pnt == 10 ){

    result = result + '<br>全問正解おめでとうございます<br>';

    for ( x = 1; x <= 20; x = x + 1 ) {

    console.log('x=' + x);

    // ここに書いた命令が繰り返されます

    result = result + '&#9786;';

}

    report.innerHTML = result;

}
}