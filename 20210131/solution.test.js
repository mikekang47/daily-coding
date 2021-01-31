function solution(array) {

    const sortedArray = array.sort((a, b) => `${b}${a}`-`${a}${b}`);
    return sortedArray.join("").toString();
    }
    
    test('solution', () => {
      expect(solution([6, 10, 2])).toBe("6210");
      expect(solution([1, 9, 0])).toBe("910");
      expect(solution([3, 30, 34, 9, 5])).toBe("9534330");
    })