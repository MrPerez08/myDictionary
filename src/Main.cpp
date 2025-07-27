// This file should do all of the word checking making sure all the words are: 
// 1. spelled correctly (using some AI model to check over the array of words)
// 2. words are capitalized
// 3. remove duplicate words
// 4. correctly sort (for later use (basically creating my own dictionary))
//   4a. creating word trees with the morpheme at the top with a words different forms branching using prefixes, suffixes and use of tense
// 5. for future refernce (another file should do this) for coumpounded words (using - 'dash or when two words alters the definition of both words when placed together 
//a collection should be created to showcase the compounded words EVEN IF both words already show up in the vocab list. (ex. rigor mortus))
//sidenote: make it insanely safe brotato chip! throw them exceptions using try and catch brotein shake!


/*
1. User should be able to EITHER copy paste their vocab words into a text area OR drag&drop a txt file or of the sort.
2. program should ask user what separates the different vocab words (do they separate with a comma? a period? a line?)
3. program compiles and gives the user the option to add additional words to the list
*/



#pragma comment(lib, "libhunspell.lib")  // Windows-only shortcut
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <memory>
#include <cctype>
#include <unordered_set>
#include <hunspell/hunspell.hxx>


void readFile(const std::string& filename){
    std::ifstream inputFile(filename);
    if(!inputFile.is_open()){
        throw std::runtime_error("Failed to open file: testing.txt");
    }
    char separator;
    std::cout << "By Line: 'L', By character: 'character'" << std::endl; //THIS IS THE DETERMINER OF WHAT SEPERATES THE VOCAB WORDS!!!
    std::cin >> separator;

    std::vector<std::string> localWordList;
    std::string currentWord;

    //both of these functions should return the same yummy looking vector
    //IMPLEMENT CAPITALIZATION AND/OR SPELL CHECKING FUNCTIONS!!!!
    if(separator=='L'){
        std::string line;
        while (std::getline(inputFile,line)){
            std::string finalLine;
            if (!line.empty()) {
                for(char c : line){
                    if(isalpha(c)){finalLine+=c;}
                }
                localWordList.push_back(finalLine);
            }
        }
    }
    else{
        char ch;
        while(inputFile.get(ch)){
            if(ch==separator){
                if(!currentWord.empty()){
                    localWordList.push_back(currentWord);
                    currentWord.clear();
                }
            } 
            else if (!isalpha(ch)){continue;}
            else{currentWord += ch;}
        }
        if(!currentWord.empty()){
            localWordList.push_back(currentWord);
        }
    }
    inputFile.close();
    

    for(int i = 0;i<localWordList.size();i++){localWordList[i][0]=toupper(localWordList[i][0]);}//Capitalizes the first letter of all words in the localWordList vector variable
    

    //Check spelling for all words in vector
    // Check spelling for all words in vector
    Hunspell hunspell("en_US.aff", "en_US.dic");
    for(const auto& vocabWord : localWordList) {
        // New non-deprecated spell check
        if(hunspell.spell(vocabWord) == 0) {  // Returns 0 if misspelled
            std::cout << "Misspelled word: " << vocabWord << std::endl;
            
            // Modern way to get suggestions
            std::vector<std::string> suggestions = hunspell.suggest(vocabWord);
            
            if (!suggestions.empty()) {
                std::cout << "  Suggestions (" << suggestions.size() << "): ";
                for (size_t j = 0; j < suggestions.size() && j < 5; j++) {
                    std::cout << suggestions[j];
                    if (j < suggestions.size()-1 && j < 4) std::cout << ", ";
                }
                std::cout << "\n";
            }
        }
    }


    //The next three lines allow for the removal of duplicate words
    std::unordered_set<std::string> seen;
    auto new_end = std::remove_if(localWordList.begin(), localWordList.end(),[&seen](const std::string& word) {return !seen.insert(word).second;});
    localWordList.erase(new_end, localWordList.end());


    //Allow for sorting decision (keep same, alphabetical ascending/descending random)



    for (const auto& word : localWordList){
        std::cout << word << std::endl;
    }
}

int main(){
    try{
        

        readFile("testin.txt");
    }
    catch(const std::exception& e){std::cerr << "EROOR IN BUNGHOLE wgat it is->"<< e.what() << std::endl;return 1;}
    return 0;
}