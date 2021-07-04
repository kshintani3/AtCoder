#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

string enum_divisors(long long N) {
    string res;
    int odd = 0;
    int even = 0;
    string out;
    for (long long i = 1; i * i <= N; ++i) {
        if (N % i == 0) {
            if(N%2 == 0){even += 1;}
            else{odd += 1;}
            if (N/i != i){
                if((N/i)%2 == 0){even += 1;}
                else{odd += 1;}
            };
        }
    }
    if(odd < even){out = "Even";}
    else if(odd > even){out = "Odd";}
    else{out = "Same";}
    return out;
}

int main(void){
    int n;
    cin >> n;
    int l,i=0,a[n];
    string out;
    for (int i = 0; i < n; i++){
        cin >> a[i];
        out = enum_divisors(a[i]);
        cout << out<< endl;
    }
}

