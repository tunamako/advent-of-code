function maxIndex(anArray) {
	return anArray.reduce((iMax, next, i, arr)=>{
		return next > arr[iMax]
			? i 
			: iMax;
	}, 0)
}

function isIdentical(a, b) {
	return a.reduce((curr, next, i)=>{
		return curr && next == b[i];
	}, true)
}

var input = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11];
var config = input.slice();
var seenConfigs = [];
var redisCount = 0;

while(true) {
	redisCount += 1

	var iMax = maxIndex(config);
	var blocks = config[iMax];
	config[iMax] = 0;

	var i = iMax == config.length -1
		? 0
		: iMax + 1;

	for(i; blocks > 0; i++){
		blocks -= 1;
		config[i] += 1;
		if(i == config.length - 1) {
			i = -1;
		}
	}

	for(var i in seenConfigs) {
		if(isIdentical(config, seenConfigs[i])){
			console.log(redisCount);
			process.exit();
		}
	}

	seenConfigs.push(config.slice());
}