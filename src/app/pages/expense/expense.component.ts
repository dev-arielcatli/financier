import {
  AfterViewInit,
  Component,
  computed,
  inject,
  Signal,
  signal,
  effect,
  ViewChild,
} from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';

import { MatInputModule } from '@angular/material/input';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { ExpenseFormComponent } from './expense-form/expense-form.component';
import { Expense } from './expense.model';
import { mockExpenses } from './mocks/expenses.mock';
import { CommonModule } from '@angular/common';

import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { ShortenPipe } from '../../shared/shortener.pipe';

@Component({
  selector: 'fn-expense',
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatDialogModule,
    MatTableModule,
    MatPaginatorModule,
    ShortenPipe,
  ],
  templateUrl: './expense.component.html',
  styleUrl: './expense.component.scss',
})
export class ExpenseComponent implements AfterViewInit {
  @ViewChild(MatPaginator) expenseTablePaginator!: MatPaginator;

  expenseDialog = inject(MatDialog);

  EXPENSE_COLUMNS: string[] = [
    'name',
    'description',
    'quantity',
    'amount',
    'date',
  ];

  private rawExpenses = signal<Expense[]>(mockExpenses);
  expenses: Signal<Expense[]> = computed(() => {
    const formattedExpenses = this.formatExpenses(this.rawExpenses());
    this.expenseDataSource = new MatTableDataSource<Expense>(formattedExpenses);
    return formattedExpenses;
  });

  expenseDataSource = new MatTableDataSource<Expense>([]);

  ngAfterViewInit(): void {
    // TODO: computed() signals are only computed when they are accessed.
    this.expenses();
    this.expenseDataSource.paginator = this.expenseTablePaginator;
  }

  onAddExpense(): void {
    console.log('Add Expense');
    this.expenseDialog.open(ExpenseFormComponent, {});
  }

  private formatExpenses(expenses: Expense[]): Expense[] {
    return expenses.map((expense) => {
      return {
        ...expense,
        date: new Date(expense.date).toLocaleString('en-US', {
          weekday: 'long',
          day: 'numeric',
          month: 'long',
          year: 'numeric',
          hour: 'numeric',
          minute: 'numeric',
          hour12: true,
        }),
        createdAt: new Date(expense.createdAt).toLocaleString('en-US', {
          weekday: 'long',
          day: 'numeric',
          month: 'long',
          year: 'numeric',
          hour: 'numeric',
          minute: 'numeric',
          hour12: true,
        }),
        updatedAt: new Date(expense.updatedAt).toLocaleString('en-US', {
          weekday: 'long',
          day: 'numeric',
          month: 'long',
          year: 'numeric',
          hour: 'numeric',
          minute: 'numeric',
          hour12: true,
        }),
      };
    });
  }
}
