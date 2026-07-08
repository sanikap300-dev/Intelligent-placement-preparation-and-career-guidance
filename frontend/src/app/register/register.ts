import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Auth } from '../services/auth';



@Component({

  selector: 'app-register',

  standalone: true,

  imports: [
    FormsModule
  ],

  templateUrl: './register.html',

  styleUrl: './register.css'

})


export class Register {


  fullname = "";

  email = "";

  mobile = "";

  college = "";

  branch = "";

  password = "";

  confirmPassword = "";




  constructor(private auth: Auth)
  {

  }





  register()
  {


    let userData = {


      fullname: this.fullname,

      email: this.email,

      mobile: this.mobile,

      college: this.college,

      branch: this.branch,

      password: this.password


    };





    this.auth.register(userData)

    .subscribe({


      next: (response:any) =>
      {


        alert(response.message);


      },


      error: (error:any) =>
      {


        alert(error.error.message);


      }


    });



  }



}