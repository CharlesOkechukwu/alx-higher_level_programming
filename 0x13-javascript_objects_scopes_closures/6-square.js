#!/usr/bin/node
const Parent = require('./5-square');

module.exports = class Square extends Parent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    if (this.width > 0 && this.height > 0) {
      for (let i = 0; i < this.height; i++) {
        let str = '';
        for (let j = 0; j < this.width; j++) {
          str += c;
        }
        console.log(str);
      }
    }
  }
};
