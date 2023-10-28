import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { UserEntity } from '../models/user.entity';
import { Repository } from 'typeorm';
import { from, Observable } from 'rxjs';
import { UserI } from '../models/user.interface';

@Injectable()
export class UserService {

    constructor(
        @InjectRepository(UserEntity)
        private userRepository: Repository<UserEntity>
    ) {}

    async add(user: UserI): Promise<UserI> {
        // Find the maximum id in the current user list
        const maxId = await this.userRepository.createQueryBuilder("user")
                        .select("MAX(user.id)", "maxId")
                        .getRawOne();

        // Set the id of the new user to be maxId + 1
        user.id = maxId ? maxId.maxId + 1 : 1;

        return this.userRepository.save(user);
    }

    findAll(): Observable<UserI[]> {
        return from(this.userRepository.find());
    }
}
