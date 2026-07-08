import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TechnicalService } from '../technical.service';


@Component({
  selector: 'app-technical',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './technical.html',
  styleUrl: './technical.css'
})
export class Technical {


  questions: any[] = [];


  constructor(private technicalService: TechnicalService) { }



  ngOnInit() {

    this.technicalService.getTechnicalQuestions()
      .subscribe({

        next: (data:any[]) => {

          this.questions = data;

        },


        error: (err:any) => {

          console.log("Error loading technical questions", err);

        }

      });

  }



  showAnswer(id:number) {

    let answer = document.getElementById("a" + id);


    if(answer) {

      if(answer.style.display === "block") {

        answer.style.display = "none";

      }
      else {

        answer.style.display = "block";

      }

    }

  }


}