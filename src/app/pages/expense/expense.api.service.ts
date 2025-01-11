import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Expense, NewExpense } from './expense.model';
import { EndpointService } from '../../shared/service/endpoint.service';

@Injectable({
  providedIn: 'root',
})
export class ExpenseApiService {
  httpClient = inject(HttpClient);
  endpointService = inject(EndpointService);
  constructor() {}

  getExpenses(userId: string = 'default'): Observable<Expense[]> {
    return this.httpClient.get<Expense[]>('/v1/expense', {
      params: { user_id: userId },
    });
  }

  getExpense(expenseId: string, userId: string): Observable<Expense> {
    return this.httpClient.get<Expense>(
      this.endpointService.buildEndpoint(
        this.endpointService.EXPENSE_ENDPOINTS[
          this.endpointService.API_ACTIONS.GET
        ],
        { expenseId },
      ),
      {
        params: { user_id: userId },
      },
    );
  }

  addExpense(newExpense: NewExpense, userId: string): Observable<Expense> {
    return this.httpClient.post<Expense>('/v1/expense', newExpense, {
      params: { user_id: userId },
    });
  }
}
