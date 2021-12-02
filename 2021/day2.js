// https://adventofcode.com/2021/day/2#part1

function readFile(fileName) {
    var fs = require('fs');
    var file = fs.readFileSync(fileName, 'utf8');
    return file;
}

class Submarine {
    constructor() {
        this.position = 0;
        this.depth = 0;
    }

    down(y) {
        this.depth += y;
    }

    up(y) {
        this.depth -= y;
    }

    forward(x) {
        this.position += x;
    }

    getResult() {
        return this.position * this.depth;
    }
};

const submarine = new Submarine();
readFile('2021/resources/day2.1.txt').split('\n').forEach(line => {
    const matches = line.matchAll(/^(\w+) (\d+)/g);
    for (const match of matches) {
        eval(`submarine.${match[1]}(${match[2]})`);
    }
});

console.info(submarine.getResult());


// https://adventofcode.com/2021/day/2#part2

class Submarine2 extends Submarine {
    constructor() {
        super();
        this.aim = 0;
    }

    down(y) {
        //super.down(y);
        this.aim += y;
    }

    up(y) {
        //super.up(y);
        this.aim -= y;
    }

    forward(x) {
        super.forward(x);
        this.depth += this.aim * x;
    }
}

const submarine2 = new Submarine2();
readFile('2021/resources/day2.2.txt').split('\n').forEach(line => {
    const matches = line.matchAll(/^(\w+) (\d+)/g);
    for (const match of matches) {
        eval(`submarine2.${match[1]}(${match[2]})`);
    }
});

console.info(submarine2.getResult());