// ormconfig.js

module.exports = {
  type: 'postgres',
  host: process.env.POSTGRES_DB,
  port: process.env.POSTGRES_PORT,
  username: process.env.POSTGRES_USER,
  password: process.env.POSTGRES_PASSWORD,
  database: process.env.POSTGRES_DB,
  synchronize: true,
  logging: true,
  entities: ['dist/**/*.entity.js'],
  migrations: ['dist/migrations/*{.ts,.js}'],
  cli: {
    migrationsDir: '../src/migrations',
  },
};