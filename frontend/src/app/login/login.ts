import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Api } from '../services/api';
import { Router } from '@angular/router';



@Component({

selector:'app-login',

standalone:true,

imports:[
FormsModule
],

templateUrl:'./login.html',

styleUrl:'./login.css'

})


export class Login {



email="";

password="";



constructor(

private api:Api,

private router:Router

)

{

}




login()
{


let data={


email:this.email,


password:this.password


};



this.api.login(data)

.subscribe({



next:(response:any)=>{


alert(response.message);



localStorage.setItem(

"user",

JSON.stringify(response.user)

);



this.router.navigate(['/dashboard']);



},




error:(error:any)=>{


alert(error.error.message);



}



});



}



}