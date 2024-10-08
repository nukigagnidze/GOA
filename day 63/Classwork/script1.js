 function numbers(arr1) {
  let evernnums = [];
     for (let arr of arr1) {
         if (arr % 2 == 0) {
             evernnums.push(arr);
         }
     }
     return evernnums;
 }

 console.log(numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))