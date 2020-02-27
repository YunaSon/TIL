class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    
    def getName(self):
        return self.name

    def getHours(self):
        return self.hours
    
    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours


def makeStudent(infoStr):
    # infoStr은 다음 각 요소가 탭으로 구분된 한 줄이다: name, hours, qpoints
    # 이에 해당하는 Student 객체를 리턴한다.
    name, hours, qpoints = infoStr.split(" ")
    return Student(name, hours, qpoints)

def main():
    # 입력 파일을 읽기 모드로 연다. 
    filename = input("Enter name the grade file: ")
    infile = open(filename, 'r')

    # best의 값을 파일 내 첫 번째 학생을 가리키도록 한다.
    best = makeStudent(infile.readline())

    # 파일의 나머지 줄을 처리한다.
    for line in infile:
        # 읽어 들인 줄을 학생 레코드로 변환한다.
        s = makeStudent(line)
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    print("The best student is: ", best.getName())
    print("hours: ", best.getHours())
    print("GPA: ", best.gpa())

if __name__ == '__main__':
    main()