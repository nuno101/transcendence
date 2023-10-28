import { Controller, Post, Body, Get, Req } from '@nestjs/common';
import { UserService } from '../service/user.service';
import { Observable, from } from 'rxjs';
import { UserI } from '../models/user.interface';

@Controller('users')
export class UserController {

    constructor(private readonly userService: UserService) {}

    @Post()
    add(@Req() req: any, @Body() user: UserI): Observable<UserI>
    {
        console.log(req.body);
        // Convert the Promise to an Observable
        return from(this.userService.add(user));
    }

    @Get()
    findAll(): Observable<UserI[]>
    {
        return this.userService.findAll();
    }
}
