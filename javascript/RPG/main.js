"use strict";

const	CHRHEIGHT	= 9;					//	�L�����̍���
const	CHRWIDTH	= 8;					//	�L�����̕�
const	FONT		= "12px monospace";		//	�g�p�t�H���g
const	FONTSTYLE	= "#ffffff";			//	�����F
const	HEIGHT		= 120;					//	���z��ʃT�C�Y�B����
const	WIDTH		= 128;					//	���z��ʃT�C�Y�B��
const	INTERVAL	= 33;					//	�t���[���Ăяo���Ԋu
const	MAP_HEIGHT	= 32;					//	�}�b�v����
const	MAP_WIDTH	= 32;					//	�}�b�v��
const	SCR_HEIGHT	= 8;					//	��ʃ^�C���T�C�Y�̔����̍���
const	SCR_WIDTH	= 8;					//	��ʃ^�C���T�C�Y�̔����̕�
const	SCROLL		= 1;					//	�X�N���[�����x
const	SMOOTH		= 0;					//	��ԏ���
const	START_HP	= 20;					//	�J�nHP
const	START_X		= 15;					//	�J�n�ʒuX
const	START_Y		= 17;					//	�J�n�ʒuY
const	TILECOLUMN	= 4;					//	�^�C������
const	TILEROW		= 4;					//	�^�C���s��
const	TILESIZE	= 8;					//	�^�C���T�C�Y(�h�b�g�j
const	WNDSTYLE = "rgba( 0, 0, 0, 0.75 )";	//	�E�B���h�E�̐F

const	gKey = new Uint8Array( 0x100 );		//	�L�[���̓o�b�t�@

let		gAngle = 0;							//	�v���C���[�̌���
let		gEx = 0;							//	�v���C���[�̌o���l
let		gHP = START_HP;						//	�v���C���[��HP
let		gMHP = START_HP;					//	�v���C���[�̍ő�HP
let		gLv = 1;							//	�v���C���[�̃��x��
let		gCursor = 0;						//	�J�[�\���ʒu
let		gEnemyType;							//	�G���
let		gFrame = 0;							//	�����J�E���^
let		gHeight;							//	����ʂ̍���
let		gWidth;								//	����ʂ̕�
let		gMessage1 = null;					//	�\�����b�Z�[�W�P
let		gMessage2 = null;					//	�\�����b�Z�[�W�Q
let		gMoveX = 0;							//	�ړ���X
let		gMoveY = 0;							//	�ړ���Y
let		gImgMap;							//	�摜�B�}�b�v
let		gImgMonster;						//	�摜�B�����X�^�[
let		gImgPlayer;							//	�摜�B�v���C���[
let		gItem = 0;							//	�����A�C�e��
let		gPhase = 0;							//	�퓬�t�F�[�Y
let		gPlayerX = START_X * TILESIZE + TILESIZE / 2;	//	�v���C���[���WX
let		gPlayerY = START_Y * TILESIZE + TILESIZE / 2;	//	�v���C���[���WY
let		gScreen;							//	���z���


const	gFileMap		= "img/map.png";
const	gFileMonster	= "img/monster.png";
const	gFilePlayer		= "img/player.png";

const	gEncounter = [ 0, 0, 0, 1, 0, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0 ];	//	�G�G���J�E���g�m��

const	gMonsterName = [ "�X���C��", "������", "�i�C�g", "�h���S��", "����" ];	//	�����X�^�[����

//	�}�b�v
const	gMap = [
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 3, 6, 3, 6, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 3, 3, 6, 6, 7, 7, 7, 2, 2, 2, 7, 7, 7, 7, 7, 7, 7, 6, 3, 0, 0, 0, 3, 3, 0, 6, 6, 6, 0, 0, 0,
 0, 0, 3, 3, 6, 6, 6, 7, 7, 2, 2, 2, 7, 7, 2, 2, 2, 7, 7, 6, 3, 3, 3, 6, 6, 3, 6,13, 6, 0, 0, 0,
 0, 3, 3,10,11, 3, 3, 6, 7, 7, 2, 2, 2, 2, 2, 2, 1, 1, 7, 6, 6, 6, 6, 6, 3, 0, 6, 6, 6, 0, 0, 0,
 0, 0, 3, 3, 3, 0, 3, 3, 3, 7, 7, 2, 2, 2, 2, 7, 7, 1, 1, 6, 6, 6, 6, 3, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 7, 7, 7, 7, 2, 7, 6, 3, 1, 3, 6, 6, 6, 3, 0, 0, 0, 3, 3, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 6, 6, 7, 2, 7, 6, 3, 1, 3, 3, 6, 6, 3, 0, 0, 0, 3, 3, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 6, 7, 7, 7, 6, 3, 1, 1, 3, 3, 6, 3, 3, 0, 0, 3, 3, 3, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 6, 6, 7, 7, 7, 6, 3, 1, 1, 3, 3, 6, 3, 3, 0, 3,12, 3, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 6, 6, 6, 7, 7, 6, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 6, 6, 6, 6, 3, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 6, 6, 3, 3, 3, 3, 1, 1, 3, 3, 3, 1, 1, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 5, 3, 3, 3, 6, 6, 6, 3, 3, 3, 1, 1, 1, 1, 1, 3, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 8, 9, 3, 3, 3, 6, 6, 6, 6, 3, 3, 3, 3, 3, 3, 1, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 6, 6, 6, 3, 3, 3, 3, 3, 3, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 6, 6, 6, 6, 3, 3, 3, 3, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 6, 6, 6, 6, 3, 3, 3, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 6, 6, 6, 3, 3, 3, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 6, 6, 6, 3, 6, 6, 6, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 6, 6, 3, 6, 6, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 6, 6, 3, 6, 6, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 6, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 6, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,14, 6, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0,
 7,15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0, 0, 0,
 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7,
];


//	�퓬�s������
function Action()
{
	gPhase++;											//	�t�F�[�Y�o��

	if( gPhase == 3 ){
		SetMessage( gMonsterName[ gEnemyType ] + "�̍U���I", 999 + " �̃_���[�W�I" );
gPhase = 7;
		return;
	}

	if( gCursor == 0 ){									//	�u�키�v�I����
		SetMessage( "���Ȃ��̍U���I", 333 + " �̃_���[�W�I" );
gPhase = 5;
		return;
	}

	if( Math.random() < 0.5 ){							//	�u������v������
		SetMessage( "���Ȃ��͓����o����", null );
		gPhase = 6;
		return;
	}

	//	�u������v���s��
	SetMessage( "���Ȃ��͓����o����", "��������荞�܂ꂽ�I" );
}

//	�o���l���Z
function AddExp( val )
{
	gEx += val;											//	�o���l���Z
	while( gLv * ( gLv + 1 ) * 2 <= gEx ){				//	���x���A�b�v�����𖞂����Ă���ꍇ
		gLv++;											//	���x���A�b�v
		gMHP += 4 + Math.floor( Math.random() * 3 );	//	�ő�HP�㏸4�`6
	}
}


//	�퓬�R�}���h
function CommandFight()
{
	gPhase = 2;					//	�퓬�R�}���h�I���t�F�[�Y
	gCursor = 0;
	SetMessage( "�@�키", "�@������" );
}


//	�퓬��ʕ`�揈��
function DrawFight( g )
{
	g.fillStyle = "#000000";							//	�w�i�F
	g.fillRect( 0, 0, WIDTH, HEIGHT );					//	��ʑS�̂���`�`��

	let		w = gImgMonster.width / 4;
	let		h = gImgMonster.height;

	g.drawImage( gImgMonster, gEnemyType * w, 0, w, h, Math.floor( WIDTH / 2 - w / 2 ), Math.floor( HEIGHT / 2 - h / 2 ), w, h );	//	

	DrawStatus( g );									//	�X�e�[�^�X�`��
	DrawMessage( g );									//	���b�Z�[�W�`��

	if( gPhase == 2 ){									//	�퓬�t�F�[�Y���R�}���h�I�𒆂̏ꍇ
		g.fillText( "��", 6, 96 + 14 * gCursor );		//	�J�[�\���`��
	}
}

//	�t�B�[���h�`�揈��
function DrawField( g )
{

	let		mx = Math.floor( gPlayerX / TILESIZE );			//	�v���C���[�̃^�C�����WX
	let		my = Math.floor( gPlayerY / TILESIZE );			//	�v���C���[�̃^�C�����WY

	for( let dy = -SCR_HEIGHT; dy <= SCR_HEIGHT; dy++ ){
		let		ty = my + dy;								//	�^�C�����WY
		let		py = ( ty + MAP_HEIGHT ) % MAP_HEIGHT;		//	���[�v��^�C�����WY
		for( let dx = -SCR_WIDTH; dx <= SCR_WIDTH; dx++ ){
			let		tx = mx + dx;							//	�^�C�����WX
			let		px = ( tx + MAP_WIDTH  ) % MAP_WIDTH;	//	���[�v��^�C�����WX
			DrawTile( g,
			          tx * TILESIZE + WIDTH  / 2 - gPlayerX,
			          ty * TILESIZE + HEIGHT / 2 - gPlayerY,
			          gMap[ py * MAP_WIDTH + px ] );
		}
	}

	//	�v���C���[
	g.drawImage( gImgPlayer,
	             ( gFrame >> 4 & 1 ) * CHRWIDTH, gAngle * CHRHEIGHT, CHRWIDTH, CHRHEIGHT,
	             WIDTH / 2 - CHRWIDTH / 2, HEIGHT / 2 - CHRHEIGHT + TILESIZE / 2, CHRWIDTH, CHRHEIGHT );

	//	�X�e�[�^�X�E�B���h�E
	g.fillStyle = WNDSTYLE;							//	�E�B���h�E�̐F
	g.fillRect( 2, 2, 44, 37 );						//	��`�`��

	DrawStatus( g );								//	�X�e�[�^�X�`��
	DrawMessage( g );								//	���b�Z�[�W�`��
}


function DrawMain()
{
	const	g = gScreen.getContext( "2d" );				//	���z��ʂ�2D�`��R���e�L�X�g���擾

	if( gPhase <= 1 ){
		DrawField( g );									//	�t�B�[���h��ʕ`��
	}else{
		DrawFight( g );
	}

/*
	g.fillStyle = WNDSTYLE;							//	�E�B���h�E�̐F
	g.fillRect( 20, 3, 105, 15 );					//	��`�`��

	g.font = FONT;									//	�����t�H���g��ݒ�
	g.fillStyle = FONTSTYLE;						//	�����F
	g.fillText( "x=" + gPlayerX + " y=" + gPlayerY + " m=" + gMap[ my * MAP_WIDTH + mx ], 25, 15 );
*/
}


//	���b�Z�[�W�`��
function DrawMessage( g )
{
	if( !gMessage1 ){								//	���b�Z�[�W���e�����݂��Ȃ��ꍇ
		return;
	}

	g.fillStyle = WNDSTYLE;							//	�E�B���h�E�̐F
	g.fillRect( 4, 84, 120, 30 );					//	��`�`��

	g.font = FONT;									//	�����t�H���g��ݒ�
	g.fillStyle = FONTSTYLE;						//	�����F
	g.fillText( gMessage1, 6, 96 );					//	���b�Z�[�W�P�s�ڕ`��
	if( gMessage2 ){
		g.fillText( gMessage2, 6, 110 );			//	���b�Z�[�W�Q�s�ڕ`��
	}
}


//	�X�e�[�^�X�`��
function DrawStatus( g )
{
	g.font = FONT;									//	�����t�H���g��ݒ�
	g.fillStyle = FONTSTYLE;						//	�����F
	g.fillText( "Lv " + gLv, 4, 13 );				//	Lv
	g.fillText( "HP " + gHP, 4, 25 );				//	HP
	g.fillText( "Ex " + gEx, 4, 37 );				//	Ex
}


function DrawTile( g, x, y, idx )
{
	const		ix = ( idx % TILECOLUMN ) * TILESIZE;
	const		iy = Math.floor( idx / TILECOLUMN ) * TILESIZE;
	g.drawImage( gImgMap, ix, iy, TILESIZE, TILESIZE, x, y, TILESIZE, TILESIZE );
}


function LoadImage()
{
	gImgMap     = new Image();	gImgMap.src     = gFileMap;		//	�}�b�v�摜�ǂݍ���
	gImgMonster = new Image();	gImgMonster.src = gFileMonster;	//	�����X�^�[�摜�ǂݍ���
	gImgPlayer  = new Image();	gImgPlayer.src  = gFilePlayer;	//	�v���C���[�摜�ǂݍ���
}


//function SetMessage( v1, v2 = null )	//	IE�Ή�
function SetMessage( v1, v2 )
{
	gMessage1 = v1;
	gMessage2 = v2;
}


//	IE�Ή�
function Sign( val )
{
	if( val == 0 ){
		return( 0 );
	}
	if( val < 0 ){
		return( -1 );
	}
	return( 1 );
}


//	�t�B�[���h�i�s����
function TickField()
{
	if( gMoveX != 0 || gMoveY != 0 || gMessage1 ){}				//	�ړ������̓��b�Z�[�W�\�����̏ꍇ
	else if( gKey[ 37 ] ){	gAngle = 1;	gMoveX = -TILESIZE;	}	//	��
	else if( gKey[ 38 ] ){	gAngle = 3;	gMoveY = -TILESIZE;	}	//	��
	else if( gKey[ 39 ] ){	gAngle = 2;	gMoveX =  TILESIZE;	}	//	�E
	else if( gKey[ 40 ] ){	gAngle = 0;	gMoveY =  TILESIZE;	}	//	��

	//	�ړ���̃^�C�����W����
	let		mx = Math.floor( ( gPlayerX + gMoveX ) / TILESIZE );	//	�ړ���̃^�C�����WX
	let		my = Math.floor( ( gPlayerY + gMoveY ) / TILESIZE );	//	�ړ���̃^�C�����WY
	mx += MAP_WIDTH;								//	�}�b�v���[�v����X
	mx %= MAP_WIDTH;								//	�}�b�v���[�v����X
	my += MAP_HEIGHT;								//	�}�b�v���[�v����Y
	my %= MAP_HEIGHT;								//	�}�b�v���[�v����Y
	let		m = gMap[ my * MAP_WIDTH + mx ];		//	�^�C���ԍ�
	if( m < 3 ){									//	�N���s�̒n�`�̏ꍇ
		gMoveX = 0;									//	�ړ��֎~X
		gMoveY = 0;									//	�ړ��֎~Y
	}

	if( Math.abs( gMoveX ) + Math.abs( gMoveY ) == SCROLL ){	//	�}�X�ڈړ����I��钼�O
		if( m == 8 || m == 9 ){		//	����
			gHP = gMHP;										//	HP�S��
			SetMessage( "������|���āI", null );
		}

		if( m == 10 || m == 11 ){	//	�X
			gHP = gMHP;										//	HP�S��
			SetMessage( "���̉ʂĂɂ�", "��������܂�" );
		}

		if( m == 12 ){	//	��
			gHP = gMHP;										//	HP�S��
			SetMessage( "�J�M�́A", "���A�ɂ���܂�" );
		}

		if( m == 13 ){	//	���A
			gItem = 1;	//	�J�M����
			SetMessage( "�J�M����ɓ��ꂽ", null );
		}

		if( m == 14 ){	//	��
			if( gItem == 0 ){			//	�J�M��ێ����Ă��Ȃ��ꍇ
				gPlayerY -= TILESIZE;		//	�P�}�X��ֈړ�
				SetMessage( "�J�M���K�v�ł�", null );
			}else{
				SetMessage( "�����J����", null );
			}
		}

		if( m == 15 ){	//	�{�X
			SetMessage( "������|��", "���E�ɕ��a���K�ꂽ" );
		}

		if( Math.random() * 4 < gEncounter[ m ] ){	//	�����_���G���J�E���g
			gPhase = 1;								//	�G�o���t�F�[�Y
			gEnemyType = 1;
			SetMessage( "�G�����ꂽ�I", null );
		}
	}

	gPlayerX += Sign( gMoveX ) * SCROLL;		//	�v���C���[���W�ړ�X
	gPlayerY += Sign( gMoveY ) * SCROLL;		//	�v���C���[���W�ړ�Y
	gMoveX -= Sign( gMoveX ) * SCROLL;			//	�ړ��ʏ���X
	gMoveY -= Sign( gMoveY ) * SCROLL;			//	�ړ��ʏ���Y

	//	�}�b�v���[�v����
	gPlayerX += ( MAP_WIDTH  * TILESIZE );
	gPlayerX %= ( MAP_WIDTH  * TILESIZE );
	gPlayerY += ( MAP_HEIGHT * TILESIZE );
	gPlayerY %= ( MAP_HEIGHT * TILESIZE );
}


function WmPaint()
{
	DrawMain();

	const	ca = document.getElementById( "main" );	//	main�L�����o�X�̗v�f���擾
	const	g = ca.getContext( "2d" );				//	2D�`��R���e�L�X�g���擾
	g.drawImage( gScreen, 0, 0, gScreen.width, gScreen.height, 0, 0, gWidth, gHeight );	//	���z��ʂ̃C���[�W������ʂ֓]��
}


//	�u���E�U�T�C�Y�ύX�C�x���g
function WmSize()
{
	const	ca = document.getElementById( "main" );	//	main�L�����o�X�̗v�f���擾
	ca.width = window.innerWidth;					//	�L�����o�X�̕����u���E�U�̕��֕ύX
	ca.height = window.innerHeight;					//	�L�����o�X�̍������u���E�U�̍����֕ύX

	const	g = ca.getContext( "2d" );				//	2D�`��R���e�L�X�g���擾
	g.imageSmoothingEnabled = g.msImageSmoothingEnabled = SMOOTH;	//	��ԏ���

	//	����ʃT�C�Y���v���B�h�b�g�̃A�X�y�N�g����ێ������܂܂ł̍ő�T�C�Y���v������B
	gWidth = ca.width;
	gHeight = ca.height;
	if( gWidth / WIDTH < gHeight / HEIGHT ){
		gHeight = gWidth * HEIGHT / WIDTH;
	}else{
		gWidth = gHeight * WIDTH / HEIGHT;
	}
}


//	�^�C�}�[�C�x���g�������̏���
function WmTimer()
{
	gFrame++;						//	�����J�E���^�����Z
	TickField();					//	�t�B�[���h�i�s����
	WmPaint();
}


//	�L�[����(DONW)�C�x���g
window.onkeydown = function( ev )
{
	let		c = ev.keyCode;			//	�L�[�R�[�h�擾

	if( gKey[ c ] != 0 ){			//	���ɉ������̏ꍇ�i�L�[���s�[�g�j
		return;
	}
	gKey[ c ] = 1;

	if( gPhase == 1 ){				//	�G�����ꂽ�ꍇ
		CommandFight();				//	�퓬�R�}���h
		return;
	}

	if( gPhase == 2 ){				//	�퓬�R�}���h�I�𒆂̏ꍇ
		if( c == 13 || c == 90 ){	//	Enter�L�[�A����Z�L�[�̏ꍇ
			Action();				//	�퓬�s������
		}else{
			gCursor = 1 - gCursor;	//	�J�[�\���ړ�
		}
		return;
	}

	if( gPhase == 3 ){
		Action();					//	�퓬�s������
		return;
	}

	if( gPhase == 4 ){
		CommandFight();				//	�퓬�R�}���h
		return;
	}

	if( gPhase == 5 ){
		gPhase = 6;
		AddExp( gEnemyType + 1 );	//	�o���l���Z
		SetMessage( "�G����������I", null );
		return;
	}

	if( gPhase == 6 ){
		gPhase = 0;					//	�}�b�v�ړ��t�F�[�Y
	}

	if( gPhase == 7 ){
		gPhase = 8;
		SetMessage( "���Ȃ��͎��S����", null );
		return;
	}

	if( gPhase == 8 ){
		SetMessage( "�Q�[���I�[�o�[", null );
		return;
	}

	gMessage1 = null;
}


//	�L�[����(UP)�C�x���g
window.onkeyup = function( ev )
{
	gKey[ ev.keyCode ] = 0;
}


//	�u���E�U�N���C�x���g
window.onload = function()
{
	LoadImage();

	gScreen = document.createElement( "canvas" );	//	���z��ʂ��쐬
	gScreen.width = WIDTH;							//	���z��ʂ̕���ݒ�
	gScreen.height = HEIGHT;						//	���z��ʂ̍�����ݒ�

	WmSize();										//	��ʃT�C�Y������
	window.addEventListener( "resize", function(){ WmSize() } );	//	�u���E�U�T�C�Y�ύX���AWmSize()���Ă΂��悤�w��
	setInterval( function(){ WmTimer() }, INTERVAL );		//	33ms�Ԋu�ŁAWmTimer()���Ăяo���悤�w���i��30.3fps�j
}
