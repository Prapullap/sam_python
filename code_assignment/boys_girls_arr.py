def can_arrange_students(boys, girls):
    boys.sort()
    girls.sort()

    if boys[0] > girls[0]:
        longer, shorter = boys, girls
    else:
        longer, shorter = girls, boys

    arrangement = []
    for i in range(len(boys)):
        arrangement.append(shorter[i])
        arrangement.append(longer[i])

    for i in range(1, len(arrangement)):
        if arrangement[i] < arrangement[i - 1]:
            return "NO"
    
    return "YES"

def main():
    test_cases = []
    num_tests = int(input("Enter the number of test cases: "))
    
    for _ in range(num_tests):
        num_students = int(input("Enter the number of boys and girls (should be the same): "))
        
        boys = list(map(int, input("Enter the heights of boys: ").split()))
        girls = list(map(int, input("Enter the heights of girls: ").split()))
        
        test_cases.append((boys, girls))
    
    results = []
    for boys, girls in test_cases:
        result = can_arrange_students(boys, girls)
        results.append(result)
    
    for result in results:
        print(result)


main()
