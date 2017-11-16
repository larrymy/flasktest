var request = require('request');
var fs = require("fs");

var csv = require("csvtojson");



// Convert a csv file with csvtojson
csv()
  .fromFile('order.csv')
  .on("end_parsed",function(jsonArrayObj){ //when parse finished, result will be emitted here.

  	var req = request({
        // url: 'http://192.168.0.115:2000/fav',
      	url: 'http://127.0.0.1:5000/hi',
      	method: "POST",
      	headers: {
          "content-type": "application/json",
          },
      	json: {file2: jsonArrayObj}
  	}, function(error, response, body){
          console.log("yo");
          console.log(body);
          console.log("yo2");
  	});

  })

// csv()
//   .fromFile('order.csv')
//   .on("end_parsed",function(jsonArrayObj){ //when parse finished, result will be emitted here.

//     var req = request({
//         // url: 'http://192.168.0.115:2000/fav',
//         url: 'http://192.168.0.115:2000/customer',
//         method: "POST",
//         headers: {
//           "content-type": "application/json",
//           },
//         json: {file2: jsonArrayObj}
//     }, function(error, response, body){
//           console.log("yo");
//           console.log(body);
//           console.log("yo2");
//     });

//   })