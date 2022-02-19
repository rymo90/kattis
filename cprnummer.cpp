#include <iostream>
#include <string>
#include <sstream>
using namespace std;
int main (){
  string pcr = "432765-4321" ;
  string n ;
  cin >> n ;

  long  num = 0;
  for (int i = 0; i < pcr.size(); i++) {
    int tmp  = 0;
    int tmp2 = 0;
    stringstream bb;
    stringstream ss;
    if (i == 6) {
      continue;
    }else{
      ss << pcr[i];
      bb << n[i];
      ss >> tmp;
      bb >> tmp2;
      num += (tmp*tmp2);
    }

  }
  if (num%11==0) {
    cout << 1 << endl;
  }else{
    cout << 0 << endl;
  }


  return 0;
}
