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
import {
  Expense,
  NewExpense,
  SafeDisplayExpense,
} from '../../store/expense/expense.model';
import { CommonModule } from '@angular/common';

import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { ShortenPipe } from '../../shared/shortener.pipe';
import { MatSortModule } from '@angular/material/sort';

import { Chart, ChartData } from 'chart.js/auto';

import { toSignal } from '@angular/core/rxjs-interop';
import { ExpenseStoreFacadeService } from '../../store/expense/expense.store';
import { RequestResult } from '@ngneat/elf-requests';
import { FormatDatePipe } from '../../shared/data-formatter.pipe';

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
    FormatDatePipe,
    MatButtonModule,
    MatIconModule,
    MatSortModule,
  ],
  templateUrl: './expense.component.html',
  styleUrl: './expense.component.scss',
})
export class ExpenseComponent implements AfterViewInit {
  // STORE
  expenseStore = inject(ExpenseStoreFacadeService);

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
    'total',
    'date',
  ];

  expenseEntities = toSignal<
    RequestResult<any, Expense[]> & { data: Expense[] }
  >(this.expenseStore.$expenses);

  expenses = computed<SafeDisplayExpense[]>(() => {
    const entities = this.expenseEntities();
    if (entities?.isSuccess) {
      return this.formatExpenses(entities.data || []).sort(
        this.sortExpenseByDate,
      );
    }
    return [];
  });

  expensesIsLoading = computed<boolean>(() => {
    return !!this.expenseEntities()?.isLoading;
  });

  constructor() {
    effect(() => {
      this.setExpenseTableData();
      this.recomputeChartData();
    });
  }

  expenseDataSource = new MatTableDataSource<SafeDisplayExpense>([]);

  private recomputeChartData() {
    const chartData = this.createChartData(this.expenses(), 21);
    this.updateChart(chartData);
  }

  ngAfterViewInit(): void {
    this.expenseStore.fetchExpenses().subscribe();
    this.initializeChart();
    this.recomputeChartData();
  }

  onAddExpense(): void {
    this.expenseDialogRef = this.expenseDialog.open(ExpenseFormComponent, {});
    this.subscribeToExpenseDialogClose();
  }

  private setExpenseTableData = () => {
    this.expenseDataSource = new MatTableDataSource<SafeDisplayExpense>(
      this.expenses(),
    );
    if (this.expenseTablePaginator) {
      this.expenseDataSource.paginator = this.expenseTablePaginator;
    }
  };

  private sortExpenseByDate(a: Expense, b: Expense) {
    return new Date(a.date).getTime() - new Date(b.date).getTime();
  }

  private initializeChart(): void {
    this.summaryChart = new Chart(
      (this.summaryChartCanvas as ElementRef<HTMLCanvasElement>).nativeElement,
      {
        type: 'line',
        data: { labels: [], datasets: [] },
        options: {
          maintainAspectRatio: false,
        },
      },
    );
  }

  private updateChart(chartData: ChartData): void {
    if (this.summaryChart) {
      this.summaryChart.data = chartData;
      this.summaryChart.update();
    }
  }

  private createChartData(expenses: Expense[], duration: number): ChartData {
    const filteredExpenses = this.filterExpensesBasedOnDate(duration, expenses);
    const labels: string[] = [];
    const data: number[] = [];

    filteredExpenses.forEach((expense) => {
      labels.push(
        new Date(expense.date).toLocaleString('en-US', {
          day: '2-digit',
          month: 'short',
        }),
      );
      data.push(expense.amount * expense.quantity);
    });

    return {
      labels,
      datasets: [
        {
          label: 'Your 3-week Expenses',
          data,
        },
      ],
    };
  }

  private filterExpensesBasedOnDate(
    duration: number,
    expenses: Expense[],
  ): Expense[] {
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    const daysAgo = new Date();
    daysAgo.setDate(today.getDate() - duration);
    daysAgo.setHours(0, 0, 0, 0);
    const filteredExpenses = expenses.filter((expense) => {
      const expenseDate = new Date(expense.date);
      expenseDate.setHours(0, 0, 0, 0);
      return expenseDate >= daysAgo && expenseDate <= today;
    });
    return filteredExpenses;
  }

  private formatExpenses(expenses: Expense[]): SafeDisplayExpense[] {
    return expenses.map((expense) => {
      return {
        ...expense,
        total: expense.amount * expense.quantity,
      };
    });
  }

  private onExpenseDialogClose(expense: Expense & NewExpense): void {
    if (expense) {
      console.log(expense);
      if (expense.id) {
        this.expenseStore
          .updateExpense({
            ...expense,
            date: new Date(expense.date),
          })
          .subscribe();
      } else {
        this.expenseStore.addExpense(expense as NewExpense).subscribe();
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
