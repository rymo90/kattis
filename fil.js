let quoteSample = "The five boxing wizards jump quickly.";
let alphabetRegexV2 = /\W+/gi; // Change this line
let result = quoteSample.match(alphabetRegexV2).length;
console.log(result);
