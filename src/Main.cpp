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
#include <hunspell/hunspell.hxx>

class VocabularyProcessor{
    private:
    std::unique_ptr<Hunspell> spellChecker;

    public:
        VocabularyProcessor(const std::string& affPath, const std::string& dicPath) {
        spellChecker = std::make_unique<Hunspell>(affPath.c_str(), dicPath.c_str());
    }

    bool isSpelledCorrectly(const std::string& word) {
        return spellChecker->spell(word);
    }

    std::vector<std::string> getSuggestions(const std::string& word) {
        return spellChecker->suggest(word);
    }
};



void checkWords(VocabularyProcessor& processor, const std::vector<std::string>& words) {
    for (const auto& word : words) {
        if (processor.isSpelledCorrectly(word)) {
            std::cout << word << " - Correct\n";
        } else {
            std::cout << word << " - Incorrect\n";
            auto suggestions = processor.getSuggestions(word);
            if (!suggestions.empty()) {
                std::cout << "  Suggestions:\n";
                for (const auto& sug : suggestions) {
                    std::cout << "  - " << sug << "\n";
                }
            }
        }
    }
}



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
            if (!line.empty()) {
                localWordList.push_back(line);
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
            } else{
                currentWord += ch;
            }
        }
        if(!currentWord.empty()){
            localWordList.push_back(currentWord);
        }
    }
    inputFile.close();
    

    for (const auto& word : localWordList){
        std::cout << word << std::endl;
    }
}

int main(){
    try{
        #ifdef _WIN32
        const std::string affPath = "en_US.aff";
        const std::string dicPath = "en_US.dic";
        #else
        const std::string affPath = "/usr/share/hunspell/en_US.aff";
        const std::string dicPath = "/usr/share/hunspell/en_US.dic";
        #endif

        VocabularyProcessor processor(affPath, dicPath);

        readFile("testin.txt");
    }
    catch(const std::exception& e){std::cerr << "EROOR IN BUNGHOLE wgat it is->"<< e.what() << std::endl;return 1;}
    return 0;
}