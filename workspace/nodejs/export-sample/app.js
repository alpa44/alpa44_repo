var msg = require('./message-literals.js');
var msg2 = require('./message-object.js');
var msg3 = require('./message-obj-with-function.js');
let msg4 = require('./message-obj2.js');
const msg5 = require('./message-function.js');
let person = require('./message-function-like-class');

console.log(msg);
console.log(msg2.SimpleMessage);
msg3.log('Hello World')
console.log(msg4.firstName + ' ' + msg4.lastName);
msg5('Hello World');

let person1 = new person('James', 'Bond');
console.log(person1.fullName());
