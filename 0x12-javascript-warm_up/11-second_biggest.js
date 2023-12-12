#!/usr/bin/node
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  let largeNum = parseInt(process.argv[2]);
  let second = parseInt(process.argv[2]);
  for (let i = 2; i < len; i++) {
    if (largeNum > parseInt(process.argv[i])) {
      if (second <= parseInt(process.argv[i])) {
        second = parseInt(process.argv[i]);
      }
    } else {
      largeNum = parseInt(process.argv[i]);
    }
  }
  console.log(second);
}
