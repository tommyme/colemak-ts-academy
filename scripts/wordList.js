import a from "./resources/wordlist.json" assert { type: "json" };
var masterList = a.masterList;
var sentence = a.sentence;
var wordLists = {
    lvl1: [],
    lvl2: [],
    lvl3: [],
    lvl4: [],
    lvl5: [],
    lvl6: [],
    lvl7: [],
};
var alphabet = "abcdefghijklmnopqrstuvwxyz',.-";
// generate new list that includes certain letters and excludes others
var customList = [];
// returns the index of the nth occurance of a char or string
function getPosition(target, subString, n) {
    return target.split(subString, n).join(subString).length;
}
// returns true if target (a string) contains at least one letter from 
// pattern (an array of chars)
function contains(target, pattern) {
    let value = 0;
    pattern.forEach(function (letter) {
        value = value + Number(target.includes(letter));
    });
    return (value >= 1);
}
// returns true if target contains ALL letters in pattern, which is an array of chars
function containsAll(target, pattern) {
    let value = 0;
    pattern.forEach(function (letter) {
        value = value + Number(target.includes(letter));
    });
    return (value >= pattern.length);
}
function clearLists() {
}
// generates a list of words containing only the given letters
function generateList(lettersToInclude, requiredLetters) {
    let excludes = [];
    // create the list of letters to exclude from final list so 
    // at the end you have only desired letters
    alphabet.split("").forEach((l) => {
        if (!lettersToInclude.includes(l)) {
            excludes.push(l);
        }
    });
    let wordList = [];
    masterList.forEach((word) => {
        if (!contains(word.toLowerCase(), excludes) && contains(word, requiredLetters.split(''))) {
            wordList.push(word);
        }
    });
    return wordList;
}
export { masterList, sentence, wordLists, getPosition, contains, generateList };
