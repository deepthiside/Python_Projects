#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>
#include <windows.h>
#include <ctime>
#include <limits>
#include <sapi.h>  // For Text-to-Speech (TTS)
using namespace std;

struct Entry {
    string title;
    string description;
    string category;
};

vector<Entry> database;
vector<string> bannedWords = {"password", "hack", "violence", "secret", "illegal"};

string toLower(string str) {
    for (char &ch : str) ch = tolower(ch);
    return str;
}

bool isSensitive(string query) {
    string lowerQuery = toLower(query);
    for (string banned : bannedWords) {
        if (lowerQuery.find(toLower(banned)) != string::npos) return true;
    }
    return false;
}

void setColor(int color) {
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), color);
}

void speak(string text) {
    ISpVoice* pVoice = NULL;
    if (FAILED(::CoInitialize(NULL))) return;

    HRESULT hr = CoCreateInstance(CLSID_SpVoice, NULL, CLSCTX_ALL, IID_ISpVoice, (void **)&pVoice);
    if (SUCCEEDED(hr)) {
        wstring wtext(text.begin(), text.end());
        pVoice->Speak(wtext.c_str(), SPF_IS_NOT_XML, NULL);
        pVoice->Release();
    }
    CoUninitialize();
}

string getGreeting() {
    time_t now = time(0);
    tm *ltm = localtime(&now);
    int hour = ltm->tm_hour;
    if (hour < 12) return "Good Morning";
    else if (hour < 18) return "Good Afternoon";
    else return "Good Evening";
}

void showWeather() {
    setColor(9);
    cout << "\nToday's Weather Report:\n";
    cout << "----------------------------\n";
    cout << "Temperature: 32°C\n";
    cout << "Humidity: 58%\n";
    cout << "Condition: Partly Cloudy\n";
    cout << "Wind Speed: 10 km/h\n";
    cout << "----------------------------\n";
    speak("Here is today's weather report. It is partly cloudy with temperature 32 degrees Celsius.");
    setColor(7);
}

void showNews() {
    setColor(10);
    cout << "\nToday's Top News Headlines:\n";
    cout << "--------------------------------------------\n";
    cout << "1. Tesla opens first Mumbai showroom, brings Model Y (~₹42.75 lakh).\n";
    cout << "2. Axiom-4 crew undocked from ISS; splashdown at 3 PM IST.\n";
    cout << "3. Orange alert for heavy rains in Mumbai amid monsoon.\n";
    cout << "--------------------------------------------\n";
    speak("Here are today's top news headlines.");
    setColor(7);
}

void googleAnimation() {
    setColor(11);
    cout << "\n\nWelcome to BlinkBot!\n";
    string greeting = getGreeting();
    cout << greeting << endl;
    setColor(14);
    cout << "\nHey, How may I help you\n";
    for (int i = 0; i < 3; i++) {
        cout << ". ";
        Sleep(500);
    }
    speak("Welcome to BlinkBot. " + greeting + ". How may I help you?");
    cout << "\n--------------------------------------------\n";
    setColor(7);
}

void loadDefaultEntries() {
    database.push_back({"Taj Mahal", "Ivory-white marble mausoleum in Agra, India.", "Monument"});
    database.push_back({"Eiffel Tower", "Iconic iron tower in Paris, France.", "Monument"});
    database.push_back({"Google", "American tech company known for its search engine.", "Technology"});
    database.push_back({"ChatGPT", "AI chatbot developed by OpenAI.", "Technology"});
    database.push_back({"Stock Market", "Marketplace where stocks like Nifty & Sensex are traded.", "Finance"});
    database.push_back({"Social Marketing", "Strategies to promote products via social platforms.", "Marketing"});
    database.push_back({"Top News", "Latest breaking news from around the world.", "News"});
    database.push_back({"Anand International College of Engineering", "Renowned engineering college in Jaipur.", "Education"});
    database.push_back({"Sun", "The star at the center of our solar system.", "Astronomy"});
    database.push_back({"Moon", "Earth's only natural satellite.", "Astronomy"});
    database.push_back({"Planets", "Celestial bodies orbiting stars.", "Astronomy"});
    database.push_back({"Flowers", "Beautiful flowers like roses, tulips, lilies.", "Nature"});
    database.push_back({"Colors", "Vibrant colors like red, blue, yellow, etc.", "Art"});
}

void clearInputBuffer() {
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

void searchEntries() {
    clearInputBuffer();
    string query;
    setColor(10);
    cout << "\nEnter Search Keyword: ";
    getline(cin, query);
    setColor(7);

    if (isSensitive(query)) {
        setColor(12);
        cout << "\nSearch Blocked: Sensitive information detected!\n";
        speak("Search blocked. Sensitive information detected.");
        setColor(7);
        return;
    }

    string lowerQuery = toLower(query);
    if (lowerQuery.find("weather") != string::npos) {
        showWeather();
        return;
    }
    if (lowerQuery.find("news") != string::npos) {
        showNews();
        return;
    }

    vector<Entry> results;
    for (Entry &e : database) {
        if (toLower(e.title).find(lowerQuery) != string::npos || toLower(e.description).find(lowerQuery) != string::npos) {
            results.push_back(e);
        }
    }

    if (results.empty()) {
        setColor(12);
        cout << "\nNo matching entries found.\n";
        speak("No matching entries found.");
    } else {
        setColor(11);
        cout << "\nFound " << results.size() << " matching result(s):\n";
        speak("I found " + to_string(results.size()) + " results.");
        for (auto &res : results) {
            cout << "\nTitle: " << res.title << "\nDescription: " << res.description << "\nCategory: " << res.category << "\n";
            speak("Title: " + res.title + ". Description: " + res.description);
        }
    }
    setColor(7);
}

void showMenu() {
    setColor(13);
    cout << "\n1. Search Entry";
    cout << "\n2. Exit\n";
    setColor(7);
}

int main() {
    googleAnimation();
    loadDefaultEntries();
    int choice;
    do {
        showMenu();
        cout << "\nEnter your choice: ";
        cin >> choice;

        if (cin.fail()) {
            setColor(12);
            cout << "\nInvalid input. Please enter a number.\n";
            speak("Invalid input. Please enter a number.");
            setColor(7);
            clearInputBuffer();
            continue;
        }

        switch (choice) {
            case 1: searchEntries(); break;
            case 2: 
                setColor(14); 
                cout << "\nThank you for visiting. Have a great day!\n"; 
                speak("Thank you for visiting. Have a great day!"); 
                setColor(7); 
                break;
            default: 
                setColor(12); 
                cout << "\nInvalid choice, try again.\n"; 
                speak("Invalid choice. Try again."); 
                setColor(7);
        }
    } while (choice != 2);

    return 0;
}
