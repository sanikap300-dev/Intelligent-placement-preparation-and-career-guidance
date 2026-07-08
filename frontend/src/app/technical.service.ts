import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class TechnicalService {


  private apiUrl = "http://127.0.0.1:5000/technical";


  constructor(private http: HttpClient) { }


  getTechnicalQuestions(){

    return this.http.get<any[]>(this.apiUrl);

  }


}