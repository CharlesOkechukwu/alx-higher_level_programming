#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let occur = 0;
  for (let i = 0; i < len; i++) {
    if (list[i] === searchElement) {
      occur += 1;
    }
  }
  return occur;
};
