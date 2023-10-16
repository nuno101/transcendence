import { Controller, Post} from "@nestjs/common";
import { AuthService } from "./auth.service";

@Controller('auth')
export class AuthController {
    constructor(private authService: AuthService){}

    // Here only the logic for the request/response.
    // Here only logic for database connection.

    @Post('signup') 
    signup(){
        //signup route http://localhost:3000/signup
        return this.authService.signup()
    }

    @Post('signin')
    signin(){
        //signin route http://localhost:3000/signup
        return this.authService.signin()
    }

} // End of AuthController Class