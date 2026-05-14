import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

import { RegisterComponent } from './register/register';
import { LoginComponent } from './login/login';
import { ProfileComponent } from './profile/profile';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    RegisterComponent,
    LoginComponent,
    ProfileComponent
  ],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {

  currentPage = 'register';

}