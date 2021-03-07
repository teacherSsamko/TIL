def plusMinus(i, numbers, target, answer, total):
    if len(numbers) == i:
        if total == target:
            return answer + 1
        else:
            return answer
    else:
        total += numbers[i]
        answer = plusMinus(i + 1, numbers, target, answer, total)
        total -= 2 * numbers[i]
        answer = plusMinus(i + 1, numbers, target, answer, total)
        return answer


if __name__ == '__main__':
    numbers = list(map(lambda x: int(x), input().split()))
    target = 0
    answer = 0
    total = 0
    i = 0
    print(plusMinus(i, numbers, target, answer, total))


"""
const solution = (numbers) => {
    const target = 0;
    let answer = 0;
    let sum = 0;
    let idx = 0;
    function plusMinus(i,numbers,target,answer,sum) {
	    if(numbers.length === i && sum===target){
		    return answer+1;
	    }else if(numbers.length === i){
    		return answer;
	    }else{
          sum += numbers[i];
          answer = plusMinus(i+1,numbers,target,answer,sum);
          sum -= 2*numbers[i];
          answer = plusMinus(i+1,numbers,target,answer,sum);
          return answer;
        }
    }
  answer = plusMinus(idx,numbers,target,answer,sum);
  return answer;
}
"""
