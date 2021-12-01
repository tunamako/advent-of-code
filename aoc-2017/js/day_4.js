var fs = require('fs');
var input = fs.readFileSync('inputs/day_4', 'utf8').split("\n");

function anagram(a, b) {
	var tempA = a.split('').sort().join('');
	var tempB = b.split('').sort().join('');
	return tempA == tempB;
}

function isValid(aString) {
	aString = aString.split(" ");
	for(var i = 0; i < aString.length; i++) {
		for(var j = i + 1; j < aString.length; j++) {
			if(anagram(aString[i], aString[j])) {
				console.log(aString);
				return 0;
			}
		}
	}
	return 1;
}

var validCount = input.reduce((curr,next)=>{
	return curr + isValid(next);
}, 0);	


console.log(validCount);
console.log(anagram("abc", "cba"));