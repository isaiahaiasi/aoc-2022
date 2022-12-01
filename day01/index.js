import { readFile } from 'fs/promises';

async function getInputData(path = 'input.txt') {
	return readFile(path).then(fileBuffer => fileBuffer.toString());
}

function getSums(rawData) {
	const elves = rawData.split('\n\n').map(elf => elf.split('\n'));
	return elves.map(elf => elf.reduce((a, n) => a + +n, 0));
}

async function main() {
	const input = await getInputData(process.argv[2]);

	const sums = getSums(input);

	// part 1
	const maxSum = Math.max(...sums);
	console.log("Part 1:\t" + maxSum);

	// part 2
	const [a, b, c, ..._rest] = sums.sort((a, b) => b - a);
	const topThreeSum = a + b + c;
	console.log("Part 2:\t" + topThreeSum);
}

main();
