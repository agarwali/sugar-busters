import { Component } from 'angular2/core';
import { Router, RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from 'angular2/router';

import { VariableRouteComponent } from '../variable-route/variable-route.component';
import { HomeComponent } from '../home/home.component';
//import { LoginComponent } from '../login/login.component';

@Component({ 
  selector: 'my-app',
  templateUrl: 'static/src/app/app.component.html',
  styleUrls: ['static/src/app/app.component.css'],
  directives: [ROUTER_DIRECTIVES],
  providers: [ROUTER_PROVIDERS]
})

@RouteConfig([
  {
    path: '/',
    name: 'Home',
    component: HomeComponent
  },
  {
    path: '/:university',
    name: 'Variable',
    component: VariableRouteComponent
  }
])

export class AppComponent {
  title = "DerbyHacks";
  constructor(private _router: Router) {
  }
  
  getCoolDataFromKyesAPI() {
    this.title += " - You added to the text";
  }
  
  goToUniversity(university: string) {
    this._router.navigate(['Variable', { university: university }]);
  }
}