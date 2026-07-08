import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-aptitude',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './aptitude.html',
  styleUrl: './aptitude.css',
})
export class Aptitude {

  time = 30 * 60;

  current = 0;

  score = 0;

  submitted = false;

  message = '';

  answers: (number | null)[] = [];

questions = [

{
q:"Profit % if CP=800 SP=1000?",
options:["20","25","30","40"],
answer:1
},

{
q:"Speed 120 km in 2 hrs?",
options:["50","60","70","80"],
answer:1
},

{
q:"25% of 640?",
options:["140","150","160","170"],
answer:2
},

{
q:"Average of 10,20,30,40,50?",
options:["25","30","35","40"],
answer:1
},

{
q:"Next: 2,4,8,16,?",
options:["18","24","32","36"],
answer:2
},

{
q:"SI of 5000 at 10% for 2 yrs?",
options:["500","750","1000","1200"],
answer:2
},

{
q:"LCM of 12 and 18?",
options:["24","30","36","48"],
answer:2
},

{
q:"Square root of 225?",
options:["12","13","14","15"],
answer:3
},

{
q:"Odd one out Apple Banana Mango Car",
options:["Apple","Banana","Mango","Car"],
answer:3
},

{
q:"CAT→DBU DOG→?",
options:["EPH","EPG","FPH","EOH"],
answer:0
},

{
q:"3,6,12,24,?",
options:["36","42","48","54"],
answer:2
},

{
q:"A,C,E,G,?",
options:["H","I","J","K"],
answer:1
},

{
q:"Pen:Write Knife:?",
options:["Cut","Eat","Cook","Draw"],
answer:0
},

{
q:"Smallest prime?",
options:["0","1","2","3"],
answer:2
},

{
q:"Angle 3:00?",
options:["60","90","120","180"],
answer:1
},

{
q:"Synonym Rapid",
options:["Slow","Fast","Weak","Small"],
answer:1
},

{
q:"Antonym Success",
options:["Victory","Failure","Growth","Profit"],
answer:1
},

{
q:"She ____ to college",
options:["go","goes","gone","going"],
answer:1
},

{
q:"Correct spelling",
options:["Recieve","Receive","Receeve","Receve"],
answer:1
},

{
q:"Opposite Ancient",
options:["Old","Historic","Modern","Traditional"],
answer:2
},

{
q:"Web structure language",
options:["Python","HTML","Java","C"],
answer:1
},

{
q:"Python comment",
options:["//","#","/*","<!--"],
answer:1
},

{
q:"FIFO structure",
options:["Stack","Queue","Tree","Graph"],
answer:1
},

{
q:"Java developer",
options:["Microsoft","Sun Microsystems","Google","IBM"],
answer:1
},

{
q:"Python function keyword",
options:["function","def","fun","define"],
answer:1
},

{
q:"C pointer symbol",
options:["&","*","#","@"],
answer:1
},

{
q:"C++ reuse feature",
options:["Loop","Inheritance","Recursion","Pointer"],
answer:1
},

{
q:"Java inheritance",
options:["implements","extends","inherit","super"],
answer:1
},

{
q:"HTML link tag",
options:["<a>","<link>","<href>","<url>"],
answer:0
},

{
q:"SQL query keyword",
options:["GET","SELECT","SHOW","FETCH"],
answer:1
}

,
{
q:"Which protocol is used to transfer web pages?",
options:["FTP","HTTP","SMTP","TCP"],
answer:1
},

{
q:"Which SQL command is used to remove a table?",
options:["DELETE","DROP","REMOVE","CLEAR"],
answer:1
},

{
q:"Which data structure uses LIFO?",
options:["Queue","Stack","Array","Tree"],
answer:1
},

{
q:"Which of these is an Operating System?",
options:["Windows","Python","Oracle","HTML"],
answer:0
},

{
q:"Which device connects multiple computers in a LAN?",
options:["Router","Switch","Monitor","Printer"],
answer:1
},

{
q:"Which company developed Angular?",
options:["Microsoft","Google","IBM","Oracle"],
answer:1
},

{
q:"Which keyword is used to create a class in Java?",
options:["define","class","new","object"],
answer:1
},

{
q:"Which HTML tag is used to display an image?",
options:["<img>","<image>","<pic>","<src>"],
answer:0
},

{
q:"Which database language is used to retrieve data?",
options:["INSERT","UPDATE","SELECT","DELETE"],
answer:2
},

{
q:"Which symbol is used to end a statement in C?",
options:[".",":",";","?"],
answer:2
}

];// We will add the remaining questions in the next step.
  

  constructor() {}

ngOnInit(){

  this.answers = new Array(this.questions.length).fill(null);

  setInterval(() => {

    if(!this.submitted){

      if(this.time > 0){

        this.time--;

      }
      else{

        this.submitTest();

      }

    }

  },1000);

}
  get minutes() {

    return Math.floor(this.time / 60);

  }

  get seconds() {

    return this.time % 60;

  }

  next() {

    if (this.current < this.questions.length - 1) {

      this.current++;

    }

  }

  prev() {

    if (this.current > 0) {

      this.current--;

    }

  }

  submitTest() {

  this.score = 0;

  for (let i = 0; i < this.questions.length; i++) {

    if (this.answers[i] === this.questions[i].answer) {

      this.score++;

    }

  }

  if (this.score >= 25) {

  this.message = "Excellent 🎉 Placement Ready";

}

else if (this.score >= 18) {

  this.message = "Good 👍 Keep Practicing";

}

else {

  this.message = "Need Improvement 📚";

}

  this.submitted = true;

}



restartTest()
{

  location.reload();

}


}