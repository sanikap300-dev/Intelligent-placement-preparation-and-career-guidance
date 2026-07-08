import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.css'
})
export class Dashboard {

  user: any;

  constructor(private router: Router) {

  }

  ngOnInit() {

    let data = localStorage.getItem("user");

    if (data) {

      this.user = JSON.parse(data);

    } else {

      this.router.navigate(['/login']);

    }

  }

  aptitude() {

    this.router.navigate(['/aptitude']);

  }

  logout() {

    localStorage.removeItem("user");

    this.router.navigate(['/login']);

  }

}