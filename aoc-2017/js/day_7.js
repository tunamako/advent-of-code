var rawInput = require('fs').readFileSync('inputs/day_7', 'utf8').split("\n");

input = rawInput.reduce((total, next) => {
	next = next.split(" -> ");
	var name = next[0].split(" ")[0];
	var weight = Number(next[0].split(" ")[1].slice(1, -1));
	var carrying = next.length > 1
		? next[1].split(", ")
		: [];

	total[name] = {};
	total[name]["weight"] = weight;
	total[name]["carrying"] = carrying;
	return(total);
}, {});



function fillTreeFrom(name) {
	var carrying = input[name]["carrying"];
	if(carrying.length == 0)
		return 1;
	return carrying.reduce((curr, next) =>{
			return curr + fillTreeFrom(next);
		}, 1);
}

var totalNameCount = Object.keys(input).length;
var rootname = "";

for(var name in input) {
	if(input[name]["carrying"].length == 0)
		continue;
	if(fillTreeFrom(name) == totalNameCount){
		rootname = name;
		break;
	}
}

function adjustWeightFor(name) {
	var carryweights = input[name]["carrying"].map(x => input[x]["weight"]);
	console.log(carryweights)
	var subSum = 0;




	if(carrying.length == 0)
		return -1;
	if(carrying.length == 2) {
		if(carrying[0] == carrying[1])
			return -1;
		return adjustWeightFor(carrying[0]);
	}
	if(carrying.length == 3) {

	}
	
}



console.log(adjustWeightFor(rootname));