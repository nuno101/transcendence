import { Injectable } from "@nestjs/common";

@Injectable()
export class AuthService{


    signin(){
        // Logic goes here
        return 'I am signed in, response from service'
    }
    signup(){
        // Logic goes here
        return 'I am signed up, response from service'
    }

} // End of AuthService Class