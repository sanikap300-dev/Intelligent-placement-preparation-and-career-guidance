import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-interview',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './interview.html',
  styleUrl: './interview.css'
})
export class Interview {

  showAnswer(id: number) {

    const answer = document.getElementById("a" + id);

    if (answer) {
      answer.style.display =
        answer.style.display === "block" ? "none" : "block";
    }

  }

}