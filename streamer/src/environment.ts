import dotenv from 'dotenv';
import { resolve } from 'path';
import {
  IsNotEmpty, IsNumber,
  IsPort,
  IsString,
  IsUrl,
  Matches,
  MinLength,
  validate
} from 'class-validator';
import { plainToClass } from 'class-transformer';

dotenv.config({ path: resolve(__dirname, '.env') });

const applicationId = 'substrate_streamer';

class EnvironmentVariableConfig {
  @IsString()
  @IsNotEmpty()
  @MinLength(3)
  APP_ID!: string;

  get APP_CLIENT_ID(): string {
    return `mbelt-${applicationId}-${this.APP_MODE.toLowerCase()}-${this.APP_NETWORK.toLowerCase()}`;
  }

  @IsString()
  APP_MODE = 'dev';

  @IsNotEmpty()
  @MinLength(3)
  APP_NETWORK!: string;

  @IsString()
  LOG_LEVEL = 'info';

  // Api
  @IsUrl()
  API_ADDR = '0.0.0.0';

  @IsPort()
  API_PORT = '8080';

  // Node
  @IsNotEmpty()
  @IsUrl()
  @MinLength(3)
  SUBSTRATE_URI!: string;

  // Kafka
  @IsNotEmpty()
  @Matches(/^\\w+:\\d+$/, {
    message: `KAFKA_URI should be set as pattern "hostname:port"`
  })
  @MinLength(3)
  KAFKA_URI!: string;

  @IsString()
  get KAFKA_PREFIX(): string {
    return `SUBSTRATE_STREAMER_${this.APP_MODE.toUpperCase()}_${this.APP_NETWORK.toUpperCase()}`;
  };

  // Postgres
  @IsNotEmpty()
  @IsString()
  @MinLength(3)
  DB_HOST = 'localhost';

  @IsPort()
  DB_PORT = '5432';

  @IsNotEmpty()
  @MinLength(3)
  DB_NAME = 'postgres';

  @IsNotEmpty()
  @MinLength(3)
  DB_USER!: string;

  @IsString()
  DB_PASSWORD = '';

  @IsString()
  DB_SCHEMA = 'public';

  //App config
  @IsNumber()
  ERA_EXTRACTION_OFFSET = 4;
}

const environment = plainToClass(EnvironmentVariableConfig, process.env);
// eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
const validateEnv = async () => await validate(environment);

export {
  environment,
  validateEnv
}
