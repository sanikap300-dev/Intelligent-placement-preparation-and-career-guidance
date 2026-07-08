import { Routes } from '@angular/router';
import { Home } from './home/home';
import { Aptitude } from './aptitude/aptitude';
import { Technical } from './technical/technical';
import { Interview } from './interview/interview';
import { Resume } from './resume/resume';

export const routes: Routes = [

  {
    path:'',
    component:Home
  },

  {
    path:'aptitude',
    component:Aptitude
  },

  {
    path:'technical',
    component:Technical
  },

  {
    path:'interview',
    component:Interview
  },


{
 path:'resume',
 component:Resume
}

];