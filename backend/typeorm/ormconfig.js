// ormconfig.js

module.exports = {
  type: 'postgres',
  host: 'localhost',
  port: 3000,
  username: 'user',
  password: '1',
  database: 'database',
  synchronize: true,
  logging: true,
  entities: ['dist/**/*.entity{.ts,.js}'],
  migrations: ['dist/migrations/*{.ts,.js}'],
  cli: {
    migrationsDir: 'src/migrations',
  },
};
