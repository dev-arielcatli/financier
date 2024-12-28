import { Injectable } from '@angular/core';
import { Endpoint } from './endpoint.model';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class EndpointService {
  constructor() {}

  API_ACTIONS = {
    GET: 'GET',
    POST: 'POST',
    PUT: 'PUT',
    DELETE: 'DELETE',
    LIST: 'LIST',
  };

  API_KEY = 'api';

  EXPENSE_ENDPOINTS: Endpoint = {
    [this.API_ACTIONS.GET]: `${this.API_KEY}/expense/{expenseId}`,
    [this.API_ACTIONS.POST]: `${this.API_KEY}/expense/`,
    [this.API_ACTIONS.PUT]: `${this.API_KEY}/expense/{expenseId}/`,
    [this.API_ACTIONS.DELETE]: `${this.API_KEY}/expense/`,
    [this.API_ACTIONS.LIST]: `${this.API_KEY}/expense/`,
  };

  INCOME_ENDPOINTS: Endpoint = {
    [this.API_ACTIONS.GET]: `${this.API_KEY}/income/{incomeId}`,
    [this.API_ACTIONS.POST]: `${this.API_KEY}/income/`,
    [this.API_ACTIONS.PUT]: `${this.API_KEY}/income/{incomeId}/`,
    [this.API_ACTIONS.DELETE]: `${this.API_KEY}/income/`,
    [this.API_ACTIONS.LIST]: `${this.API_KEY}/income/`,
  };

  buildEndpoint(endpoint: string, params: Record<string, string>): string {
    const BASE_URL = environment.apiURL;
    let path = endpoint;
    Object.entries(params).forEach(([key, value]) => {
      path = path.replace(`{${key}}`, value);
    });

    return `${BASE_URL}/${path}`;
  }
}
