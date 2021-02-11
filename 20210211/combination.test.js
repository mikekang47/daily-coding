//2. 숫자카드가 모여있을 때 조합해서 나올 수 있는 모든 수 반환하는 함수
 
function combination(cards) {
    function n개짜리(n) {
      if(n == 1) {
       return cards.length;
      }
      if(n == 2) {
        return  cards.length*(cards.length-1);
      } 
      if(n == 3) {
        return cards.length*(cards.length-1)*(cards.length-2);
      }
      
      else {
        return null;
      }
    }
  
    function accumulator(n) {
      return n개짜리(1) + n개짜리(2) + n개짜리(3);
    }
  
    return  accumulator(3);
  }
  
  test('combination', () => {
    expect(combination([1,4])).toBe(4);
    expect(combination([1,4,6])).toBe(15);
    //1,4,6,14,41,46,64,16,61,146,164,416,461,614,641
  });