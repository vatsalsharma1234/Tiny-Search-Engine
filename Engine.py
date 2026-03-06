#include <iostream>
#include <unordered_map>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

class TinySearchEngine {
private:
    unordered_map<string, vector<pair<int,int>>> index;

public:

    void addDocument(int docID, const string &text) {

        unordered_map<string,int> freq;
        stringstream ss(text);
        string word;

        while (ss >> word) {
            freq[word]++;
        }

        for (auto &p : freq) {
            index[p.first].push_back({docID, p.second});
        }
    }

    vector<pair<int,int>> search(const string &word) {

        vector<pair<int,int>> result;

        if(index.find(word) != index.end()) {
            result = index[word];
        }

        // Rank documents by frequency
        sort(result.begin(), result.end(),
            [](const pair<int,int> &a, const pair<int,int> &b){
                return a.second > b.second;
            });

        return result;
    }

    void printResults(const vector<pair<int,int>> &results) {

        if(results.empty()){
            cout << "No documents found\n";
            return;
        }

        for(const auto &r : results){
            cout << "Document " << r.first 
                 << " (frequency: " << r.second << ")\n";
        }
    }
};

int main() {

    TinySearchEngine engine;

    engine.addDocument(1, "data structures and algorithms");
    engine.addDocument(2, "search engine using inverted index");
    engine.addDocument(3, "algorithms and data science");

    string query;

    cout << "Enter search word: ";
    cin >> query;

    vector<pair<int,int>> results = engine.search(query);

    cout << "\nSearch Results:\n";
    engine.printResults(results);

    return 0;
}
