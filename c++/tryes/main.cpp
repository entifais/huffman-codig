#include <string>
#include <map>
#include <vector>
#include <iostream>
using namespace std;
map<int, int> numL(vector<int> &longitudes){
	map<int, int> table;
	for(int i=0;i<longitudes.size();i++){
		if(table.find(longitudes[i])!=table.end()){
			table[longitudes[i]]=table[longitudes[i]]+1;
		}
		else{
			table[longitudes[i]]=1;
		}
	}
	return table;
}

map<char, int> getprob(string text){
	map<char, int> table;
	for(int i=0;i<text.length();i++){
		char character=text.at(i);
		if (table.find(character)!=table.end()){
			table[character]=1;
		}
		else{
			table[text[i]]=table[text[i]]+1;
		}
	}
	return table;
}

void heapify(vector<int> &A, int n){
    while(n>0 && A[A[n]]<A[A[((int)(n-1)/2)]]){
    	int tmp= A[n];
        A[n] = A[(int)((n-1)/2)];
        A[(int)((n-1)/2)] = tmp;
        n = (int)((n-1)/2);
    }
}
void build_heap(vector<int> &A,int n){
    int element = 1;
    while (element < n){
        heapify(A, element);
        element = element + 1;
    }
}
void sift(vector<int> &A,int n){
    int base = 0;
    int minimo = base;
    while (base < n){ 
        if (2*base + 1 < n && A[A[2*base+1]] < A[A[minimo]]){
        	minimo = 2*base+1;
        }
        if (2*base+2 < n &&  A[A[2*base+2]] < A[A[minimo]]){
            minimo = 2*base+2;
        }
        if (base != minimo){
            int tmp =A[base];
            A[base] = A[minimo];
            A[minimo] = tmp;
            base = minimo;
        }
        else{
            base = n; 
        }
    } 
}
vector<int> codeLengh(vector<int> &table){
    int m1,m2;
    int n = table.size();
    vector<int> A(2*n,0); //[0] * (2*n)
    int i = 0;
    while (i < n){
        A[i] = n + i;
        A[n+i] = table[i];
        i = i + 1;
    }
    build_heap(A, n);
    int h = n-1;
    while (h > 0){
        m1 = A[0];
        A[0] = A[h];
        h = h - 1;
        sift(A,h);
        m2 = A[0];
        A[h+1] = A[m1]+A[m2];
        A[0] = h+1;
        A[m1] = h + 1;
        A[m2] = h+1;
        sift(A, h);
    }    
    A[1] = 0;
    i = 2;
    while (i < 2*n){
        A[i] = A[A[i]]+1;
        i = i + 1;
    	}
    
    return A;
}

vector<char> getKeys(map<char, int> &tablaOriginal){
	vector<char> keys;
	for(map<char,int>::iterator it = tablaOriginal.begin(); it != tablaOriginal.end(); ++it) {
		keys.push_back(it->first);
	}	
	return keys;
}
vector<int> getValues(map<char, int> &tablaOriginal){
	vector<int> values;
	for(map<char,int>::iterator it = tablaOriginal.begin(); it != tablaOriginal.end(); ++it) {
		values.push_back(it->second);
	}	
	return values;
}
vector<int> getValues(map<int, int> &tablaOriginal){
    vector<int> values;
    for(map<int,int>::iterator it = tablaOriginal.begin(); it != tablaOriginal.end(); ++it) {
        values.push_back(it->second);
    }   
    return values;
}
void printMap(map<int, int> &tablaOriginal){
    for(map<int, int>::iterator it = tablaOriginal.begin(); it != tablaOriginal.end(); ++it) {
        cout<<it->first<<it->second<<endl;
    }   
}

int main(){
	map<char, int> tablaOriginal = getprob("velezrestrepoarangosohmpolancorodriguez");
	vector<char> simbolos = getKeys(tablaOriginal);
	vector<int> tabla = getValues(tablaOriginal);
	vector<int> A = codeLengh(tabla);
	int i = 0;
	while (i < simbolos.size()){
    		cout<<simbolos[i]<<": "<<A[simbolos.size()]<<": "<<A[simbolos.size()+i]<<endl;
    		cout<<""<<endl;
    		i = i + 1;
    	}
    map<int, int> numldata=numL(A);
    printMap(numldata);
	return 0;
}