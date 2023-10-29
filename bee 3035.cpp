#include<iostream>
#include<algorithm>

using namespace std;

int main(){
int n, move, pos[3] ={0, 0, 0};
char coin;

cin >> n;
cin >> coin;
pos[pos - 65] = 1;

while(n > 0){
    cin >> move;
    switch(move){
    case 1:
        if(pos[0] || pos[1] == 1)
            swap(pos[0], pos[1])
        break;
    case 2:
        if(pos[1] || pos[2] == 1)
            swap(pos[1], pos[2])
        break;
    case 3:
        if(pos[2] || pos[0] == 1)
            swap(pos[0], pos[2])
        break;

    }
    n--;
}

if(pos[0] == 1)
    cout << "A" << endl;
else
    if(pos[1] == 1)
        cout << "B" << endl;
    else
       cout << "C" << endl;


return 0;

}
