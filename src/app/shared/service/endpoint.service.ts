import { Injectable } from '@angular/core';
import { Endpoint } from './endpoint.model';

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
    [this.API_ACTIONS.GET]: `/expense/{expenseId}`,
    [this.API_ACTIONS.POST]: `/expense/`,
    [this.API_ACTIONS.PUT]: `/expense/{expenseId}/`,
    [this.API_ACTIONS.DELETE]: `/expense/`,
    [this.API_ACTIONS.LIST]: `/expense/`,
  };

  INCOME_ENDPOINTS: Endpoint = {
    [this.API_ACTIONS.GET]: `/income/{incomeId}`,
    [this.API_ACTIONS.POST]: `/income/`,
    [this.API_ACTIONS.PUT]: `/income/{incomeId}/`,
    [this.API_ACTIONS.DELETE]: `/income/`,
    [this.API_ACTIONS.LIST]: `/income/`,
  };

  buildEndpoint(endpoint: string, params: Record<string, string>): string {
    let path = endpoint;
    Object.entries(params).forEach(([key, value]) => {
      path = path.replace(`{${key}}`, value);
    });
    return `/${path}`;
  }
}
