import { createStore } from '@ngneat/elf';
import {
  withEntities,
  withActiveId,
  setEntities,
  selectAllEntities,
} from '@ngneat/elf-entities';
import { Expense } from './expense.model';
import { inject, Injectable } from '@angular/core';
import { joinRequestResult, trackRequestResult } from '@ngneat/elf-requests';
import { ExpenseApiService } from '../../pages/expense/expense.api.service';
import { tap } from 'rxjs';

const expenseStore = createStore(
  {
    name: 'Expense',
  },
  withEntities<Expense>({
    initialValue: [],
  }),
  withActiveId(),
);

@Injectable({
  providedIn: 'root',
})
export class ExpenseStoreFacadeService {
  store = expenseStore;

  expenseAPIService = inject(ExpenseApiService);

  $expenses = this.store.pipe(
    selectAllEntities(),
    joinRequestResult(['Expense']),
  );

  fetchExpenses() {
    return this.expenseAPIService.getExpenses().pipe(
      tap((expenses) => {
        this.addExpenses(expenses);
      }),
      trackRequestResult(['Expense']),
    );
  }

  addExpenses(expenses: Expense[]): void {
    this.store.update(setEntities(expenses));
  }
}
