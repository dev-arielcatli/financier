import {
  AfterViewInit,
  Component,
  computed,
  inject,
  Signal,
  signal,
  effect,
  ViewChild,
  ElementRef,
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

import { Chart } from 'chart.js/auto';
import { ExpenseApiService } from './expense.api.service';

import { toSignal } from '@angular/core/rxjs-interop';
import { tap } from 'rxjs';

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
  // SERVICES
  expenseApiService = inject(ExpenseApiService);

  // DIALOGS
  expenseDialog = inject(MatDialog);
  expenseDialogRef!: MatDialogRef<ExpenseFormComponent>;

  // SUMMARY
  @ViewChild('summaryChartCanvas') summaryChartCanvas!: ElementRef;
  summaryChart!: Chart;
  summaryMessage = signal<string>(
    'Manage your expenses in here and have insights with your spending.',
  );

  // TABLE
  @ViewChild(MatPaginator)
  private _expenseTablePaginator!: MatPaginator;
  public get expenseTablePaginator(): MatPaginator {
    return this._expenseTablePaginator;
  }
  public set expenseTablePaginator(value: MatPaginator) {
    this._expenseTablePaginator = value;
  }
  EXPENSE_COLUMNS: string[] = [
    'name',
    'description',
    'quantity',
    'amount',
    'date',
  ];

  expenses = toSignal<Expense[]>(
    this.expenseApiService.getExpenses().pipe(
      tap((expenses) => {
        if (!!expenses) {
          const formattedExpenses = this.formatExpenses(expenses);
          this.expenseDataSource = new MatTableDataSource<SafeDisplayExpense>(
            formattedExpenses,
          );
        }
      }),
    ),
  );

  expenseDataSource = new MatTableDataSource<SafeDisplayExpense>([]);

  ngAfterViewInit(): void {
    if (!!this.expenses()) {
      const formattedExpenses = this.formatExpenses(
        this.expenses() as Expense[],
      );
      this.expenseDataSource = new MatTableDataSource<SafeDisplayExpense>(
        formattedExpenses,
      );
    }
    this.expenseDataSource.paginator = this.expenseTablePaginator;
    this.initializeChart();
  }

  onAddExpense(): void {
    this.expenseDialogRef = this.expenseDialog.open(ExpenseFormComponent, {});
    this.subscribeToExpenseDialogClose();
  }

  private initializeChart(): void {
    this.summaryChart = new Chart(
      (this.summaryChartCanvas as ElementRef<HTMLCanvasElement>).nativeElement,
      {
        type: 'line',
        data: {
          labels: Array.from(
            { length: 21 },
            (_, i) => new Date(2024, 11, 22 + i),
          ).map((d) =>
            new Date(d).toLocaleString('en-US', {
              day: '2-digit',
              month: 'short',
            }),
          ),
          datasets: [
            {
              label: 'Your 3-week expenses',
              data: [...Array(100).keys()].map(
                (number) => Math.random() * 10000,
              ),
            },
          ],
        },
        options: {
          maintainAspectRatio: false,
        },
      },
    );
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
    this.expenseDialogRef = this.expenseDialog.open(ExpenseFormComponent, {
      data: expense,
    });
    this.subscribeToExpenseDialogClose();
  }
}
