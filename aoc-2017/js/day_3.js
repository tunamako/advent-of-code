var input = 361527;
var ringDim = 1;
while(ringDim * ringDim < input) {
	ringDim += 2;
}

for(var i = 0; i <= 4; i++) {
	var wah = Math.abs(ringDim * ringDim - i*(ringDim-1) - input);
	if(wah <= Math.floor((ringDim-1)/2)) {
		console.log(ringDim-1-wah);
	}
}

