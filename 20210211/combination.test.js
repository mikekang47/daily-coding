//2. 숫자카드가 모여있을 때 조합해서 나올 수 있는 모든 수 반환하는 함수
//모든 n개짜리 값을 더해 반환하는 함수 accumulator => 완료
//n개짜리 값을 각각 구하는 함수 n개짜리 => 
 
function combination(cards) {
  let sum = 1;
    function recursion(n){
      if (n == 0) {
        return sum;
      }
      else if(n > 0) {
        sum *= (cards.length -(n-1));
        return recursion(n-1);
      }
    }
  
    function n개짜리(n) {
      return recursion(n);
    }

    let sumRe = 0;
    function accumulator(n) {
      for(let i = 1; i <= n; i++) {
        sumRe += recursion(i);
      }
      return sumRe;
    }
  
   return accumulator(cards.length);
  }
  
  test('combination', () => {
    expect(combination([1,4])).toBe(4);
    // expect(combination([0,4])).toBe(3);
    expect(combination([1,4,6])).toBe(15);
    //1,4,6,14,41,46,64,16,61,146,164,416,461,614,641
  });