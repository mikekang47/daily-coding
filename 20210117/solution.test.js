test('solution', () => {
    const solution = require('./solution');

    const n = 3;

    expect(solution(n)).toBe('수박수');
    expect(solution(4)).toBe('수박수박');

})