// const printTwo = () => {
//   return new Promise((res, rej) => {
//     setTimeout(() => {
//       res(console.log(2));
//     }, 2000);
//   });
// };

// const printResult = async () => {
//   console.log(1);
//   await printTwo();
//   console.log(3);
// };

// printResult();

// for (let i = 0; i < 5; i++) {
//   if (i === 3) {
//     continue;
//   }
//   console.log(i);
// }

// [1,2,3,4,5].forEach((i) => {
// if (i === 3) {
//     continue;
//     }
//     console.log(i);
// })

// for (var i = 1; i < 5; i++) {
//   setTimeout(() => {
//     console.log(i);
//   }, 1000);
// }

// const x = 5
// x = x+1
// console.log(x)

// function digitalRoot(n) {
//   if (n === undefined) {
//     return 0;
//   }
//   let str = n.toString();
//   let res = 0;
//   for (let i = 0; i < str.length; i++) {
//     res += parseInt(str[i]);
//   }
//   if (res > 9) {
//     return digitalRoot(res);
//   } else {
//     return res;
//   }
// }
// console.log(digitalRoot());

// const fnB = () => {
//   console.log(1);
// };

// const fnA = () => {
//   return fnB();
// };

// const result = fnA()

// let b = null;
// b = b+"avc"
// console.log(b)


// function generateHashtag (str) {
//     let res = str.trim().split(' ');
//     return res.map((r) => (r[0]))
//     // const resMap = (str) => { console.log(res[str][0]) }
//     // resMap(str)
// }
// console.log(generateHashtag(" Hello there thanks for trying my Kata"))

function generateHashtag (str) {
    let res = [];
    if(str.length !== 0){
        let strLst = str.trim().split(' ');
        let arr = strLst.map((string) => {
           string.length > 0 ? res.push(string[0].toUpperCase() + string.slice(1, string.length)) : null ;
        })
        const finAns = ('#' + res.join(''));
        if(finAns.length > 140){
            return false;
        }else {
            return finAns;
        }
    }else{
        return false
    }
}
generateHashtag("  ")