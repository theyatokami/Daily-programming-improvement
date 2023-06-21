interface Person {
  name: string;
  age: number;
}

class Greeter {
  greet(person: Person) {
    console.log(`Hello, ${person.name}! You are ${person.age} years old.`);
  }
}

const john: Person = { name: "John", age: 25 };
const greeter = new Greeter();
greeter.greet(john);
