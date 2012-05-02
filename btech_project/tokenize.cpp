#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

bool custom_sort(pair<string, int> a, pair<string, int> b) {
  return (a.second>=b.second);
}

int main() {
  string line;
  int i;
  ifstream myfile ("sample.txt");
  vector<string> words;
  map<string, int> wordcounts;
  map<string, int>::iterator w_iterator;
  
  vector <pair <string, int> > sorted_by_numbers;
  
  if (myfile.is_open())
  {
    while ( myfile.good() )
    {
      myfile>>line;
      words.push_back(line);
      ++wordcounts[line];
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 

  sort(words.begin(),words.end());
  
  for(w_iterator=wordcounts.begin(); w_iterator!=wordcounts.end(); w_iterator++) {
    sorted_by_numbers.push_back(make_pair((*w_iterator).first, (*w_iterator).second));
  }
  
  sort(sorted_by_numbers.begin(), sorted_by_numbers.end(), custom_sort);
  
  ofstream ofile;
  ofile.open("word-list.txt");
  
  if (ofile.is_open()) {
    for(i=0;i<sorted_by_numbers.size();i++) {
      ofile<<"{"<<sorted_by_numbers[i].first<<", "<<sorted_by_numbers[i].second<<"} ";
    }
  }
  else cout << "Unable to open file";

  ofile.close();
  
  return 0;
}