const getMissingLetter = (words) => {
  let prevCode = undefined;
  let result = [];
  for (let i = 0; i < words.length; i++) {
    if (!prevCode) {
      prevCode = words.charCodeAt(i);
      continue;
    }

    if (words.charCodeAt(i) - prevCode !== 1) {
      const missingCode = words.charCodeAt(i) - 1;
      const missingLetter = String.fromCharCode(missingCode);
      result.push(missingLetter);
      prevCode = missingCode + 1;
    } else {
      prevCode = words.charCodeAt(i);
    }
  }
  if (result.length) {
    return result.join(",");
  }
  return undefined;
};

console.log(getMissingLetter("bcefghijklmnopqrsuvxyz"));
