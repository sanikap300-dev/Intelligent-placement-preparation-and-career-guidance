import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-resume',
  standalone: true,
  imports: [
    FormsModule,
    CommonModule
  ],
  templateUrl: './resume.html',
  styleUrl: './resume.css'
})


export class Resume {


  student:any = null;


  formData:any = {

    name:"",
    email:"",
    phone:"",
    address:"",

    career:"",
    career_other:"",

    education:"",
    education_other:"",

    skills:[],

    project:"",
    project_other:"",

    experience:"",
    experience_other:"",

    languages:[],

    hobbies:[]

  };



  toggleSkill(skill:string){

    if(this.formData.skills.includes(skill))
    {
      this.formData.skills =
      this.formData.skills.filter(
        (x:any)=>x !== skill
      );
    }
    else
    {
      this.formData.skills.push(skill);
    }

  }



  toggleLanguage(lang:string){

    if(this.formData.languages.includes(lang))
    {
      this.formData.languages =
      this.formData.languages.filter(
        (x:any)=>x !== lang
      );
    }
    else
    {
      this.formData.languages.push(lang);
    }

  }




  toggleHobby(hobby:string){

    if(this.formData.hobbies.includes(hobby))
    {
      this.formData.hobbies =
      this.formData.hobbies.filter(
        (x:any)=>x !== hobby
      );
    }
    else
    {
      this.formData.hobbies.push(hobby);
    }

  }



  generateResume(){

    this.student = {

      ...this.formData,

      skills:this.formData.skills.join(", "),

      languages:this.formData.languages.join(", "),

      hobbies:this.formData.hobbies.join(", ")

    };

  }


}
