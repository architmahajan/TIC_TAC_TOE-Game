#include<iostream>
using namespace std;
#include<bits/stdc++.h>
enum{NOUGHTS,CROSSES,BORDER,EMPTY};
enum{HumanWin,CompWin,Draw};
int board[25];
const int convertTo25[]={
	6,7,8,
	11,12,13,
	16,17,18
};
const int directions[4]={1,5,4,6};
int middle=4;
int corner[4]={0,2,6,8};
int ply=0;
int positions=0;
int maxply=0;
int getnumfordir(int startsq,const int dir,const int *board,const int us)
{
	int found=0;
	while(board[startsq]!=BORDER)
	{
		if(board[startsq]!=us)
			break;
		found++;
		startsq+=dir;
	}
	return found;
}
int findthreeinarow(const int *board,const int ourindex,const int us)
{
	int dirindex=0;
	int dir=0;
	int threecount=1;
	for(dirindex=0;dirindex<4;++dirindex)
	{
		dir=directions[dirindex];
		threecount+=getnumfordir(ourindex+dir,dir,board,us);
		threecount+=getnumfordir(ourindex+(dir*(-1)),dir*(-1),board,us);
		if(threecount==3)
		{
			break;
		}
		threecount=1;
	}
	return threecount;
}
int findthreeinarowallboard(const int *board,const int us)
{
	int threefound=0;
	int i;
	for(i=0;i<9;i++)
	{
		if(board[convertTo25[i]]==us)
		{
			if(findthreeinarow(board,convertTo25[i],us)==3)
			{
				threefound=1;
				break;
			}
		}
	}
	return threefound;
}
int evalforwin(const int *board,const int us)
{
	if(findthreeinarowallboard(board,us)!=0)
		return 1;
	if(findthreeinarowallboard(board,us^1)!=0)
		return -1;
	return 0;
}
int minmax(int *board,int side)
{
	//cout<<"X\n";
	int movelist[9];
	int movecount=0;
	int bestscore=-2;
	int score=-2;
	int bestmove=-1;
	int move;
	int i;
	if(ply>maxply)
		maxply=ply;
	positions++;
	if(ply>0)
	{
		score=evalforwin(board,side);
		if(score!=0)
			return score;
	}
	for(i=0;i<9;i++)
	{ 
		//cout<<board[convertTo25[i]]<<" ";
		if(board[convertTo25[i]]==EMPTY)
		{
			movelist[movecount++]=convertTo25[i];
		}
	}
	for(i=0;i<movecount;i++)
	{
		move=movelist[i];
		board[move]=side;
		ply++;
		score=-minmax(board,side^1);
		//cout<<score<<"\n";
		if(score>bestscore)
		{
			bestscore=score;
			bestmove=move;
		}
		board[move]=EMPTY;
		ply--;
	}
	if(movecount==0)
	{
		bestscore=findthreeinarowallboard(board,side);
	}
	if(ply!=0)
		return bestscore;
	else
		return bestmove;
}
void initialise(int *board)
{
	int i;
	for(i=0;i<25;i++)
		board[i]=BORDER;
	for(i=0;i<9;i++)
		{
			board[convertTo25[i]]=EMPTY;
			
		}
}
void printboard(int *board)
{
	int i;
	char pceChars[]="OX|-";

    for(i=0;i<9;i++)
		{
			if(i!=0 && i%3==0)
				printf("\n");
			printf("%4c",pceChars[board[convertTo25[i]]]);
		}	
		printf("\n");
}
int Hasempty(const int *board)
{
	int index =0;
	for(index=0;index<9;++index)
	{
		if(board[convertTo25[index]]==EMPTY)
			return 1;
	}
	return 0;
}
int getnextbest(const int *board)
{
	int ourmove=convertTo25[middle];
	if(board[ourmove]==EMPTY)
	{
		return ourmove;
	}
	int i=0;
	ourmove=-1;
	for(i=0;i<4;i++)
	{
		ourmove=convertTo25[corner[i]];
		if(board[ourmove]==EMPTY)
			break;
		ourmove=-1;
	}
	return ourmove;
}
int getwinningmove(int *board,const int side)
{
	int ourmove=-1;
	int winmove=0;
	int i =0;
	for(i=0;i<9;i++)
	{
		if(board[convertTo25[i]]==EMPTY)
		{
			ourmove=convertTo25[i];
			board[ourmove]=side;
			if(findthreeinarow(board,ourmove,side)==3)
				winmove=1;
			board[ourmove]=EMPTY;
			if(winmove==1)
				break;
			ourmove=-1;
		}
	}
	return ourmove;
}
int getcomputermove(int *board,int side)
{
	/*int i=0;
	int numfree=0;
	int avai[9];
	int randommove=0;
	randommove=getwinningmove(board,side);
	if(randommove!=-1)
	{
         return randommove;
	}
	randommove=getwinningmove(board,side^1);
	if(randommove!=-1)
	{
         return randommove;
	}
	randommove=getnextbest(board);
	if(randommove!=-1)
	{
         return randommove;
	}
	for(i=0;i<9;i++)
	{
		if(board[convertTo25[i]]==EMPTY)
		{
			avai[numfree++]=convertTo25[i];
		}
	}
	randommove=(rand()%numfree);
	return avai[randommove];*/
	ply=0;
	positions=0;
	maxply=0;
	int best = minmax(&board[0],side);
	//printf("Finished searching positions:%d maxdepth:%d bestmove:%d\n",positions,maxply,best);
	return best;
}

int gethumanmove(const int *board)
{
	char userinput[4];
	int moveok=0;
	int move=-1;
	while(moveok==0)
	{
		cout<<"Enter the move from 1 to 9\n";
		cin>>move;
        if(move<1 || move>9)
        {
        	move=-1;
        	printf("InvalidRange\n");
        	continue;
        }
        move--;
        if(board[convertTo25[move]]!=EMPTY)
        {
        	move=-1;
        	printf("Square Not Available\n");
        	continue;
        }
        moveok=1;
	}
	return(move);
}
void Makemove(int *board ,const int sq,const int side)
{
	board[sq]=side;
}
int rungame()
{
	int gameover= 0;
	int side=NOUGHTS;
	//int side=CROSSES;
	int lastmovemade=0;
	initialise(board);
	printboard(&board[0]);
            
	while(!gameover)
	{
		if(side==NOUGHTS)
		{
			
            lastmovemade=gethumanmove(&board[0]);
            cout<<"Human ";
			printf("Making Move = %d\n",lastmovemade);
            Makemove(&board[0],lastmovemade,NOUGHTS);
            side=CROSSES;
		}
		else
		{
			
			lastmovemade=getcomputermove(&board[0],side);
			cout<<"Computer ";
			printf("Making Move = %d\n",lastmovemade);
            Makemove(&board[0],lastmovemade,CROSSES);
          side=NOUGHTS;
		}
		//printboard(&board[0]);
		if(findthreeinarow(&board[0],lastmovemade,side^1)==3)
		{
            printf("Gameover\n");
            gameover=1;
            if(side==NOUGHTS)
            {
            	printf("Computer Wins\n");
            }
            else
            {
            	printf("Human Wins\n");
            }
		}
		if(!Hasempty(&board[0]))
		{
			printf("gameover\n");
			gameover=1;
			printf("Draw\n");
		}
	}
}
int main(int argc ,char * argv[]) 
{

    	string str=argv[1];
    	//cout<<str<<"\n";
    	initialise(&board[0],str);
    	int move=rungame();
    	if(move/5==1)
    		move-=5;
    	else if(move/5==2)
    		move-=7;
    	else if(move/5==3)
    		move-=9;
    	printf("%d",move);
}
int main()
{
	srand(time(NULL));
	rungame();
}