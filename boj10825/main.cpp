#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Student {
private:
    string name;
    int korean;
    int english;
    int math;
public:
    int getKorean();

    int getEnglish();

    int getMath();

    string getName();

    Student(string name, int korean, int english, int math) {
        this->name = name;
        this->korean = korean;
        this->math = math;
        this->english = english;
    }
};

int Student::getEnglish() {
    return this->english;
}

int Student::getKorean() {
    return this->korean;
}

int Student::getMath() {
    return this->math;
}

string Student::getName() {
    return this->name;
}

bool cmp(Student s1, Student s2) {
    if (s1.getKorean() == s2.getKorean() && s1.getEnglish() == s2.getEnglish() && s1.getMath() == s2.getMath()) {
        return s1.getName() < s2.getName();
    } else if(s1.getKorean() == s2.getKorean() && s1.getEnglish() == s2.getEnglish()){
        return s1.getMath() > s2.getMath();
    } else if(s1.getKorean() == s2.getKorean()){
        return s1.getEnglish() < s2.getEnglish();
    } else {
        return s1.getKorean() > s2.getKorean();
    }
}


int n;
int kr, en, math;
vector<Student> students;
string name;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> name >> kr >> en >> math;
        Student st = Student(name, kr, en, math);
        students.push_back(st);
    }
    sort(students.begin(), students.end(), cmp);
    for (Student s: students) {
        cout << s.getName() << "\n";
    }
    return 0;
}
