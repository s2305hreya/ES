import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './login.html'
})
export class LoginComponent {

  email = '';
  password = '';

  login() {

    let user:any = JSON.parse(localStorage.getItem('user') || '{}');

    if(this.email == user.email && this.password == user.password) {

      alert("Login Successful");
    }
    else {

      alert("Invalid Email or Password");
    }

  }

}