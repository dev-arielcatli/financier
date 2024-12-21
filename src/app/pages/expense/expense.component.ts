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
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

import { MatInputModule } from '@angular/material/input';
import {
  MatDialog,
  MatDialogModule,
  MatDialogRef,
} from '@angular/material/dialog';
import { ExpenseFormComponent } from './expense-form/expense-form.component';
import { Expense, SafeDisplayExpense } from './expense.model';
import { mockExpenses } from './mocks/expenses.mock';
import { CommonModule } from '@angular/common';

import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { ShortenPipe } from '../../shared/shortener.pipe';
import { MatSortModule } from '@angular/material/sort';

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
    MatButtonModule,
    MatIconModule,
    MatSortModule,
  ],
  templateUrl: './expense.component.html',
  styleUrl: './expense.component.scss',
})
export class ExpenseComponent implements AfterViewInit {
  @ViewChild(MatPaginator) expenseTablePaginator!: MatPaginator;

  expenseDialog = inject(MatDialog);
  expenseDialogRef!: MatDialogRef<ExpenseFormComponent>;

  EXPENSE_COLUMNS: string[] = [
    'name',
    'description',
    'quantity',
    'amount',
    'date',
  ];

  private rawExpenses = signal<Expense[]>(mockExpenses);
  expenses: Signal<SafeDisplayExpense[]> = computed(() => {
    const formattedExpenses = this.formatExpenses(this.rawExpenses());
    this.expenseDataSource = new MatTableDataSource<SafeDisplayExpense>(
      formattedExpenses,
    );
    return formattedExpenses;
  });

  expenseDataSource = new MatTableDataSource<SafeDisplayExpense>([]);

  ngAfterViewInit(): void {
    // TODO: computed() signals are only computed when they are accessed.
    this.expenses();
    this.expenseDataSource.paginator = this.expenseTablePaginator;
  }

  onAddExpense(): void {
    this.expenseDialogRef = this.expenseDialog.open(ExpenseFormComponent, {});
    this.subscribeToExpenseDialogClose();
  }

  private formatExpenses(expenses: Expense[]): SafeDisplayExpense[] {
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

  private onExpenseDialogClose(expense: Expense): void {
    if (expense) {
      if (expense.id) {
        console.log('Update expense', expense);
      } else {
        console.log('Create expense', expense);
      }
    }
  }

  subscribeToExpenseDialogClose(): void {
    this.expenseDialogRef.afterClosed().subscribe((payload) => {
      this.onExpenseDialogClose(payload);
    });
  }

  onRowClick(expense: Expense): void {
    this.expenseDialog.open(ExpenseFormComponent, {
      data: expense,
    });
  }
}
