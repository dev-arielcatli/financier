import { mergeApplicationConfig, ApplicationConfig } from '@angular/core';
import { provideServerRendering } from '@angular/platform-server';
import { provideServerRoutesConfig } from '@angular/ssr';
import { appConfig } from './app.config';
import { serverRoutes } from './app.routes.server';
import {
  provideTanStackQuery,
  QueryClient,
} from '@tanstack/angular-query-experimental';
const serverConfig: ApplicationConfig = {
  providers: [
    provideServerRendering(),
    provideServerRoutesConfig(serverRoutes),
    provideTanStackQuery(new QueryClient()),
  ],
};

export const config = mergeApplicationConfig(appConfig, serverConfig);
